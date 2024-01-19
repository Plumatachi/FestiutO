var remplaceLien="changerValeur"

function changerImage(type){
    var maDiv = document.getElementById('divConteneurGroupe');
    var enfants = maDiv.querySelectorAll('a');

    if(type == -1 ){
        for (var i = 0; i < enfants.length; i++) {
            if(enfants[i].classList.contains('imageGroupe1') ){
                enfants[i].className = ''
                enfants[i].classList.add("imageGroupe2");
                enfants[i].classList.add('imageGroupe');
                changeIdInfoJournee(enfants[i].id.match(/\d+/)[0]);
                document.getElementById("titreGroupeMusique").innerText = enfants[i].title
            }
            else if(enfants[i].classList.contains('imageGroupe2') ){
                enfants[i].className = ''
                enfants[i].classList.add("imageGroupe3");
                enfants[i].classList.add('imageGroupe');
            }
            else if(enfants[i].classList.contains('imageGroupe3')){
                enfants[i].className = ''
                enfants[i].classList.add("imageCacher");
                enfants[i].classList.add('imageGroupe');
            }
            else if(i != enfants.length-1){
                if(enfants[i+1].classList.contains('imageGroupe1')){
                    enfants[i].className = ''
                    enfants[i].classList.add("imageGroupe1");
                    enfants[i].classList.add('imageGroupe');
                }
            }
            else{
                if(enfants[0].classList.contains('imageGroupe1')){
                    console.log("12")
                    enfants[i].className = ''
                    enfants[i].classList.add("imageCacher");
                    enfants[i].classList.add('imageGroupe');
                }
                if(enfants[0].classList.contains('imageGroupe2')){
                    console.log("13")
                    enfants[i].className = ''
                    enfants[i].classList.add("imageGroupe1");
                    enfants[i].classList.add('imageGroupe');
                }
                if(enfants[0].classList.contains('imageGroupe3')){
                    console.log("14")
                    enfants[i].className = ''
                    enfants[i].classList.add("imageGroupe2");
                    enfants[i].classList.add('imageGroupe');
                    document.getElementById("titreGroupeMusique").innerText = enfants[i].title
                    changeIdInfoJournee(enfants[i].id.match(/\d+/)[0]);
                }
            }
            
        }
    }
    else{
        for (var i = 0; i < enfants.length; i++) {
            if(enfants[i].classList.contains('imageGroupe1') ){
                enfants[i].className = ''
                enfants[i].classList.add("imageCacher");
                enfants[i].classList.add('imageGroupe');
            }
            else if(enfants[i].classList.contains('imageGroupe2')){
                enfants[i].className = ''
                enfants[i].classList.add("imageGroupe1");
                enfants[i].classList.add('imageGroupe');
            }
            else if(enfants[i].classList.contains('imageGroupe3')){
                enfants[i].className = ''
                enfants[i].classList.add("imageGroupe2");
                enfants[i].classList.add('imageGroupe');
                document.getElementById("titreGroupeMusique").innerText = enfants[i].title
                changeIdInfoJournee(enfants[i].id.match(/\d+/)[0]);
            }
            else if(i != 0){
                if(enfants[i-1].classList.contains('imageGroupe2')){
                    enfants[i].className = ''
                    enfants[i].classList.add("imageGroupe3");
                    enfants[i].classList.add('imageGroupe');
                }
            }
            else{
                if(enfants[enfants.length-1].classList.contains('imageGroupe1')){
                    console.log("12")
                    enfants[i].className = ''
                    enfants[i].classList.add("imageGroupe2");
                    enfants[i].classList.add('imageGroupe');
                    document.getElementById("titreGroupeMusique").innerText = enfants[i].title
                    changeIdInfoJournee(enfants[i].id.match(/\d+/)[0]);
                }
                if(enfants[enfants.length-1].classList.contains('imageGroupe2')){
                    console.log("13")
                    enfants[i].className = ''
                    enfants[i].classList.add("imageCacher");
                    enfants[i].classList.add('imageGroupe');
                }
                if(enfants[enfants.length-1].classList.contains('imageGroupe3')){
                    console.log("14")
                    enfants[i].className = ''
                    enfants[i].classList.add("imageGroupe3");
                    enfants[i].classList.add('imageGroupe');
                }
            }
            
        } 
    }
}

