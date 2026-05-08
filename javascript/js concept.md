# JS concept

### map function
data.map((obj,idx)=>(
//statement
))

-------------------------------------------------------
TypeScript
-------------------------------------------------------
1. why create an interface in TypeScript why not class?
- TS mein hum interfaces isliye use karte hain kyunki humein sirf "Shape of the Data" define karni hoti hai. Lightweight: Interface JS code mein convert nahi hote, so zero overhead. Flexibility: TS "Structural Typing" use karta hai. Agar object ka structure interface se match karta hai, toh TS khush hai.Easy to Extend: Aap multiple interfaces ko easily merge ya extend kar sakte ho.Difference at a Glance Feature Interface (TS)Class (TS/Java)Runtime Presence No (gayab ho jata hai)Yes (exists in JS/JVM) Memory Lightweight Heavy (methods aur logic store hota hai) Purpose Data structure define karna Logic aur Data dono handle karna
   


# ShadCn
---------------------------------------------------------------------------
### How implement sidebar in nextjs.

1. open sidebar install in project.
2. visit in sidebar block component copy and past all component from there







# React Js
------------------------------------------------------------------------------------------------------------------


# Create React App.
npm create vite@latest
name of project
select rect
select javascript
npm install axios,react-router-dom

#Setup Routes
```
import { BrowserRouter, Route, Routes } from 'react-router-dom'
   <BrowserRouter>
<Routes>
<Route path='/' element={<Home/>}/>
</Routes>
    </BrowserRouter>

```

npm install I


npm version conflict error
Error: error:0308010C:digital envelope routines::unsupported
set in json file script start:

 "start": "set NODE_OPTIONS=--openssl-legacy-provider && react-scripts start",



# Next Js
---
### React Query (tanstack) setup
-----------------------
```
1. Add or install Tanstack React Query from Tanstack documentation
2. Wrap QueryClientProvider with the root file, create ReactQueryProvider, and return QueryClientProvider,
 also pass client in queryclientProvider.

useQuery ----> Get Request
useMutation -> Put post Delete Request
vvi: React Quuery only work in client component

ex:
 # Create ReactQueryProvider component or provider folder
"use client";
import { QueryClientProvider, QueryClient } from "@tanstack/react
import { useState } from "react";

interface Props {
children: React. ReactNode;
}
export default function ReactQueryProvider({ children }: Props) {
const [queryClient] = useState(() => new QueryClient());
return (
<QueryClientProvider client={queryClient}> {children} </Query


# Now wrap in root layout
<html lang="en">
<body>
<QueryProvider>{children}</QueryProvider>
</body>
</html>



```

### How request send using tanstack Get and Post

------------
i. Get Request
------------------


1. create useQueryClient()
2. create useQuery  hook in there pass 2 attribute in that object, key & api function. 
- Key-> this for data cache, another time direct get using this if available otherwise it automatic fetch from db.
- Function -> this for Api service method so it call api.

```
//step 1
 const queryClient = useQueryClient();
 //step 2
  const { data: wholesellers } = useQuery({
    queryKey: ["wholeseller"],
    queryFn: getWholeseller,
  });

```

ii. post method
-----------------------
1. first create mutation function using useMutation Hook and pass object, in obj there pass api service method, success, and error function.
2. make submit Handler there call mutation method.
   
 ```
  const sizeMutation = useMutation({
    mutationFn: createSize,
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ["sizes"] }); // Automatically refetch   <--------------- using queryClient pass key which set from get request, it will refresh data
      setNewSizeName("");
      toast.success("Size added successfully");
    },
    onError: () => toast.error("Failed to add size"),
  });
  
  const handleAddSize = () => {
    if (!newSizeName.trim()) return toast.error("Please enter a size name");
    sizeMutation.mutate({ name: newSizeName });
  };

```



### React Hook Form
-----

### Zod validation
---------
1. install zod and Resolver, it found in schema section in react hook form docs.
   - npm install @hookform/resolvers yup
2. Create Schema,
   - it also have feature to convert direct schema into interface so not need to create interface direct convert



# Hook
useSearchParams: Yeh current URL ko Read karta hai. (Jaise: URL mein abhi kya filter laga hai?)

URLSearchParams: Yeh ek helper hai jo naya URL string Likhta/Modify karta hai. (Jaise: Purane filters mein 'Sort' bhi add kar do).

router.push: Yeh naye URL par Navigate karta hai. (Jaise: Naya link apply kar do).



_debouncedSubmit()



// app/dashboard/page.tsx
async function getUserData() {
  const res = await fetch('https://api.your-springboot.com/user/profile', {
    // Isse Next.js server par data cache NAHI karega
    cache: 'no-store', 
    headers: {
      'Authorization': 'Bearer YOUR_TOKEN'
    }
  });
  
  return res.json();
}
