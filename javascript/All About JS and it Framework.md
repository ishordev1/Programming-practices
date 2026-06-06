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
### Data show in field

```
<select {...register(`variants.${index}.size`)}>
  <option value="">Select Size</option>

  {sizes.map((size) => (
    <option key={size.id} value={size.name}>
      {size.name}
    </option>
  ))}
</select>
```
```
  <Input
  list="sizes"
  {...register("size")}
/>

<datalist id="sizes">
  <option value="S" />
  <option value="M" />
  <option value="L" />
  <option value="XL" />
  <option value="XXL" />
</datalist>
```


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
### Replace vs Push

- Replace <- //replace not hold back page if go forwared. means user login and user want to go back it is not show singin page
- push <- it hold previous like user is go product page and then details page and again come in product page it will show.
  ```
  import { router } from 'next/router';
  router.push("/")
  router.replace("/");
  ```
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
1. useFormContext -> it is use for managing large form
- create one form provider and wrap all child form in that form.
- Also create one submit button, when button click it will get all data in one place

  ```
const page = () => {
const methods=useForm<Product>()
 const onSubmit=(data:Product)=>{
  console.log(`data: ${data}`);
  
 }
  return (
   <>
   <FormProvider {...methods}>
    <form>
<BasicDetails/>
  <Button onSubmit={methods.handleSubmit(onSubmit)}>submit</Button>
    </form>

   </FormProvider>
   </>
  );
};
  ```


### Zod validation
- it is use to validate input fields with a custom method and check in frontend without hitting the backend request.
---------
1. install zod and Resolver, it found in schema section in react hook form docs.
   - npm install @hookform/resolvers yup
2. Create Schema,
   - it also have feature to convert direct schema into interface so not need to create interface direct convert






# React Hook Form , Zod validation and tanstack query
--------------------------------
```

const SizeManagement = () => {
  const useClient = useQueryClient();
  const { data: sizes, isLoading } = useQuery({
    queryKey: ["sizes"],
    queryFn: getAllSizes,
  });


const {register,handleSubmit,reset,formState:{errors,isSubmitting}}=useForm<SizeRequest>({
    resolver: zodResolver(SizeRequestSchema),
})

  const createSizeMutation=useMutation({
    mutationFn:createSize,
    onSuccess:()=>{
        useClient.invalidateQueries({queryKey:["sizes"]})
        toast.success("create size successfully")
    },
    onError:(error:any)=>{
        toast.error(error.message|| "fail to create size")
    }
  })




  return (
    <>
      <Card className="w-full  mt-4">
        <CardHeader>
          <CardTitle>Size Management</CardTitle>
          <CardDescription>manage all size </CardDescription>
        </CardHeader>
        <CardContent>
          <Separator />
          <form  onSubmit={handleSubmit((data)=>createSizeMutation.mutate(data))}>
            <div className="flex items-center mt-4">
              <Field className="w-[50%]">
                <FieldLabel htmlFor="size">Enter size Here</FieldLabel>
                <Input id="size" {...register("name",{required:true})} />
              {errors.name && (
                  <span className="text-red-600">This field is required</span>
                )}
              </Field>
              <div className="mt-7 mx-3">
                <Button>Add Size</Button>
              </div>
            </div>
          </form>

```

# Zustand
- It is a library same like context api, and the redux toolkit, which manages state automatically.
- Context API is only used in small applications, and Redux is very complex.
- Zustand is easy and flexible, and is also used in large projects.

### How to Use Zustand?
 - Install zustand from the documentation.
 - create store folder and there create store file. 
 - create function in that store file using zustand and add the state which you manage on application.
 - also create function on that zustan function for edit or update of that state.
 - when ever you want to use or change state, just import zustand store file and bring out that function and store in new variable and work.

```
// src/store/useCounterStore.js
import { create } from 'zustand';

const useCounterStore = create((set) => ({
  // 1. Initial State
  count: 0,

  // 2. Actions (State ko update karne ke liye)
  increment: () => set((state) => ({ count: state.count + 1 })),
  decrement: () => set((state) => ({ count: state.count - 1 })),
  reset: () => set({ count: 0 }),
}));

export default useCounterStore;

```
```
// src/components/Counter.jsx
"use client";

import useCounterStore from "@/store/useCounterStore";

export default function Counter() {
  // Store se state aur actions ko select karein
  const count = useCounterStore((state) => state.count);
  const increment = useCounterStore((state) => state.increment);
  const decrement = useCounterStore((state) => state.decrement);
  const reset = useCounterStore((state) => state.reset);

  return (
    <div style={{ padding: "20px", border: "1px solid #ccc", borderRadius: "8px" }}>
      <h2>Counter Component</h2>
      <h1>Count: {count}</h1>
      
      <div style={{ display: "flex", gap: "10px" }}>
        <button onClick={increment} style={{ padding: "10px" }}>Increment</button>
        <button onClick={decrement} style={{ padding: "10px" }}>Decrement</button>
        <button onClick={reset} style={{ padding: "10px", backgroundColor: "red", color: "white" }}>Reset</button>
      </div>
    </div>
  );
}
```
  ### Persist
  - It is also part of zustand.
  - It is used to sync state with local storage automatically. So that Not lose value after refreshing the page.

  - first pass perist and in call back function, also put name of object for accessing the local storage value.
