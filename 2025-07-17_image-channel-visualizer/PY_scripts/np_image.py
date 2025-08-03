import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
import requests
from io import BytesIO

def load_image(url):
    response = requests.get(url)
    return Image.open(BytesIO(response.content))



# elephant_url = "https://upload.wikimedia.org/wikipedia/commons/3/37/African_Bush_Elephant.jpg"
porshe_url = "https://content-hub.imgix.net/6H8edXTmr2k2YESRNhr616/9d44e2e239cefb4c0198660f37d823b2/the-20most-20iconic-20porsche-20colours.jpg?w=2064"
    
porshe = load_image(porshe_url)

# Display the image
plt.figure(figsize=(6,4))
plt.imshow(porshe)
plt.title("TWO BEAUTIES")
plt.axis("off")
plt.show()


# image to array

porshe_np = np.array(porshe)
print( "PORSHE_SHAPE",porshe_np.shape)