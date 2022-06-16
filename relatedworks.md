---
layout: default
---

This list of {{ site.data.background.papers.size }} papers contains inter-disciplinary background research on the subject of Vygotskian Autotelic AI. 


{% assign paperlist = site.data.background.papers | group_by: 'domain' | sort:"name"  %}
{% for yeargroup in paperlist %}
{% if yeargroup.name == "" %}
<h3 class="page-title">Undated: {{ yeargroup.size }} Papers</h3>
{% else %}
<h3 class="page-title" >{{ yeargroup.name }}: {{ yeargroup.size }} Papers</h3>
{% endif %}
<ul>
	{% assign sortedgroup = yeargroup.items | sort:"title"  %}
	{% for item in sortedgroup %}
	{% if item.title %}
	<li>
		<details><summary><b class="paper-title">{{ item.title }}</b></summary>
		<blockquote>
		{% if item.authors %}
		   <h4 class="blockquote-content">Authors:</h4>
		   <ul>
		   {% for author in item.authors %}
		      <li>{{ author }}</li>
		   {% endfor %}
		   </ul>
		{% endif %}
		{% if item.abstract %}
		   <h4 class="blockquote-content" >Abstract:</h4>
		   {{ item.abstract }}
		{% endif %}
		{% if item.pdfurl or item.codeurl or item.webpageurl %}
		   <h4 class="blockquote-content">Links:</h4>
		   <ul>
		   {% if item.pdfurl %}
		   <li><a href="{{ item.pdfurl }}">Paper</a></li>
		   {% endif %}
		   {% if item.codeurl %}
		   <li><a href="{{ item.codeurl }}">Source-code</a></li>
		   {% endif %}
		   {% if item.webpageurl %}
		   <li><a href="{{ item.webpageurl }}">Webpage</a></li>
		   {% endif %}
		   </ul>
		{% endif %}
		{% if item.bibtex %}	 
		   <h4 class="blockquote-content">Bibtex:</h4>
		   <pre><code>{{ item.bibtex }}</code></pre>
		{% endif %}
		<hr>
		 </blockquote>
		</details>
	</li>
	{% endif %}
	{% endfor %}
</ul>
{% endfor %}