```
import { create } from 'zustand'
import { persist, createJSONStorage } from 'zustand/middleware'

export const useBearStore = create()(
  persist(
    (set, get) => ({
      bears: 0,
      addABear: () => set({ bears: get().bears + 1 }),
    }),
    {
      name: 'food-storage', // name of the item in the storage (must be unique)
      storage: createJSONStorage(() => sessionStorage), // (optional) by default, 'localStorage' is used
    },
  ),
)

```

# React Drop Zone
1. it is use to upload file
2. Install it library
3. getRootProps, getInputProps -> this two help to open the form for drag file and handle the file in the form. without this can't open the form for drag

```   
import { useCallback, useState } from 'react'
import { useDropzone } from 'react-dropzone'
function App() {
const [state, setState] = useState << File []>([])
const { getRootProps, getInputProps, isDragActive } = useDropzone({
onDrop: useCallback((files: any)=>{
// console.log(files);
setState(files)
}, [])
})
return (
<>
<h1>Hello React DropZone</h1>
<div className="root-file" {...getRootProps()} >
<input {...getInputProps()} />
{
isDragActive ?
<p>Drop the files here ...</p> :
<p>Drag 'n' drop some files here, or click to select files</p>
}
</div>
<div className="">
{
state && state.length > 0 && state.map((c,i)=>{
return <img key={i} src={URL.createObjectURL(c)} width={200} height={200}/>
})
}
</div>
```
   
1. or using component
   
```
function App() {
const [state, setState] = useState<File[]>([])
return (
<>
<h1>Hello React DropZone</h1>
<DropZoneComponent setState={setState} />
<div className="">
{
state && state.length > 0 && state.map((c,i)=>{
return <img key={i} src={URL.createObjectURL(c)} width= {200} height={200} alt="" />
})
}
</div>
</>
}
export default App
 

Const DropZoneComponent = ({setState):any)=>{
const onDrop = useCallback((files: any) => {
console. Log(files);
setState (files)
｝，[]）
const { getRootProps, getInputProps, isDragActive } = useDropzone ((
onDrop
return
<＞
‹div className="root-file" {...getRootProps()} ›
‹input {...getInputProps()} /›
isDragActive ?
‹p›Drop the files here ...‹/p› :
‹p›Drag 'n' drop some files here, or click to select files</p>
</div>
</>

```




# Multi Stepper Form
```
const ProductStepper = () => {
  const [activeStep, setActiveStep] = useState(0);
  const [formData, setFormData] = useState({
    basicInfo: {},
    variants: [],
    images: []
  });

  const steps = ['Basic Details', 'Variants & Stock', 'Images & Media', 'Review'];

  const handleNext = () => setActiveStep((prev) => prev + 1);
  const handleBack = () => setActiveStep((prev) => prev - 1);

  return (
    <div className="w-full p-6">
      {/* Step Indicator */}
      <div className="flex justify-between mb-8">
        {steps.map((label, index) => (
          <div key={label} className={`flex-1 text-center border-b-4 pb-2 ${activeStep >= index ? 'border-blue-600 text-blue-600' : 'border-gray-200'}`}>
            <span className="font-bold">{index + 1}.</span> {label}
          </div>
        ))}
      </div>

      {/* Dynamic Step Content */}
      <div className="bg-white p-8 rounded shadow">
        {activeStep === 0 && <BasicInfoForm data={formData.basicInfo} onUpdate={(val) => setFormData({...formData, basicInfo: val})} />}
        {activeStep === 1 && <VariantsForm variants={formData.variants} />}
        {activeStep === 2 && <ImageUploadSection images={formData.images} />}
        {activeStep === 3 && <ReviewAndSubmit data={formData} />}
      </div>

      {/* Navigation Buttons */}
      <div className="mt-8 flex justify-between">
        <button disabled={activeStep === 0} onClick={handleBack} className="px-6 py-2 bg-gray-300 rounded">Back</button>
        {activeStep === steps.length - 1 ? (
          <button onClick={finalSubmit} className="px-6 py-2 bg-green-600 text-white rounded">Final Save</button>
        ) : (
          <button onClick={handleNext} className="px-6 py-2 bg-blue-600 text-white rounded">Next</button>
        )}
      </div>
    </div>
  );
};
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
