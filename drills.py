import random
from sys import exit

deutsch = {'a conduce catre':'zufuhren'}

words1 = {'dispretuitor (1)':'haughty', 'dispretuitor (2)':'disdainful','uzura':'attrition',
	'a toci (pentru un examen) (single word)':'to cram', 
	'a toci (pentru un examen) (idiom)':'to swot up (on)',
	'presupunere':'guesswork','a ezita (idiom)':'to be in two minds about',
	's-o iei de bun':'it begs the question','simplu, modest':'unassuming',
	'ponosit (1)':'shabby','ponosit(2)':'dingy','a calma':'to appease',
	'a imparti (cu zgarcenie)':'to dole out','subred, rahitic':'rickety',
	'a trimite, a expedia':'to consign','tovaras':'crony','propice, favorabil':'conducive',
	'beligerant':'warring','divers, variat, multiplu':'manifold', 'denigrant':'disparagingly'}
	
words2 = {'a avea dubii/indoieli':'to be dubious about','care nu poate fi explicat':'inexplicable',
	'in vederea a...':'with a view to + verb-ing',
	'de neexplicat, paranormal':'unexplainable','ocol':'berth','cocotat':'perched',
	'stil':'panache','a acoperi, a suporta costuri':'to underwrite costs'}
	
words3 = {'a rastalmaci, a interpreta gresit':'to misconstrue','cofetar':'confectioner',
	'a trancani, a sporovai':'to gab','a se indopa':'to gorge','plictiseala':'ennui',
	'plictis':'spleen','sugrumare, strangulare, gatuire, innabusire':'stranglehold',
	'a impodobi':'to adorn','impregnat, cufundat':'steeped','clauza, conditie':'provisio',
	'rezilierea unui contract':'termination','legea in vigoare':'law in force',
	'podoaba, ornament':'adornement'}
	
words4 = {'"urechi de magar" (hartie)':'earmarked','permanent':'indelibly',
	'umplut cu puf':'quilted','pana acum':'hitherto','obsedat':'besotted'}
	
words5 = {'o buna parte din...':'a good many...','in loc de...':'in place of...',
	'schimbator':'changeable','a decora':'to do up','elaborat':'contrived',
	'a cugeta la, a reflecta la (doua prepozitii posibile)':'to muse on/upon',
	'banc de pesti':'shoal','a beneficia de pe urma':'to capitalise on',
	'cuantificabil (care poate fi masurat)':'quantifiable','aparent, pretins':'ostensible',
	'a paste':'to graze','chei (geografic)':'gorge'}
	
words6 = {'coplesit, inundat, bombardat (figurat)':'inundated', 'teritoriu, gazon (context)':'turf',
	'tisa':'yew','obstacol, problema':'snag','ascuns':'furtive','trecator':'transient',
	'tinta (context: frisbee, darts)':'tee'}
	
words7 = {'futil, fara succes':'abortive','de buna credinta (lat.)':'bona fide','enclava (loc ferit)':'enclave',
	'nugget':'chicken kiev','rapid':'briskly','viclean':'shrewd','ocarat':'reviled',
	'camara (de alimente)':'pantry', 'in atat cat sa...':'in as much as', 
	'a avea o mare influenta':'to hold sway','eficient':'lean and mean',
	'a se baza pe':'to be reliant on'}
	
words8 = {'granderur, maiestate':'stateliness','a se eschiva, a evita':'to eschew',
	'evaluare':'appraisal','de necucerit':'unassailable','persoana tanara de succes':'whizz-kid',
	'datorita, cu ajutorul':'by dint of','proeminenta':'dint','a se vinde/cumpara foarte bine':'to snap up',
	'a sacai':'to harry','particular, peculiar':'idiosyncratic','tacanit (to go ____ = to go crazy)':'barmy',
	'a exclude':'to preclude','estetic, senzorial':'sensuos','fluturas de badminton':'shuttlecock',
	'pitulice':'wren','de rau augur':'ominous','ciocarlie':'skylark','nagart (cocstarc mai mic)':'lapwing',
	'casuta de pasari':'birdtables','dreptul copilului mai mare de a mosteni':'primogeniture'}
	
words9 = {'a merge impotriva':'to run counter','a uri':'to abhor','marginire':'philistinism',
	'bonus, recompensa (incentive)':'inducement','tanguitor':'plaintive','maniac':'crank',
	'in principal':'in the main','responsabil / obligatoriu':'incumbent','impertinent (rude)':'impudent',
	'ridicol':'stultified','trestie':'bulrush','preistoric':'antediluvian','moleseala':'lassitude',
	'a paste':'to graze','calcan / talpa':'sole','simplu':'undemonstrative'}
	
words10 = {'actor care joaca acelasi tip de roluri':'typecast','a convinge pe cineva':'to talk somebody round',
	'a nega':'gainsay','norocosule (ironic)':'jammy','autonom':'autonomous','a evalua situatia':'to take stock of the situation'}
	
words11 = {'in consecinta, drept urmare':'accordingly','amagitor':'quackish','editor-si-agent':'editor-cum-agent',
	'pe ascuns':'surreptitiously','explicit':'pointedly','mediu (de viata)':'milieu','marire':'aggrandisement',
	'a falsifica/denatura':'to adulterate','penaj, pana':'plume','coincidenta, sansa':'happenstance',
	'perspectiva / opinie':'slant','capul familiei':'breadwinner','neobosit':'indefatigable','rasfat':'cosseting'}
	
