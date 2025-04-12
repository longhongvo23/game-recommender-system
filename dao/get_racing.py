import streamlit.components.v1 as components
from process.process_data import *

def get_racing():
  # Danh sách URL hình ảnh
  for i in range(0,20):
    game = top_racing.iloc[i]
    game_name = game['name']
    game_url = "https://store.steampowered.com/app/" + str(game['appid'])
    header_image = game['header_image']
    price = game['price']*25427.50
    formatted_price = '{:,.2f}'.format(price)
    f_price = str(formatted_price)
    short_description = game['short_description']
    release_date = game['release_date']
    developer = game['developer']
    publisher = game['publisher']
    tags = game['steamspy_tags']
    tags = eval(tags)
    thumbnail_urls = get_path_thumbnails(game['screenshots'])
    html_output = f"""
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
* {{box-sizing: border-box}}
body {{font-family: Arial, Helvetica, sans-serif; margin:0}}
.mySlides {{
  display: none;
  justify-content: center;
  align-items: center;
  display: flex;
}}

.main_container{{
  display: flex;
  padding:10px;
  position:relative;
  top:5px;
  background:#c7d5e0;
  flex-direction: column;
  border-radius: 25px;
  height:455px;
}}
/* Slideshow container */
.slideshow-container {{
  display: flex;
  position: relative;
  width: 100%;
  justify-content: center;
  align-items: center;
  border: 1px solid #c7d5e0;
  background: black;
  height: 240px;
  border-radius: 10px;
}}

.container{{
  display: flex;
  flex-direction: row;
}}

.slide_show{{
  display: flex;
  align-items: center;
  flex-direction: column;
  width: 60%;
}}

.info{{
  width: 40%;
  margin-left: 10px;
}}
.short_description{{
  height: 6em; /* Khoảng chiều cao cho 3-4 dòng văn bản */
  overflow: hidden; /* Ẩn phần nội dung vượt quá */
  display: -webkit-box;
  -webkit-line-clamp: 4; /* Số dòng tối đa */
  -webkit-box-orient: vertical;
  line-height: 1.5em; 
  font-size: 12px;
  margin-bottom: 15px;
}}

.header{{
  background-color: black; 
  -webkit-background-clip: text; 
  -webkit-text-fill-color: transparent;
}}

.text{{
  display: flex;
  flex-direction: row;
  margin-bottom: 3px;
}}
#toggleButton{{
  font-size: 12px;
}}
#collapseButton{{
  font-size: 12px;
}}
.text-dev-publ{{
  font-size: 12px;
  display: block;
}}
.boild{{
  color:#1B2838;
  font-size: 12px;
  width: 95px;
}}
#content{{
  margin-left: 5px;
}}
.headerdiv{{
  margin-left: 10px;
}}
.hidden{{
  display: none;
}}
/* Next & previous buttons */
.prev, .next {{
  cursor: pointer;
  position: absolute;
  top: 50%;
  width: auto;
  padding: 16px;
  margin-top: -22px;
  color: white;
  font-weight: bold;
  font-size: 18px;
  transition: 0.6s ease;
  border-radius: 0 3px 3px 0;
  user-select: none;
}}

/* Position the "next button" to the right */
.next {{
  right: 0;
  border-radius: 3px 0 0 3px;
}}
.prev {{
  left: 0;
  border-radius: 3px 0 0 3px;
}}
/* On hover, add a black background color with a little bit see-through */
.prev:hover, .next:hover {{
  background-color: rgba(0,0,0,0.8);
}}


/* The dots/bullets/indicators */
.dot {{
  cursor: pointer;
  height: 10px;
  width: 10px;
  margin: 0 2px;
  background-color: #bbb;
  border-radius: 50%;
  display: inline-block;
  transition: background-color 0.6s ease;
}}

.active, .dot:hover {{
  background-color: #717171;
}}

/* Fading animation */
.fade {{
  animation-name: fade;
  animation-duration: 1.5s;
}}

@keyframes fade {{
  from {{opacity: .4}} 
  to {{opacity: 1}}
}}

/* On smaller screens, decrease text size */
@media only screen and (max-width: 300px) {{
  .prev, .next,.text {{font-size: 11px}}
}}
</style>
</head>
<body>
<div class="main_container">
  <div class="headerdiv">
    <h4 class="header">
      <a href="{game_url}" target="_blank">{game_name}</a>
    </h4>
  </div>
  <div class="container".
    <!-- Container for the image gallery -->
    <div class="slide_show">
      <div class="slideshow-container">
        {" ".join([f'<div class="mySlides fade"><img src="{thub}" style="width:100%; border-radius:10px; height: 223px;vertical-align: middle;"></div>' for thub in thumbnail_urls])}
        <a class="prev" onclick="plusSlides(-1)">❮</a>
        <a class="next" onclick="plusSlides(1)">❯</a>
      </div>
      <div style="margin-bottom: 20px">
        {" ".join([f'<span class="dot" onclick="currentSlide({i + 1})"></span>' for i in range(len(thumbnail_urls))])}
      </div>
      <div>{" ".join([f'<div style="color: #66c0f4;padding: 2px 4px; margin: 2px; display: inline-block; background:#2a475e; border-radius: 5px;font-size:14px">{tag}</div>' for tag in tags])}</div>
    </div>

    <div class="info">
      <img src="{header_image}" alt="Header Image" style="width: 100%; border-radius: 5px;">
      <div class="short_description">{short_description}</div>
      <div class="text">
        <b class="boild">Release Date:</b>
        <div style="color:#1B2838; font-size: 12px;margin-left: 5px">{release_date}</div>
      </div>
      <div class="text">
        <b class="boild">Developer:</b>
        <div id="content">
"""
    if(len(developer)>2):
      html_output += " ".join([f'<a class = "text-dev-publ">{developer[i]}</a>' for i in range(0,2)])
      html_output += " ".join([f'<a class = "text-dev-publ hidden">{developer[i]}</a>' for i in range(2,len(developer))])
      html_output += """<button id="toggleButton">Extend</button>
                        <button id="collapseButton" class="hidden">Collapse</button>
                    """
    else:
      html_output += " ".join([f'<a class = "text-dev-publ">{dev}</a>' for dev in developer])
      
    html_output += f"""
        </div>
      </div>
      <div class="text">
        <b class="boild">Publisher:</b>
        <div id="content">
          {" ".join([f'<a class = "text-dev-publ">{pub}</a>' for pub in publisher])}
        </div>
      </div>
      <h5 style ="color: #BEEE11;background: #4c6b22; text-align: center; margin-top: 10px; padding: 10px; margin-left:40%;">
        {f_price} ₫
      </h5>
    </div>
  </div>
</div>

<script>
let slideIndex = 1;
showSlides(slideIndex);

function plusSlides(n) {{
  showSlides(slideIndex += n);
}}

function currentSlide(n) {{
  showSlides(slideIndex = n);
}}

function showSlides(n) {{
  let i;
  let slides = document.getElementsByClassName("mySlides");
  let dots = document.getElementsByClassName("dot");
  if (n > slides.length) {{slideIndex = 1}}    
  if (n < 1) {{slideIndex = slides.length}}
  for (i = 0; i < slides.length; i++) {{
    slides[i].style.display = "none";  
  }}
  for (i = 0; i < dots.length; i++) {{
    dots[i].className = dots[i].className.replace(" active", "");
  }}
  slides[slideIndex-1].style.display = "block";  
  dots[slideIndex-1].className += " active";
}}
</script>
<script>
 document.getElementById('toggleButton').addEventListener('click', function() {{
    var hiddenDevs = document.querySelectorAll('#content a.hidden');
    hiddenDevs.forEach(function(dev) {{
        dev.classList.remove('hidden');
    }});
    this.classList.add('hidden'); // Ẩn nút "Extend"
    document.getElementById('collapseButton').classList.remove('hidden'); // Hiển thị nút "Collapse"
}});

document.getElementById('collapseButton').addEventListener('click', function() {{
    var allDevs = document.querySelectorAll('#content a');
    allDevs.forEach(function(dev, index) {{
        if (index >= 2) {{
            dev.classList.add('hidden');
        }}
    }});
    document.getElementById('toggleButton').classList.remove('hidden'); // Hiển thị nút "Extend"
    this.classList.add('hidden'); // Ẩn nút "Collapse"
}});
</script>
</body>
</html> 
"""
    components.html(html_output, height=475)