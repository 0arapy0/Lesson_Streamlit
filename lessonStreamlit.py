import streamlit as st
import numpy as np
#import pandas as pd
#from PIL import Image

st.title('Streamlit 超入門')
st.write('DataFrame')


# df=pd.DataFrame({
#     '1列目':[1,2,3,4],
#     '2列目':[10,20,30,40]
# })

#st.write(df)

#動的なTable：DataFrame
#https://docs.streamlit.io/library/api-reference/data/st.dataframe
#st.dataframe(df,width=500,height=500)
#st.dataframe(df.style.highlight_max(axis=0))

#静的なTable：Static Table
#https://docs.streamlit.io/library/api-reference/data/st.table
#st.table(df.style.highlight_max(axis=0))

#折れ線グラフ
# df=pd.DataFrame(
#     np.random.rand(20,3),
#     columns=['a','b','c']
# )
# st.line_chart(df)
# st.area_chart(df)
# st.bar_chart(df)

#地図表示
df=pd.DataFrame(
    np.random.rand(100,2)/[50,50]+[35.69,139.70],
    columns=['lat','lon']
)
st.map(df)


#画像
# st.write('Display Iamge')
# img=Image.open('Lesson_Streamlit/IMG_6788.JPG')
# #st.image(img,caption='AAAA')
# st.image(img,caption='AAAA',use_column_width=True)

#マジックコマンド
"""
# 章
## 節
### 項

```python
import streamlit as st
import numpy as np
import pandas as pd
```
"""