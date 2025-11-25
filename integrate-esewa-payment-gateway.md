# Integrate eSewa Payment Gateway
res.render('customer/payment-failure'); --> this means customer folder has payment-failure.ejs file
1. Create an order and redirect to a specific URL, but also send the following data from the server to the frontend:
- Total price  
- Order ID  
- Description  

2. Take that data in the frontend, create a form , and redirect to the payment gateway URL (given in eSewa docs) after 2 seconds or put button after click that redirect on there.
```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Redirecting to eSewa...</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
    <div class="container my-5">
        <div class="row justify-content-center">
            <div class="col-md-6 text-center">
                <div class="spinner-border text-success mb-3" role="status" style="width: 3rem; height: 3rem;">
                    <span class="visually-hidden">Loading...</span>
                </div>
                <h3>Redirecting to eSewa Payment Gateway...</h3>
                <p class="text-muted">Please wait while we redirect you to secure payment.</p>
                <p class="mt-4">Order #: <strong><%= order.orderNumber %></strong></p>
                <p>Amount: <strong>NPR <%= order.totalAmount.toLocaleString() %></strong></p>
            </div>
        </div>
    </div>
    
    <form id="esewaForm" action="<%= paymentUrl %>" method="POST" style="display: none;">
        <input type="hidden" name="amount" value="<%= paymentData.amount %>">
        <input type="hidden" name="tax_amount" value="<%= paymentData.tax_amount %>">
        <input type="hidden" name="total_amount" value="<%= paymentData.total_amount %>">
        <input type="hidden" name="transaction_uuid" value="<%= paymentData.transaction_uuid %>">
        <input type="hidden" name="product_code" value="<%= paymentData.product_code %>">
        <input type="hidden" name="product_service_charge" value="<%= paymentData.product_service_charge %>">
        <input type="hidden" name="product_delivery_charge" value="<%= paymentData.product_delivery_charge %>">
        <input type="hidden" name="success_url" value="<%= paymentData.success_url %>">
        <input type="hidden" name="failure_url" value="<%= paymentData.failure_url %>">
        <input type="hidden" name="signed_field_names" value="<%= paymentData.signed_field_names %>">
        <input type="hidden" name="signature" value="<%= paymentData.signature %>">
    </form>
    
    <script>
        // Auto-submit form after 2 seconds
        setTimeout(function() {
            document.getElementById('esewaForm').submit();
        }, 2000);
    </script>
// if you not want automatic then create button to redirect after submit
    
</body>
</html>

```

3. Esewa handle payment after they redirect into success or error url, if success check and verify with esewa payment is success  or fail with encryption token. 
    if success then also update in your order data.
```

// Payment success callback
exports.paymentSuccess = async (req, res) => {
    try {
        // eSewa sends response as base64 encoded data
        const encodedData = req.query.data;
        
        if (!encodedData) {
            console.error('No data received from eSewa');
            return res.redirect('/payment/failure');
        }
        
        // Decode base64 data
        const decodedData = Buffer.from(encodedData, 'base64').toString('utf-8');
        const responseData = JSON.parse(decodedData);
        
        console.log('eSewa Response:', responseData);
        
        const { 
            transaction_code, 
            status, 
            total_amount, 
            transaction_uuid, 
            product_code, 
            signed_field_names, 
            signature
        } = responseData;
        
        // Verify signature
        const isValid = esewaPayment.verifySignature({
            transaction_code,
            status,
            total_amount,
            transaction_uuid,
            product_code,
            signed_field_names,
            signature
        });
        
        if (!isValid) {
            console.error('Invalid signature');
            return res.redirect('/payment/failure');
        }
        
        if (status !== 'COMPLETE') {
            console.error('Payment not completed:', status);
            return res.redirect('/payment/failure');
        }
        
        // Find order by transaction UUID
        const order = await Order.findOne({ 'paymentDetails.oid': transaction_uuid });
        
        if (!order) {
            console.error('Order not found for transaction:', transaction_uuid);
            return res.redirect('/payment/failure');
        }
        
        // Update order payment status
        order.paymentStatus = 'Completed';
        order.orderStatus = 'Processing';
        order.paymentDetails = {
            transactionId: transaction_code,
            refId: responseData.ref_id || '',
            oid: transaction_uuid,
            paymentDate: new Date()
        };
        await order.save();
        
        // Update customer total spent
        const customer = await Customer.findOne({ email: order.customer.email });
        if (customer) {
            customer.totalSpent += order.totalAmount;
            await customer.save();
        }
        
        res.render('customer/payment-success', { order });
        
    } catch (error) {
        console.error('Payment success error:', error);
        res.redirect('/payment/failure');
    }
};

// Payment failure callback
exports.paymentFailure = async (req, res) => {
    try {
        const { transaction_uuid } = req.query;
        
        if (transaction_uuid) {
            // Find and update order status
            const order = await Order.findOne({ 'paymentDetails.oid': transaction_uuid });
            if (order) {
                order.paymentStatus = 'Failed';
                await order.save();
                
                // Restore product stock
                for (const item of order.items) {
                    const product = await Product.findById(item.product);
                    if (product) {
                        const variantIndex = product.variants.findIndex(v => v.size === item.variant.size);
                        if (variantIndex !== -1) {
                            product.variants[variantIndex].stock += item.quantity;
                            await product.save();
                        }
                    }
                }
            }
        }
        
        res.render('customer/payment-failure');
        
    } catch (error) {
        console.error('Payment failure error:', error);
        res.render('customer/payment-failure');
    }
```
