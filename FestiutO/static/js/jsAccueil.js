function changerImage(type){
        var maDiv = document.getElementById('divConteneurGroupe');
        var enfants = maDiv.children;

        if(type == -1 ){
            for (var i = 0; i < enfants.length; i++) {
                console.log(enfants.length);
        
                if(enfants[i].classList.contains('imageGroupe1') ){
                    enfants[i].className = ''
                    enfants[i].classList.add("imageGroupe2");
                    enfants[i].classList.add('imageGroupe');
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
                    }
                }
                
            }
        }
        else{
            for (var i = 0; i < enfants.length; i++) {
                console.log("coucouc");
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
