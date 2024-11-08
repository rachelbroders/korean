def front():
    return f"""
<div class="scrollable-content" onclick="toggleContent(this)">
  <div class="clickable-title">
    <div class="title-templates-container" style="display: flex; align-items: center;">
      <!-- Title aligned to the left -->
      <div class="title-left">
        <p class="g_title">{{{{title}}}}</p>
      </div>
    
      <!-- Templates aligned to the right -->
      <div>
        <table>
          <tr>
              {{{{#template1}}}}<td>{{{{template1}}}}</td>{{{{/template1}}}}
              {{{{#template2}}}}<td>{{{{template2}}}}</td>{{{{/template2}}}}
              {{{{#template3}}}}<td>{{{{template3}}}}</td>{{{{/template3}}}}
              {{{{#template4}}}}<td>{{{{template4}}}}</td>{{{{/template4}}}}
              {{{{#template5}}}}<td>{{{{template5}}}}</td>{{{{/template5}}}}
          </tr>
        </table>
      </div>
    </div>

    <p style="text-align: center;">
      <strong>Translation:</strong><br>{{{{translation}}}}
    </p>
  </div>

    <p><strong>Formality/Politeness:</strong></br>  {{{{formalPolite}}}}</p></br>
    <p><strong>Description:</strong></br>  {{{{description}}}}</p></br>
    <p><strong>Exceptions:</strong></br>  {{{{exceptions}}}}</p></br>
    <p><strong>Examples:</strong></br>  {{{{exampleSentences}}}}</p></br>
    <p><strong>Additional Notes:</strong></br> {{{{additionalNotes}}}}</p></br>
</div>

"""

def back():
    return ""