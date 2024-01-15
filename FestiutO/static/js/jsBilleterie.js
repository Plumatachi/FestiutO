for (let i = 0; i < listeDate.length; i++){
    var dateObj = new Date(listeDate[i]);
    var jour = dateObj.getDate();
    var mois = dateObj.getMonth() + 1;
    listeMoisJour.push([mois,jour]);
}
var typebillet = 0;

function typeBillet(type) {
    div = document.getElementById("typeBillet");
    div.innerHTML = ""
    typebillet = type;
    pBilletType = document.createElement("p");
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



let date = new Date(listeDate[0]);
let dateEnregistre = new Date();
let verifierpremierchargement = false;



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
    for (let i = 1; i <= lastDay;) {
        // Enquanto o dia da semana for < 7, ele vai adicionar colunas na linha da semana
        while (week < 7) {
            td = document.createElement('td');
            let text = document.createTextNode(i);
            btn = document.createElement('button');
            var estPresent = listeMoisJour.some(function (sousListe) {
                return sousListe[1] === i && sousListe[0] === date.getMonth()+1;
            });
            if(estPresent){
                btn.style = "color : white; background-color : green;"
                btn.className = "btn-day dateJournee";
            }
            else{
                btn.disabled = true;
                btn.className = "btn-day";
            }
            btn.addEventListener('click', function () { changeDate(this) });
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
function changeDate(button) {
    let newDay = parseInt(button.textContent);
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
    dateEnregistre = date;
}
document.onload = generateCalendar();

