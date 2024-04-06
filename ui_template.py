HTML_BANNER = """
    <div style="background-color: #464e5f; padding:10px;border-radius:10px"> 
    <h1 style="color:white; text-align:center;">Text Visualizer NLP App </h1> 
    </div>
    """

HTML_BANNER_SKEWED = """
  <style>
    header{
      position: relative;
      height: 200px;
      background-image: linear-gradient(#51b0f1,#464e54);
    }
    h2{
      margin: 0;
      padding:  50px 0;
      font: 44px "Aerial";
      text-align: center;
    }
    header h2{
      color: white;
    }

    .divider{
      position: absolute;
      bottom: 0;
      left:0;
      right: 0;
      width: 100%;
      height: 100px;
      /*drop the height to have a constant angle for all screen width*/
    }
  </style>
  <header>
    <h2>Text Visualizer NLP App</h2>
    <img src="https://erikdkennedy.com/r-r-r-random/divider-triangle.png" class="divider"/>
  </header>
  """

HTML_STICKER = """
  <style>
    *{
      margin: 0;
      padding: 0;
    }
    body{
      font-family: arial, sans-serif;
      font-size: 100%;
      margin: 1em;
      background: #666;
      color:#fff;
    }
    h2,p{
      font-size: 100%;
      font-weight: normal;
    }
    ul,li{
      list-style: none;
    }
    ul{
      overflow: hidden;
      padding: 3em;
    }
    ul li a{
      text-decoration: none;
      color:#000;
      background: #ffc;
      display: block;
      height: 10em;
      width: 10em;
      padding: 1em;
      -moz-box-shadow: 5px 5px 7px rgba(33,333,33,1);
      -webkit-box-shadow:5px 5px 7px rgba(33,333,33,.7);
      box-shadow: 5px 5px 7px rgba(33,333,33,.7);
      -moz-transition: -moz-transform .15s linear;
      -o-transition: -o-transform .15s linear;
      -webkit-transition: -webkit-transform .15s linear;     
    }
    ul li{
      margin: 1em;
      float: left;
    }
    ul li h2{
      font-size: 140%;
      font-weight: bold;
      padding-bottom: 10px;
    }
    ul li p{
      font-family: "Reenie Beanie",Arial, sans-serif;
      font-size: 80%;
    }
    ul li a{
      -webkit-transform: rotate(-6deg);
      -o-transform: rotate(-6deg);
      -moz-transform: rotate(-6deg);
      position: relative;
    }
    ul li:nth-child(even) a{
    -o-transform:rotate (4deg);
    -webkit-transform:rotate (4deg); 
    -moz-transform:rotate (4deg); 
    position:relative;
    top:5px;
    background:#cfc;
}
ul li:nth-child(3n) a{
-webkit-transform:rotate(-3deg);
      -moz-transform:rotate(-3deg);
      -o-transform:rotate(-3deg);
      position:relative; 
      top:-5px;
      background:#ccf;
    }
    ul li:nth-child(5n) a{
      -o-transform:rotate(5deg);
      -webkit-transform:rotate(5deg);
      -moz-transform:rotate(5deg);
      position:relative; 
      top:-10px;
    }
    ul li a:hover, ul li a:focus{
      box-shadow: 10px 10px 7px rgba(0,0,0,.7);
      -moz-box-shadow: 10px 10px 7px rgba(0,0,0,.7);
      -webkit-box-shadow: 10px 10px 7px rgba(0,0,0,.7);
      -webkit-transform: scale(1.25);
      -moz-transform: scale(1.25); 
      -o-transform: scale(1.25);
      position:relative; 
      z-index:5;
      }
      ol{text-align:center;}
      ol li{display:inline;padding-right: 1em; } 
      ol li a{color:#fff;}
    </style>
    <ul>
      <li>
        <a href="#">
          <h2>Text Visualization</h2>
          <p>Visualzing the Insights In Textual Data</p>
        </a>
      </li>
      <li>
        <a href="#">
          <h2>Text Viz Methods</h2>
          <p>word count</p>
          <p>Mendelhall Curve</p>
          <p>WordCloud</p>
          <p>Parts of Speech Tag</p>
          <p>Named Entity Recognition</p>
        </a>
      </li>
      <li>
        <a href="#">
          <h2>Application</h2>
          <p>Insights</p>
          <p>NLP</p>
          <p>Keyword Extraction</p>
          <p>forensic linguistics</p>
          <p>stc</p>
        </a>
      </li>
      <li>
        <a href="#">
          <h2>Tools and Pkgs</h2>
          <p>Pandas</p>
          <p>NLTK</p>
          <p>Spacy</p>
          <p>Neattext</p>
          <p>etc</p>
        </a>
      </li>
      <li>
        <a href="#">
          <h2>Libraries for Text Visualization</h2>
          <p>WordCloud</p>
          <p>Yellowbrick</p>
          <p>Spacy</p>
          <p>Matplotlib</p>
          <p>NLTK</p>
        </a>
      </li>
      <li>
      <a href="#">
        <h2>About</h2>
        <p>@streamlit</p>
      </a>
    </li>
    </ul>
"""

HTML_WRAPPER = """<div style="overflow-x:auto border:1px solid #464e5f; border-radius:0.25rem"></div>"""
