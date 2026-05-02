# JS concept

### map function
data.map((obj,idx)=>(
//statement
))

-------------------------------------------------------
TypeScript
-------------------------------------------------------
1. why create an interface in TypeScript why not class?
TS mein hum interfaces isliye use karte hain kyunki humein sirf "Shape of the Data" define karni hoti hai.Lightweight: Interface JS code mein convert nahi hote, so zero overhead.Flexibility: TS "Structural Typing" use karta hai. Agar object ka structure interface se match karta hai, toh TS khush hai.Easy to Extend: Aap multiple interfaces ko easily merge ya extend kar sakte ho.Difference at a GlanceFeatureInterface (TS)Class (TS/Java)Runtime PresenceNo (gayab ho jata hai)Yes (exists in JS/JVM)MemoryLightweightHeavy (methods aur logic store hota hai)PurposeData structure define karnaLogic aur Data dono handle karna
   


------------------------------------------------------------------------------------
# ShadCn
---------------------------------------------------------------------------
### How implement sidebar in nextjs.
```
1. open sidebar install in project.
2. visit in sidebar block component copy and past all component from there

```






--------------------------------------------------------------------------------------------------------
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


-----------------------------------------------------------------------------------------------------------------------
# Next Js
----------------------------------------------------------------------------------------------------------------------
### React Query (tanstack) setup
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
