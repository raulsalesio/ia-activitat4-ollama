# Exercici 1: la temperatura

**Objectiu:** veure que amb temperatura 0 el model és previsible (però no per això encerta), que a mesura que puja les respostes es fan més variades i que la temperatura no canvia res quan la pregunta només té una resposta correcta.

**Predicció (abans de començar):** què creieu que passarà amb les respostes quan pugeu la temperatura?

**La vostra predicció:** Segons s'augmenti la temperatura, les respostes seran menys comúns.

## Primera prova: una paraula

1. Inicieu el model i fixeu la temperatura a 0:

   ```
   ollama run gemma3:4b
   >>> /set parameter temperature 0
   ```

2. Escriviu aquest prompt, llegiu la resposta, anoteu-la a la **taula 1** i feu `/clear`. Repetiu-ho fins a tenir **3 respostes** (una a cada columna):

   ```
   Digues una paraula en català de més de 10 lletres. Respon només amb la paraula.
   ```

3. Repetiu el pas 2 amb `/set parameter temperature 0.8` i, després, amb `/set parameter temperature 1.5`. Cada temperatura és una fila de la taula.

**Taula 1: la paraula**

| Temperatura | Resposta 1 | Resposta 2 | Resposta 3 |
| :- | :- | :- | :- |
| 0 |Il·lustració|Estratègia|Estratègia|
| 0.8 |Estratègia|Estratègia|Estratègia|
| 1.5 |Exuberant|Estratègia||

## Segona prova: una pregunta amb una sola resposta

4. Feu el mateix que a la primera prova (3 respostes per temperatura, amb `/clear` entre cadascuna), però només amb les temperatures 0 i 1.5 i amb aquest altre prompt. Comenceu per la temperatura 0: torneu-la a fixar amb `/set parameter temperature 0`, perquè ara la teniu a 1.5. Anoteu les respostes a la **taula 2**, encara que sembli que sempre sortirà el mateix: és justament el que voleu comprovar:

   ```
   Quina és la capital de França? Respon només amb el nom.
   ```

**Taula 2: la capital de França**

| Temperatura | Resposta 1 | Resposta 2 | Resposta 3 |
| :- | :- | :- | :- |
| 0 |París|París|París|
| 1.5 |París|París|París|

## Preguntes

1. Mireu la taula 1. Les tres respostes amb temperatura 0 són iguals? Per què? Compteu les lletres de la paraula: en té més de 10? Que sempre surti la mateixa paraula vol dir que sigui correcta?

   **Resposta:** Gairebé són iguals (Estratègia surt 2 de 3 cops) perquè a temperatura 0 el model tria quasi sempre l'opció més probable. La paraula Estratègia té 10 lletres, això demostra que ser previsible i repetir una resposta no garanteix que el model encerti ni compleixi la instrucció.

2. Què passa quan pugeu la temperatura? Surten paraules diferents? N'hi ha alguna que no tingui més de 10 lletres o que no sembli una paraula real?

   **Resposta:** A temperatura 1.5 surten paraules noves. Totes són reals, però Exuberant només té 9 lletres i Estratègia 10, així que hi ha més varietat però el model falla més a l'hora de complir la condició de longitud.

3. Mireu la taula 2. Les respostes sobre la capital canvien tant com les de la paraula quan puja la temperatura? Per què creieu que la temperatura hi té tan poc efecte? (Pista: quantes respostes correctes té cada pregunta? La temperatura només dona varietat quan el model dubta entre diverses opcions.)

   **Resposta:** No canvien gens, sempre surt París. Com que la pregunta només té una resposta correcta i el model n'està gairebé 100% segur, no dubta entre altres opcions i apujar la temperatura no altera el resultat.

4. Amb les vostres paraules: què fa el paràmetre `temperature`?

   **Resposta:** Controla l'aleatorietat de les respostes. A temperatura baixa el model és conservador i tria l'opció més probable. A temperatura alta s'arrisca amb paraules menys probables.

