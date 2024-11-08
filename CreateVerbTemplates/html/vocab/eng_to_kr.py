def front():
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

  <div style='font-family: "Arial"; font-size: 30px;'>
    <b>
      {{{{English}}}}
    </b>
  </div>

  <div style='display: none' class="identifier">
    eng_to_kr
  </div>

  <br>
  {{{{type:Korean}}}}
  <br>

  <div style='font-family: "Arial"; font-size: 20px; text-align: center;'>
    {{{{English Description}}}}
  </div>

  <script>
    function duplicateDisplayEnglish(language) {{
      if ("{{{{Duplicates}}}}".includes("EnglishDuplicate")){{
        document.getElementById("duplicateEnglish").style.display = "inline-block";
        document.getElementById("duplicateEnglish").innerText = "EnglishDuplicate";
      }}
      else if ("{{{{Duplicates}}}}".includes("PresentTenseEnglishDuplicate")){{
        document.getElementById("duplicateEnglish").style.display = "inline-block";
        document.getElementById("duplicateEnglish").innerText = "PresentTenseEnglishDuplicate";
      }}
    }}

    function duplicateDisplayKorean(language) {{
      if ("{{{{Duplicates}}}}".includes("KoreanDuplicate")){{
        document.getElementById("duplicateKorean").style.display = "inline-block";
        document.getElementById("duplicateKorean").innerText = "KoreanDuplicate";
      }}
      else if ("{{{{Duplicates}}}}".includes("PresentTenseDuplicate")){{
        document.getElementById("duplicateKorean").style.display = "inline-block";
        document.getElementById("duplicateKorean").innerText = "PresentTenseDuplicate;"
      }}
    }}
    duplicateDisplayEnglish();
    duplicateDisplayKorean();
  </script>

</body>

"""

def back():
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

{{{{English}}}}

<hr id=answer>
{{{{type:Korean}}}}
<br>
<br>
{{{{tts ko_KR voices=Apple_Yuna,Apple_Suhyun,Microsoft_Haemi:Korean}}}}
{{{{tts ko_KR voices=Apple_Minsu:Korean}}}}
<br>
<br>
<div style='font-family: "Arial"; font-size: 14px;'>{{{{Korean Description}}}}</div>
<hr>
<div style='font-family: "Arial"; font-size: 14px;'>{{{{English Description}}}}</div>

  <script>
    function duplicateDisplayEnglish(language) {{
      if ("{{{{Duplicates}}}}".includes("EnglishDuplicate")){{
        document.getElementById("duplicateEnglish").style.display = "inline-block";
        document.getElementById("duplicateEnglish").innerText = "EnglishDuplicate";
      }}
      else if ("{{{{Duplicates}}}}".includes("PresentTenseEnglishDuplicate")){{
        document.getElementById("duplicateEnglish").style.display = "inline-block";
        document.getElementById("duplicateEnglish").innerText = "PresentTenseEnglishDuplicate";
      }}
    }}

    function duplicateDisplayKorean(language) {{
      if ("{{{{Duplicates}}}}".includes("KoreanDuplicate")){{
        document.getElementById("duplicateKorean").style.display = "inline-block";
        document.getElementById("duplicateKorean").innerText = "KoreanDuplicate";
      }}
      else if ("{{{{Duplicates}}}}".includes("PresentTenseDuplicate")){{
        document.getElementById("duplicateKorean").style.display = "inline-block";
        document.getElementById("duplicateKorean").innerText = "PresentTenseDuplicate;"
      }}
    }}
    duplicateDisplayEnglish();
    duplicateDisplayKorean();
  </script>

</body>
"""