# Moodul 02: URDF / Xacro — Vastused

## Ülesanne 1: Mudeli analüüs

Ava fail `minu_description/urdf/yahboom_robot.urdf.xacro` ja vasta:

### 1. Mitu link'i on mudelis?

TODO: Mudelis on kokku mitu link’i, sh base_footprint, base_link, rattad, laser_link, camera_link, imu_link ja sonar_link. Kokku on ligikaudu 10–11 link’i, sõltuvalt xacro genereeritud osadest (nt rattad 4 tk eraldi linkidena).

### 2. Mitu joint'i? Mis tüüpi on ratta joint'id ja miks?

TODO: Mudelis on mitu joint’i (ligikaudu 8–10).
Ratta joint’id on continuous tüüpi, sest rattad peavad saama vabalt pöörleda lõpmatus suunas, et robot saaks liikuda.

### 3. Mis vahe on visual ja collision geomeetrial?

TODO: Visual geometry: kasutatakse ainult kuvamiseks RVizis või simulatsioonis (välimus)
Collision geometry: kasutatakse füüsikas (kokkupõrked, simulatsioon, ROS/Gazebo)

### 4. Miks on base_footprint eraldi base_link'ist?

TODO: Aitab lihtsustada navigeerimist
hoida TF puu stabiilsena maapinna suhtes

---

## Ülesanne 2: Visualiseerimine ja TF puu

### 1. Millised lingid on RViz2-s näha?

TODO: RViz2-s on nähtavad kõik robotiga seotud lingid:
base_link, base_footprint, rattad, laser_link, camera_link, imu_link, sonar_link.

### 2. Kuidas mõjutab laser_link asukoht base_link suhtes /scan andmete tõlgendamist?

TODO: Laser_link asukoht määrab, kust punktpilv või /scan andmed pärinevad. Kui laser on nihkes või vales asendis, siis:
objektide kaugused võivad olla valed
kaardistamine (SLAM) muutub ebatäpseks

### 3. Lisa ekraanipilt RViz2-st

TODO: Nägin mudelit robotist, kuhu taha lisasin ühe anduri juurde

### 4. Lisa TF puu (frames.pdf)

TODO: kopeeri frames.pdf siia reposse

---

## Ülesanne 3: URDF ja Webots PROTO võrdlus

### 1. Mis on PROTO faili roll Webots simulatsioonis? Miks ei piisa ainult URDF-ist?

TODO: PROTO defineerib Webotsis roboti täieliku simulatsioonimudeli (füüsika, sensorid, materjalid). URDF ei kirjelda kõiki Webotsi spetsiifilisi simulatsiooni omadusi.

### 2. Mis infot annab URDF Webots-kontekstis?

TODO: URDF annab roboti kinemaatika:

link’id
joint’id
struktuur
TF puu

### 3. Kui tahaksid muuta roboti välimust Webotsis, kas muudaksid URDF-i või PROTO-t? Miks?

TODO: Muudaksin PROTO faili, sest see kontrollib Webotsi visuaalset ja simulatsioonilist välimust. URDF-i kasutatakse ROSi jaoks, mitte Webotsi renderduse muutmiseks.
