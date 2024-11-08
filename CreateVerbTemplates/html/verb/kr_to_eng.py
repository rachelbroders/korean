from .. import common
from utils import TENSE_MAP


def front(card_type):
    eng_tense = TENSE_MAP[card_type] + 'English'

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

  <div class="identifier">{card_type}</div>
  <div>
    {common.audio(card_type)}
  </div>
  {{{{type:{eng_tense}}}}}
  
  {common.duplicateScript(card_type)}
</body>
"""

def back(card_type):
    kr_tense = TENSE_MAP[card_type]
    eng_tense = TENSE_MAP[card_type] + 'English'

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

{{{{{kr_tense}}}}}
<hr>
</br>
{{{{type:{eng_tense}}}}}
</br>
{common.audio(card_type)}
<br>
<br>
{common.more_info()}

{common.duplicateScript(card_type)}
</body>
"""