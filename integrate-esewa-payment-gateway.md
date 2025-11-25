# Integrate eSewa Payment Gateway

Create an order and redirect to a specific URL, but also send the following data from the server to the frontend:
- Total price  
- Order ID  
- Description  

Take that data in the frontend, create a form automatically, and redirect to the payment gateway URL (given in eSewa docs) after 2 seconds.
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
</body>
</html>

```


