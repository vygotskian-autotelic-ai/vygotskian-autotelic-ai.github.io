---
layout: default
---


<h2 class="page-title"> List of papers</h2>

{{ site.data.paperlist.papers.size }} papers are listed. 

You can click on each title to display more information, including authors, url to pdf, abstract and bibtex. 

{% comment %} tags:
<span class="badge embodied">Embodied</span>
<span class="badge supervised">Supervised Learning</span>
<span class="badge env">Environment</span>
<span class="badge autotelic">Autotelic</span>
<span class="badge all">All</span> ––>
{% endcomment %}

{% assign paperlist = site.data.paperlist.papers | group_by: 'year' | sort:"name"  %}
{% for yeargroup in paperlist reversed %}
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
		<details><summary><b class="paper-title">{{ item.title }}</b>
		{% for tag in item.tags %}
			{% if tag contains "Embodied" %}<span class="badge embodied">Embodied</span>{% endif %}
			{% if tag contains "earning" %}<span class="badge supervised">Supervised Learning</span>{% endif %}
			{% if tag contains "Autotelic" %}<span class="badge autotelic">Autotelic</span>{% endif %}
			{% if tag contains "Environment" %}<span class="badge env">Env</span>{% endif %}
		{% endfor %}
		
		</summary>
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