function changeIdInfoJournee(idgroupe){
    $.ajax({
        url: '/get_Info_journee_Groupe',
        type: 'GET',
        data:{
            'idgroupe' : idgroupe
        },
        success: function (data) {
            console.log(data)
            var maDiv = document.getElementById('divCaseEvenements');
            maDiv.innerHTML = '';
            console.log(data)
            for (var i = 0; i < data.length; i++){
                var dateObj = new Date(data[i][0]);
                var jour = dateObj.getDate();
                var mois = dateObj.getMonth() + 1;
                var jourMoisFormat = jour + '/' + mois;
                if(document.getElementById(jourMoisFormat) == null){
                    
                    divDate = document.createElement("div");
                    divDate.id = jourMoisFormat;
                    divDate.classList.add('divContientTexteDateEvenement');

                    divEvement = document.createElement("div");
                    divEvement.classList.add('divPetBoutonProgramme');
                    h2Evenement = document.createElement("h2");
                    h2Evenement.textContent = jourMoisFormat;
                    h2Evenement.classList.add('h2Evenement');

                    
                    
                    PEvenement = document.createElement("p");
                    PEvenement.classList.add('texteEvenement');
                    PEvenement.textContent = data[i][2] + " : " +new Date(data[i][0]).toTimeString().split(' ')[0].slice(0, -3) + ": a "+data[i][3];
                    
                    buttonEvenement = document.createElement("button");
                    buttonEvenement.textContent = "S'inscrire";
                    buttonEvenement.setAttribute('onclick', "inscrireEvenement('" + data[i][4] + "')");
                    buttonEvenement.classList.add('buttonInscription');
                    
                    divDate.appendChild(h2Evenement);
                    divEvement.appendChild(PEvenement);
                    divEvement.appendChild(buttonEvenement);
                    if(data[i][5] != null){
                        divConcert= document.createElement("div");
                        divConcert.id  = "concert";


                        h3Consert = document.createElement("h3");
                        h3Consert.textContent = "Consert";
                        h3Consert.classList.add('h2Evenement');

                        divConcert.appendChild(h3Consert);
                        divConcert.appendChild(divEvement);
                        divDate.appendChild(divConcert);
                    }
                    else{
                        divActivite= document.createElement("div");
                        divActivite.id  = "activiter";


                        h3Acitivite = document.createElement("h3");
                        h3Acitivite.textContent = "Activite";
                        h3Acitivite.classList.add('h2Evenement');

                        divActivite.appendChild(h3Acitivite);
                        divActivite.appendChild(divEvement);
                        divDate.appendChild(divActivite);
                    }
                    
                    
                    document.getElementById("divCaseEvenements").appendChild(divDate);


                }
                else{
                    
                    divEvement = document.createElement("div");
                    divEvement.classList.add('divPetBoutonProgramme');
                    PEvenement = document.createElement("p");
                    PEvenement.classList.add('texteEvenement');
                    PEvenement.textContent = data[i][2] + " : " +new Date(data[i][0]).toTimeString().split(' ')[0].slice(0, -3) + ": a "+data[i][3];

                    buttonEvenement = document.createElement("button");
                    buttonEvenement.textContent = "S'inscrire";
                    buttonEvenement.classList.add('buttonInscription');
                    buttonEvenement.setAttribute("onclick","inscrireEvenement('"+data[i][4]+"')");
                    
                    divEvement.appendChild(PEvenement);
                    divEvement.appendChild(buttonEvenement);
                    divEvement.appendChild(aInscrire);
                    divDate = document.getElementById(jourMoisFormat)
                    if(data[i][5] != null){
                        var divEnfant = divDate.querySelector('#' + "concert");
                        if(conteneurParent && divEnfant && conteneurParent.contains(divEnfant)){
                            divEnfant.appendChild(divEvement);
                        }
                        else{
                            divConcert= document.createElement("div");
                            divConcert.id  = "concert";
                            divConcert.appendChild(divEvement);
                        }
                    }
                    else{
                        var divEnfant = divDate.querySelector('#' + "activiter");
                        if(conteneurParent && divEnfant && conteneurParent.contains(divEnfant)){
                            divEnfant.appendChild(divEvement);
                        }
                        else{
                            divActivite = document.createElement("div");
                            divActivite.id  = "activiter";
                            divActivite.appendChild(divEvement);
    
                        }
                    }
                    
                    
                    
                }
            }
            var maDiv = document.getElementById('divCaseEvenements');
            if(maDiv.innerHTML == ''){
                divDate = document.createElement("div");
                divDate.classList.add('divContientTexteDateEvenement');

                h2Evenement = document.createElement("h2");
                h2Evenement.textContent = "Arrive Bientot";
                h2Evenement.classList.add('h2Evenement');
                divDate.appendChild(h2Evenement);
                maDiv?.appendChild(divDate);
            }
        }
    });

}




    function inscrireEvenement(id){
        console.log(id)
        lien = document.getElementById("lienAcheterBillet");
        var hrefActuel = lien.getAttribute("href");
        var nouveauHref1 = hrefActuel.replace(remplaceLien, id);
        console.log(nouveauHref1);
        remplaceLien = id;
        lien.setAttribute("href", nouveauHref1);
        document.getElementById("lienAcheterBillet").click();

    }