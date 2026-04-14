<?php
$files = ['index.html','catalogo.html','checkout.html','privacidad.html'];
$base = 'https://raw.githubusercontent.com/kreathuragency-prog/importadoramaully-web/master/';
$ok = 0;
foreach($files as $f){
    $c = file_get_contents($base.$f);
    if($c && file_put_contents(__DIR__.'/'.$f, $c)){
        echo "OK: $f (".strlen($c)." bytes)<br>";
        $ok++;
    } else {
        echo "ERROR: $f<br>";
    }
}
echo "<br>$ok/".count($files)." archivos descargados.";
if($ok == count($files)) echo " SITIO RESTAURADO!";
unlink(__FILE__);
?>