words12 = {'cu riscul':'at the risk','a face aluzii':'driving at','a se bizui pe noroc':'trust to luck',
		'a-i scapa (din minte)':'escape the notice','prietenos':'chummy','propunere / uvertura':'overtures',
		'in linie / actual':'abreast','pe punctul de a izbucni':'afire','pe punctul de a se prabusi':'aground',
		'lasciv, obscen':'prurient','din nou':'afresh','deradere (mockery)':'derision','irascibil (edgy)':'tetchy',
		'discret, modest, sfios, sters':'self-effacing'}
		
words13 = {'in linie, actual':'abreast','lasciv, obscen':'prurient','deradere (mockery)':'derision',
	'irascibil':'tetchy','discret, modest, sfios, sters':'self-effacing','solicitare, cerere, procura':'at the behest of',
	'huiduiala':'hoot','a merge incet':'to traipse','idee vaga':'smattering','sera':'hothouse','novice':'neophyte',
	'apatic, indiferent, nepasator':'stolid'}
	
words14 = {'impresie buna':'immediate impression','cu atat mai mult / ca sa nu mai spunem de...':'not least',
	'suspectat de':'suspected of','a tremura de frica':'shudder with fear','actiune ilegala':'confabulation',
	'iesit din comun, extraordinar':'maverick'}
	
words15 = {'abundent':'profuse','complet, absolut':'stark','a se plimba':'to saunter','a topai, a sari':'to cavort',
	'indirect, prin inlocuire':'vicariously','inchis in tarc, imprejmuit':'corralled','piatra de hotar':'touchstone',
	'alegatori, electorat, centru de vot':'constituency', 'formeaza baza':'forms the basis',
	'buzunar (adica ce castigi)':'pay packet','mieros':'candied','greu de descris (inefabil)':'ineffable'}
	
words16 = {'lupta':'tussle','smoc (ex. de iarba)':'tussock','fir de iarba':'blade of grass','poezie proasta':'doggerel',
	'compasiune':'commiseration','nemultumire, plangere':'grouse'}

# sorry, had to get a quick solution
# oricum ar trebui sa faci un rework la programul asta este cam shite :(
# dar macar merge :)
# #proud
	
def merge_all_dicts(*dict_args):
	finaldict = {}
	for dictionary in dict_args:
		finaldict.update(dictionary)
	return finaldict
	
all = merge_all_dicts(words1, words2, words3, words4, words5, words6, words7, words8, words9,
			words10, words11, words12, words13, words14, words15, words16)

	
def drill(words):
	words_correct = []
	words_wrong = []
	
	print "There are ",len(words)," words you need to input. Start!"
	
	for i in range(0, len(words)):
		word_romana = random.choice(words.keys())
		
		while word_romana in words_correct or word_romana in words_wrong:
			word_romana = random.choice(words.keys())
		print word_romana
		
		word_english = raw_input('>')
		
		if word_english.lower() == words[word_romana]:
			words_correct.append(word_romana)
			print "Correct!",len(words_correct),"/",len(words)," correct!"
		elif word_english == "exit":
			exit(0)
		else:
			words_wrong.append(word_romana)
			if len(words_wrong) == 1:
				print "Incorrect. One mistake so far."
			else:
				print "Incorrect.",len(words_wrong)," mistakes so far."
				
	if len(words)!=len(words_correct):
		print "\nHere are the words you missed:"
		for i in range (0, len(words_wrong)):
			print words_wrong[i],"=",words[words_wrong[i]]
	else:
		print "Good job! You got every word right."
		
	
	print "Press any key to exit, or type again if you would like to try again."
	e = raw_input('>')
	
	if e == 'again': main()
	else: exit(0)
	
def main():
	print "Pick a list from the following:"
	print "1 - words1"
	print "2 - words2"
	print "3 - words3"
	print "4 - words4"
	print "5 - words5"
	print "6 - words6"
	print "7 - words7"
	print "8 - words8"
	print "9 - words9"
	print "10 - words10"
	print "11 - words11"
	print "12 - words12"
	print "13 - words13"
	print "14 - words14"
	print "15 - words15"
	print "16 - words16"
	print "all - ALL WORDS"
	print "deutsch - German words"
	print "debug - debugging"
	print "Type 'exit' to leave at any time."
	var = raw_input('>')

	if var == '1':
		drill(words1)
	elif var == '2':
		drill(words2)
	elif var == '3':
		drill(words3)
	elif var == '4':
		drill(words4)
	elif var == '5':
		drill(words5)
	elif var == '6':
		drill(words6)
	elif var == '7':
		drill(words7)
	elif var == '8':
		drill(words8)
	elif var == '9':
		drill(words9)
	elif var == '10':
		drill(words10)
	elif var == '11':
		drill(words11)
	elif var == '12':
		drill(words12)
	elif var == '13':
		drill(words13)
	elif var == '14':
		drill(words14)
	elif var == '15':
		drill(words15)
	elif var == '16':
		drill(words16)
	elif var == 'all':
		drill(all)
	elif var == 'debug':
		print 'Incerc sa vad daca merge all:\n'
		print all
	elif var == 'deutsch':
		print "WARNING! Umlauts don't work."
		drill(deutsch)
	elif var == 'exit':
		exit(0)
	else:
		print "Not a list! (yet). Try again."
		main()

main()		