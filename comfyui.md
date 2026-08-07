# Comfy UI Basic to advance notes

- ctrl+B -----------------> bypass node
## Node Details:
- Load Image in node  -----> Load Image
- crop image --------> image crop
- save output ------> save Image
- for writing notes------------> note
- Only view image not save in file ----------> preview Image
  
### 1. load checkpoint
- It is use for modal load

### 2. modal alway get 2 Input for prompt understanding
1. For Positive prompt
2. For negative prompt

- that two input use same node for prompt give------------> clip text encode (prompt)
- do color for visual positive negative only

### 3. Empty Latent Image
- this node use to give size width and height

### 4. KSampler
- this is actual work/operation perform
- Actual it is deside how much time, how output want all manage from here
  
1. seed <---- this is use to get consist output or random
2. 

### 5. VAE Decode
- Here all things come and it give final shape after all things come.
- allthings made and come, it give only shape here. Means presentation state

### 6. save Image 
- now here save node

# run in colab
- !git clone repo  link
- ls   or !pwd   or %cd /content/ComfyUI
- %cd ComfyUi
- !pip install -r requirements.txt
- !python main.py --listen --enable-cors-header                         <------here also enable cross origin
- copy url and open pinggy past url and from pinggy copy and in colab  past in terminal, hit enter type yes
-  


 # Pinggy
 - it is a bridge tunnel where expose local ip in internet, so after expose any user can access that application in the internet.
 - when comfy ui install in colab, it can only run in colab means colab is local virtual mechine, so we expose it ip in internet and direct access that ip with other browser or anyother device.
