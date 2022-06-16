---
layout: default
---


<h3 class="page-title"> List of papers</h3>

This list of {{ site.data.paperlist.papers.size }} papers include algorithms leveraging the cognitive functions of language. 
We use 5 different tags:
* <span class="badge supervised">Disembodied</span> refers to disembodied agents usually based on supervised learning algorithms.
* <span class="badge embodied">Embodied</span> refers to embodied agents usually trained with reinforcement learning algorithms.
* <span class="badge autotelic">Autotelic</span> refers to embodied agents able to represent, generate, pursue and master their own goals (see a review [here](https://arxiv.org/abs/2012.09830)). 
* <span class="badge vygotskian">Vygotskian</span> refers to disembodied or embodied agents that internalize social linguistic production (see details [here](https://arxiv.
  org/abs/2206.01134)).
* <span class="badge vaai">VAAI</span> refers to **embodied**, **Vygotskian** and **autotelic** agents.

Click on the paper's title to display the list of authors, the abstract, a link to the article and the bibtex. 

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
			{% if tag contains "earning" %}<span class="badge supervised">Disembodied</span>{% endif %}
			{% if tag contains "Autotelic" %}<span class="badge autotelic">Autotelic</span>{% endif %}
			{% if tag contains "Vygotskian" %}<span class="badge vygotskian">Vygotskian</span>{% endif %}
			{% if tag contains "VAAI" %} <span class="badge vaai">VAAI</span>{% endif %}
			{% if tag contains "Environment" %}<span class="badge env">Env</span>{% endif %}
		{% endfor %}
		
		</summary>
		<blockquote>
		{% if item.authors %}
		   <h4 class="blockquote-content" style="margin-top:10px;">Authors:</h4>
			{{ item.authors }}
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

