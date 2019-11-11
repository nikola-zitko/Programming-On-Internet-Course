# Programming-On-Internet-Course
College Course
### Task 1
## Client - Server App
Klijent ima iduće funkcionalnosti:
1)	Na portu 40101 osluškuje i dozvoljava spajanje jednog (prethodnog u prstenu) klijenta i primanje poruke.

2)	Nakon primanju poruke (ili unosa poruke na konzoli), klijent se spaja na klijenta i šalje mu poruku.

3)	Pamćenjem zadnje poslane poruke se omogućuje da se zaustavi neprekidno slanje iste poruke.
Klijent će se po potrebi spajati na idućeg klijenta (zadanog IP adresom i portom). Za realizaciju klijenta će biti potreba 1 dodatna niti (uz glavnu nit):
•	Glavna nit pokreće dodatnu nit i nakon toga u petlji čeka i šalje unos korisnika (pročita poruku sa konzole, spoji se na idućeg klijenta i pošalje poruku). Spajanje i slanje se događa u petlji sa čekanjem 5 sekundi između pokušaja dok se ne uspije poslati poruka.

•	Dodatna nit u petlji osluškuje za spajanje klijenta. Kada se klijent spoji, čita se poruka i šalje idućem klijentu (spajanje i slanje je identično kao i kod unosa korisnika s konzole). Nakon toga se zatvara spojeni socket i čeka novo spajanje. 

### Task 2
## Web Crawler
Realizirati aplikaciju za otkrivanje i popisivanje sadržaja povezanih linkovima (pojednostavljeni WebSpider ili WebCrawler). Aplikacija će kretati od zadane adrese, primiti odgovor (u obliku HTTP odgovora sa HTML stranicom) i popisati sve linkove obradom odgovora. Nakon toga za svaki popisani link ponoviti postupak slanja zahtjeva na istu adresu sa različitom putanjom.
Ograničiti broj posjećenih linkova na 50 i sve linkove na kraju treba ispisati na konzoli. Ovisno o implementaciji, svi linkovi se neće uspjeti dohvatiti (provjeriti da li je status odgovora „200 OK“), takve linkove se može ignorirati.
Da bi se izbjeglo kruženje, prije dodavanja linka u listu provjerite da li se link već nalazi u listi. 

### Task 3
## HTML Forme
Pretvoriti HTML stranice u Python skripte tako da se omogući prosljeđivanje unesenih podataka pomoću skrivenih polja. Postaviti ih na XAMPP server u cgi-bin folder. Dodati i zadnju stranicu (Python skriptu) koja će ispisati sve unesene podatke i imati link za povratak na početak wizarda.