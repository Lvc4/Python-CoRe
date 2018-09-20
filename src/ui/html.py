
import webbrowser, sys, os

def to_html(string):
	return string.replace('&','&amp;').replace('<','&lt;').replace('>','&gt;').replace('\n','<br/>').replace(' ','&nbsp;')

def display(output, turn_count):
	print('Open protocol...')
	ai_1_base = os.path.basename(sys.argv[1])
	ai_2_base = os.path.basename(sys.argv[2])
	ai_1 = os.path.splitext(ai_1_base)[0]
	ai_2 = os.path.splitext(ai_2_base)[0]
	title = '{} / {}'.format(ai_1, ai_2)
	html = '<!DOCTYPE html>'
	html += '<title>{}</title>'.format(to_html(title))
	html += '''
		<style>
		body { font-family: monospace; background-color: rgb(50,50,50); color: rgb(150,150,150); }
		h1,h2,h3,.a { font-size: 32px; }
		a { color: rgb(200,200,200); }
		button { background-color: rgb(50,50,50); color: rgb(150,150,150); font-weight: bold;
			font-size: 24px; }
		table {background: rgb(100,100,100);}
		table, th, td {border: 1px solid black;border-collapse: collapse;}
		td, .X, .O { width: 64px; height: 64px; }
		.X {
			background: linear-gradient(to bottom right, grey, white);
			border-radius: 50%; }
		.O {
			background: linear-gradient(to bottom right, black, grey);
			border-radius: 50%; }
		</style>'''
	html += '<h1>{}</h1>'.format(to_html(title))
	head,*body = output
	id_ = 0
	html += '<h2>{}</h2>'.format(to_html(head))
	html += '<h3>{} Turns</h3>'.format(turn_count)
	html += '<hr/>'
	html += '''
		<button onclick="
			var styles = 'table{margin-bottom:100vh;}';
			var tag = document.createElement('style');
			tag.appendChild(document.createTextNode(styles));
			document.head.appendChild(tag);
			location.href = '#1';">
		Simulate</button>
		<button onclick="
			var turn = prompt('Turn [1-64]', '1');
			location.href = '#' + turn;">
		Goto</button>'''
	html += '<hr/>'
	html += '<div class="a">'
	for item in body:
		if isinstance(item, str):
			html += '<p>' + to_html(item) + '</p>'
		else:
			id_ += 1
			html += '<a id="{}" href="#{}">back</a> <a href="#{}">next</a>'.format(id_,id_-1,id_+1)
			html += '<table>'
			for row in item:
				html += '<tr>'
				for string in row:
					if string == '#':
						html += '<td>&nbsp;</td>'
					elif string == 'X':
						html += '<td><div class="X"></div></td>'
					elif string == 'O':
						html += '<td><div class="O"></div></td>'
					else:
						html += '<td>' + to_html(string) + '</td>'
				html += '</tr>'
			html += '</table>'
			html += '</div><div class="a">'
	html += '</div>'
	htmlfilename = '{}_v_{}.html'.format(ai_1, ai_2)
	myfile = open(htmlfilename,'w')
	myfile.write(html)
	myfile.close()
	webbrowser.open(htmlfilename)
