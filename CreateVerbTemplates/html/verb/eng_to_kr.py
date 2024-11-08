from utils import TENSE_MAP
from .. import common


def front(card_type):
    eng_tense = TENSE_MAP[card_type] + 'English'
    kr_tense = TENSE_MAP[card_type]
    return f"""
<body>	

  <div style="display: flex; justify-content: flex-end; width: 100%;">
    <div class="duplicate english" id="duplicateEnglish">
      ExampleDuplicate
    </div>
  </div>
  <div style="display: flex; justify-content: flex-end; width: 100%;">
    <div class="duplicate korean" id="duplicateKorean">
      ExampleDuplicate
    </div>
  </div>
  
  <div class="tense"><i>{kr_tense}</i></div> 
  <br>  
  <div class="identifier">{card_type}</div>
  <div class="title">{{{{{eng_tense}}}}}</div>
  <div class="subtitle">({{{{English}}}})</div>
  <br>
  <div id="input-area">{{{{type:{kr_tense}}}}}</div>
  <br>
  <hr>
  <div class="double_desc">{{{{English Description}}}}</div>
  
  {common.duplicateScript(card_type)}
</body>
"""

def back(card_type):
    eng_tense = TENSE_MAP[card_type] + 'English'
    kr_tense = TENSE_MAP[card_type]
    return f"""
<body>
  <div style="display: flex; justify-content: flex-end; width: 100%;">
    <div class="duplicate english" id="duplicateEnglish">
      ExampleDuplicate
    </div>
  </div>
  <div style="display: flex; justify-content: flex-end; width: 100%;">
    <div class="duplicate korean" id="duplicateKorean">
      ExampleDuplicate
    </div>
  </div>

<div>{{{{{eng_tense}}}}}</div>
<div>({{{{English}}}})</div>
<hr>
{{{{type:{kr_tense}}}}}
<br>
<br>
{common.audio(card_type)}
<br>
<br>
{common.more_info()}

{common.duplicateScript(card_type)}
</body>
"""