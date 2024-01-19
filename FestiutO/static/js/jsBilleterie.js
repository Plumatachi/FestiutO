
var listeMoisJour = [];
for (let i = 0; i < listeDate.length; i++){
    var dateObj = new Date(listeDate[i][0]);
    var jour = dateObj.getDate();
    var mois = dateObj.getMonth() + 1;
    listeMoisJour.push([mois,jour,listeDate[i][1]]);
}
var typebillet = 0;

function typeBillet(type) {
    div = document.getElementById("typeBillet");
    div.innerHTML = ""
    typebillet = type;
    pBilletType = document.createElement("p");
    pBilletType.className = "texteInformationVente";
    if(type == 1){
        pBilletType.textContent = "1 journee "
    }
    else if(type == 2){
        pBilletType.textContent = "2 journee "
    }
    else{
        pBilletType.textContent = "tout les journee "
    }
    div.appendChild(pBilletType);
}


const months = [
    "janvier",
    "fevrier",
    "mars",
    "avril",
    "mai",
    "juin",
    "juillet",
    "aout",
    "semptembre",
    "octobre",
    "novembre",
    "decembre"
];

const weekdays = ["lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "dimanche"];



let date = new Date(listeDate[0][0]);
let dateEnregistre = new Date();
let verifierpremierchargement = false;
let indexJournenregistre = 0;
let nombreJournee = 0;


var valeur = 0;
                        
function updateValue() {
  document.getElementById('valeur').value = valeur;
}

function increment() {
  valeur++;
  updateValue();
}

function decrement() {
  valeur--;
  updateValue();
}

updateValue();

function getCurrentDate(element, asString) {
    if (element) {
        if (asString) {
            return element.textContent = weekdays[date.getDay()] + ', ' + date.getDate() + " de " + months[date.getMonth()] + " de " + date.getFullYear();
        }
        if (!verifierpremierchargement) {
            verifierpremierchargement = true;
        }
        else {
            date.setDate(date.getDate() + 1);
        }
        return element.value = date.toISOString().substr(0, 10);
    }
    return date;
}


// Função principal que gera o calendário
function generateCalendar() {

    // Pega um calendário e se já existir o remove
    const calendar = document.getElementById('calendar');
    if (calendar) {
        calendar.remove();
    }

    // Cria a tabela que será armazenada as datas
    const table = document.createElement("table");
    table.id = "calendar";

    // Cria os headers referentes aos dias da semana
    const trHeader = document.createElement('tr');
    trHeader.className = 'weekends';
    weekdays.map(week => {
        const th = document.createElement('th');
        const w = document.createTextNode(week.substring(0, 3));
        th.appendChild(w);
        trHeader.appendChild(th);
    });

    // Adiciona os headers na tabela
    table.appendChild(trHeader);

    //Pega o dia da semana do primeiro dia do mês
    const weekDay = new Date(
        date.getFullYear(),
        date.getMonth(),
        1
    ).getDay();

    //Pega o ultimo dia do mês
    const lastDay = new Date(
        date.getFullYear(),
        date.getMonth() + 1,
        0
    ).getDate();

    let tr = document.createElement("tr");
    let td = '';
    let empty = '';
    let btn = document.createElement('button');
    let week = 0;

    // Se o dia da semana do primeiro dia do mês for maior que 0(primeiro dia da semana);
    while (week < weekDay) {
        td = document.createElement("td");
        empty = document.createTextNode(' ');
        td.appendChild(empty);
        tr.appendChild(td);
        week++;
    }

    // Vai percorrer do 1º até o ultimo dia do mês
    console.log(listeMoisJour);
    for (let i = 1; i <= lastDay;) {
        // Enquanto o dia da semana for < 7, ele vai adicionar colunas na linha da semana
        while (week < 7) {
            td = document.createElement('td');
            let text = document.createTextNode(i);
            btn = document.createElement('button');
            var indexJournee = listeMoisJour.findIndex(function (sousListe) {
                return sousListe[1] === i && sousListe[0] === date.getMonth()+1;
            });
            if(indexJournee != -1){
                btn.style = "color : white; background-color : green;"
                btn.className = "btn-day dateJournee";
                console.log(listeMoisJour[indexJournee][2])
                btn.setAttribute('onclick', "changeDate('"+i+"','"+listeMoisJour[indexJournee][2]+"')");
            }
            else{
                btn.disabled = true;
                btn.className = "btn-day";
            }
            week++;



            // Controle para ele parar exatamente no ultimo dia
            if (i <= lastDay) {
                i++;
                btn.appendChild(text);
                td.appendChild(btn)
            } else {
                text = document.createTextNode(' ');
                td.appendChild(text);
            }
            tr.appendChild(td);
        }
        // Adiciona a linha na tabela
        table.appendChild(tr);

        // Cria uma nova linha para ser usada
        tr = document.createElement("tr");

        // Reseta o contador de dias da semana
        week = 0;
    }
    // Adiciona a tabela a div que ela deve pertencer
    const content = document.getElementById('table');
    content.appendChild(table);
    changeActive();
    changeHeader(date);
    document.getElementById('date').textContent = date;
    getCurrentDate(document.getElementById("currentDate"), true);
    getCurrentDate(document.getElementById("date"), false);
}

// Altera a data atráves do formulário
function setDate(form) {
    let newDate = new Date(form.date.value);
    date = new Date(newDate.getFullYear(), newDate.getMonth(), newDate.getDate() + 1);
    generateCalendar();
    return false;
}

// Método Muda o mês e o ano do topo do calendário
function changeHeader(dateHeader) {
    const month = document.getElementById("month-header");
    if (month.childNodes[0]) {
        month.removeChild(month.childNodes[0]);
    }
    const headerMonth = document.createElement("h1");
    const textMonth = document.createTextNode(months[dateHeader.getMonth()].substring(0, 3) + " " + dateHeader.getFullYear());
    headerMonth.appendChild(textMonth);
    month.appendChild(headerMonth);
}

// Função para mudar a cor do botão do dia que está ativo
function changeActive() {
    let btnList = document.querySelectorAll('button.active');
    btnList.forEach(btn => {
        btn.classList.remove('active');
    });
    btnList = document.getElementsByClassName('btn-day');
    for (let i = 0; i < btnList.length; i++) {
        const btn = btnList[i];
        if (btn.textContent === (date.getDate()).toString() && btn.classList.contains('dateJournee')) {
            btn.classList.add('active');
        }
    }
}

// Função que pega a data atual
function resetDate() {
    date = new Date();
    generateCalendar();
}

// Muda a data pelo numero do botão clicado
function changeDate(context,id) {
    indexJournenregistre = id;
    let newDay = context;
    date = new Date(date.getFullYear(), date.getMonth(), newDay);
    generateCalendar();
}

// Funções de avançar e retroceder mês e dia
function nextMonth() {
    date = new Date(date.getFullYear(), date.getMonth() + 1, 1);
    generateCalendar();
}

function prevMonth() {
    date = new Date(date.getFullYear(), date.getMonth() - 1, 1);
    generateCalendar();
}


function prevDay() {
    date = new Date(date.getFullYear(), date.getMonth(), date.getDate() - 1);
    generateCalendar();
}

function nextDay() {
    date = new Date(date.getFullYear(), date.getMonth(), date.getDate() + 1);
    generateCalendar();
}


function sauvergarderDate(){
    if(typebillet != 3 && typebillet != 0 && typebillet > nombreJournee){
        nombreJournee++;
        dateEnregistre = document.getElementById("date").value;
        div = document.getElementById("dateEnregistre");
        pDateEnregistre = document.createElement("p");
        pDateEnregistre.className = "texteInformationVente";
        pDateEnregistre.id = indexJournenregistre;
        pDateEnregistre.textContent = document.getElementById("date").value;
        div.appendChild(pDateEnregistre);
    }
}
document.onload = generateCalendar();




var remplaceLienIdJournee = "changerValeurJournee";
var remplaceLienNombre = "nombreJournee";
var remplaceLienType = typeJournee


function acheterBillet(){
    if(document.getElementById("dateEnregistre").innerHTML == "" && typebillet != 3){
        alert("Veuillez choisir une date");
        return;
    }
    else if(document.getElementById("typeBillet").innerHTML == ""){
        alert("Veuillez choisir un type de billet");
        return;
    }
    else if(document.getElementById("valeur").value == 0){
        alert("Veuillez choisir un nombre de billet");
        return;
    }
    else if(typebillet == 1 && nombreJournee != 1){
        alert("Veuillez choisir un 1 de date");
        return;
    }
    else if(typebillet == 2 && nombreJournee != 2){
        alert("Veuillez choisir un 2 de date");
        return;
    }
    else{
        div = document.getElementById("dateEnregistre");
        var enfants = div.childNodes;
        var listeJournee = "'";
        for (var i = 1; i < enfants.length; i++) {
            listeJournee += enfants[i].id+" ";
        }
        listeJournee+="'";
        lien = document.getElementById("lienAcheterBillet");
        var hrefActuel = lien.getAttribute("href");
        console.log(document.getElementById("valeur").value);
        var nouveauHref1 = hrefActuel.replace(remplaceLienIdJournee, listeJournee);
        var nouveauHref1 = nouveauHref1.replace(remplaceLienNombre, document.getElementById("valeur").value);
        var nouveauHref1 = nouveauHref1.replace(remplaceLienType, typebillet);
        remplaceLienIdJournee = "idJournee="+listeJournee;
        remplaceLienIdJournee = "nombre="+document.getElementById("valeur").value;
        remplaceLienIdJournee = "type="+typebillet;
        lien.setAttribute("href", nouveauHref1);
        document.getElementById("lienAcheterBillet").click();


    }
}
