from utils import TENSE_MAP


def audio(card_type):
    kr_tense = TENSE_MAP[card_type]
    return f"""    {{{{tts ko_KR voices=Apple_Yuna,Apple_Suhyun,Microsoft_Haemi:{kr_tense}}}}}
    {{{{tts ko_KR voices=Apple_Minsu:{kr_tense}}}}}"""

def more_info():
    return """
<div class="double_desc">{{English Description}}</div>
<hr>
<div class="double_desc">{{Korean Description}}</div>"""

def identifier(card_type):
    return f"""
<div class="identifier">{card_type}</div>"""

def duplicateScript(card_type):
    
    tense = TENSE_MAP[card_type]
    tags = {"English": {
        "general": "EnglishDuplicate",
        "specific": tense + "EnglishDuplicate"
        },
        "Korean": {
            "general": "KoreanDuplicate",
            "specific": tense + "Duplicate"
        }
    }


    return f"""
  <script>
    function duplicateDisplayEnglish(language) {{
      if ("{{{{Duplicates}}}}".includes("{tags["English"]["general"]}")){{
        document.getElementById("duplicateEnglish").style.display = "inline-block";
        document.getElementById("duplicateEnglish").innerText = "{tags["English"]["general"]}";
      }}
      else if ("{{{{Duplicates}}}}".includes("{tags["English"]["specific"]}")){{
        document.getElementById("duplicateEnglish").style.display = "inline-block";
        document.getElementById("duplicateEnglish").innerText = "{tags["English"]["specific"]}";
      }}
    }}

    function duplicateDisplayKorean(language) {{
      if ("{{{{Duplicates}}}}".includes("{tags["Korean"]["general"]}")){{
        document.getElementById("duplicateKorean").style.display = "inline-block";
        document.getElementById("duplicateKorean").innerText = "{tags["Korean"]["general"]}";
      }}
      else if ("{{{{Duplicates}}}}".includes("{tags["Korean"]["specific"]}")){{
        document.getElementById("duplicateKorean").style.display = "inline-block";
        document.getElementById("duplicateKorean").innerText = "{tags["Korean"]["specific"]};"
      }}
    }}
    duplicateDisplayEnglish();
    duplicateDisplayKorean();
  </script>
"""