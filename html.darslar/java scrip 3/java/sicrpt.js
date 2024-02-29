
let user = +prompt('3 xonali son kiriting')
let bir = Math.floor(user / 100);
 let ikkita = user % 100
let ikki = Math.floor(ikkita / 10);
 let uch = user % 10;
// 213
 if (bir > ikki && ikki > uch ){
     alert(`${bir}${ikki}${uch}`)

 //132    
 }
 else if(bir < ikki && ikki < uch) {
     alert(`${uch}${ikki}${bir}`)
 }
 else if (bir < ikki && ikki > uch)
 alert(`${ikki}${uch}${bir}`)

else if (bir > ikki && ikki < uch){
    alert(`${bir}${uch}${ikki}`)
}

 else{
     alert(false)
 }
 
 


