# pylint:disable=missing-module-docstring,missing-class-docstring,missing-function-docstring
from .base import compare_template, SimpleTestCase

class TimePickerTest(SimpleTestCase):
    maxDiff = None

    def test_rendered(self):
        template = """
{% load carbondesign %}
{% TimePicker form.started_at %}
"""
        expected = r"""
<div class="bx--form-item">
<label for="id_started_at" class="bx--label">
  Started at
</label>
  <div class="bx--time-picker">
    <div class="bx--time-picker__input"><input type="text" name="started_at" value="2022-02-03 01:02:03" class="bx--text-input bx--time-picker__input-field" pattern="(1[012]|[1-9]):[0-5][0-9](\\s)?" placeholder="hh:mm" maxlength="5" required id="id_started_at"></div>
<div class="bx--time-picker__select bx--select">
  <label for="select-ampm-id_started_at" class="bx--label bx--visually-hidden">
    Select AM/PM
  </label>
  <select id="select-ampm-id_started_at" class="bx--select-input">
    <option class="bx--select-option" value="AM">AM</option>
    <option class="bx--select-option" value="PM">PM</option>
  </select>
  <svg focusable="false" preserveAspectRatio="xMidYMid meet"
      xmlns="http://www.w3.org/2000/svg" fill="currentColor"
      class="bx--select__arrow" width="16" height="16" viewBox="0 0 16 16"
      aria-hidden="true">
    <path d="M8 11L3 6 3.7 5.3 8 9.6 12.3 5.3 13 6z"></path>
  </svg>
</div>
<div class="bx--time-picker__select bx--select">
  <label for="select-zone-id_started_at" class="bx--label bx--visually-hidden">
    Select time zone
  </label>
  <select id="select-zone-id_started_at" class="bx--select-input">
<option class="bx--select-option" value="Africa/Abidjan">Africa/Abidjan</option>
<option class="bx--select-option" value="Africa/Accra">Africa/Accra</option>
<option class="bx--select-option" value="Africa/Addis_Ababa">Africa/Addis_Ababa</option>
<option class="bx--select-option" value="Africa/Algiers">Africa/Algiers</option>
<option class="bx--select-option" value="Africa/Asmara">Africa/Asmara</option>
<option class="bx--select-option" value="Africa/Bamako">Africa/Bamako</option>
<option class="bx--select-option" value="Africa/Bangui">Africa/Bangui</option>
<option class="bx--select-option" value="Africa/Banjul">Africa/Banjul</option>
<option class="bx--select-option" value="Africa/Bissau">Africa/Bissau</option>
<option class="bx--select-option" value="Africa/Blantyre">Africa/Blantyre</option>
<option class="bx--select-option" value="Africa/Brazzaville">Africa/Brazzaville</option>
<option class="bx--select-option" value="Africa/Bujumbura">Africa/Bujumbura</option>
<option class="bx--select-option" value="Africa/Cairo">Africa/Cairo</option>
<option class="bx--select-option" value="Africa/Casablanca">Africa/Casablanca</option>
<option class="bx--select-option" value="Africa/Ceuta">Africa/Ceuta</option>
<option class="bx--select-option" value="Africa/Conakry">Africa/Conakry</option>
<option class="bx--select-option" value="Africa/Dakar">Africa/Dakar</option>
<option class="bx--select-option" value="Africa/Dar_es_Salaam">Africa/Dar_es_Salaam</option>
<option class="bx--select-option" value="Africa/Djibouti">Africa/Djibouti</option>
<option class="bx--select-option" value="Africa/Douala">Africa/Douala</option>
<option class="bx--select-option" value="Africa/El_Aaiun">Africa/El_Aaiun</option>
<option class="bx--select-option" value="Africa/Freetown">Africa/Freetown</option>
<option class="bx--select-option" value="Africa/Gaborone">Africa/Gaborone</option>
<option class="bx--select-option" value="Africa/Harare">Africa/Harare</option>
<option class="bx--select-option" value="Africa/Johannesburg">Africa/Johannesburg</option>
<option class="bx--select-option" value="Africa/Juba">Africa/Juba</option>
<option class="bx--select-option" value="Africa/Kampala">Africa/Kampala</option>
<option class="bx--select-option" value="Africa/Khartoum">Africa/Khartoum</option>
<option class="bx--select-option" value="Africa/Kigali">Africa/Kigali</option>
<option class="bx--select-option" value="Africa/Kinshasa">Africa/Kinshasa</option>
<option class="bx--select-option" value="Africa/Lagos">Africa/Lagos</option>
<option class="bx--select-option" value="Africa/Libreville">Africa/Libreville</option>
<option class="bx--select-option" value="Africa/Lome">Africa/Lome</option>
<option class="bx--select-option" value="Africa/Luanda">Africa/Luanda</option>
<option class="bx--select-option" value="Africa/Lubumbashi">Africa/Lubumbashi</option>
<option class="bx--select-option" value="Africa/Lusaka">Africa/Lusaka</option>
<option class="bx--select-option" value="Africa/Malabo">Africa/Malabo</option>
<option class="bx--select-option" value="Africa/Maputo">Africa/Maputo</option>
<option class="bx--select-option" value="Africa/Maseru">Africa/Maseru</option>
<option class="bx--select-option" value="Africa/Mbabane">Africa/Mbabane</option>
<option class="bx--select-option" value="Africa/Mogadishu">Africa/Mogadishu</option>
<option class="bx--select-option" value="Africa/Monrovia">Africa/Monrovia</option>
<option class="bx--select-option" value="Africa/Nairobi">Africa/Nairobi</option>
<option class="bx--select-option" value="Africa/Ndjamena">Africa/Ndjamena</option>
<option class="bx--select-option" value="Africa/Niamey">Africa/Niamey</option>
<option class="bx--select-option" value="Africa/Nouakchott">Africa/Nouakchott</option>
<option class="bx--select-option" value="Africa/Ouagadougou">Africa/Ouagadougou</option>
<option class="bx--select-option" value="Africa/Porto-Novo">Africa/Porto-Novo</option>
<option class="bx--select-option" value="Africa/Sao_Tome">Africa/Sao_Tome</option>
<option class="bx--select-option" value="Africa/Tripoli">Africa/Tripoli</option>
<option class="bx--select-option" value="Africa/Tunis">Africa/Tunis</option>
<option class="bx--select-option" value="Africa/Windhoek">Africa/Windhoek</option>
<option class="bx--select-option" value="America/Adak">America/Adak</option>
<option class="bx--select-option" value="America/Anchorage">America/Anchorage</option>
<option class="bx--select-option" value="America/Anguilla">America/Anguilla</option>
<option class="bx--select-option" value="America/Antigua">America/Antigua</option>
<option class="bx--select-option" value="America/Araguaina">America/Araguaina</option>
<option class="bx--select-option" value="America/Argentina/Buenos_Aires">America/Argentina/Buenos_Aires</option>
<option class="bx--select-option" value="America/Argentina/Catamarca">America/Argentina/Catamarca</option>
<option class="bx--select-option" value="America/Argentina/Cordoba">America/Argentina/Cordoba</option>
<option class="bx--select-option" value="America/Argentina/Jujuy">America/Argentina/Jujuy</option>
<option class="bx--select-option" value="America/Argentina/La_Rioja">America/Argentina/La_Rioja</option>
<option class="bx--select-option" value="America/Argentina/Mendoza">America/Argentina/Mendoza</option>
<option class="bx--select-option" value="America/Argentina/Rio_Gallegos">America/Argentina/Rio_Gallegos</option>
<option class="bx--select-option" value="America/Argentina/Salta">America/Argentina/Salta</option>
<option class="bx--select-option" value="America/Argentina/San_Juan">America/Argentina/San_Juan</option>
<option class="bx--select-option" value="America/Argentina/San_Luis">America/Argentina/San_Luis</option>
<option class="bx--select-option" value="America/Argentina/Tucuman">America/Argentina/Tucuman</option>
<option class="bx--select-option" value="America/Argentina/Ushuaia">America/Argentina/Ushuaia</option>
<option class="bx--select-option" value="America/Aruba">America/Aruba</option>
<option class="bx--select-option" value="America/Asuncion">America/Asuncion</option>
<option class="bx--select-option" value="America/Atikokan">America/Atikokan</option>
<option class="bx--select-option" value="America/Bahia">America/Bahia</option>
<option class="bx--select-option" value="America/Bahia_Banderas">America/Bahia_Banderas</option>
<option class="bx--select-option" value="America/Barbados">America/Barbados</option>
<option class="bx--select-option" value="America/Belem">America/Belem</option>
<option class="bx--select-option" value="America/Belize">America/Belize</option>
<option class="bx--select-option" value="America/Blanc-Sablon">America/Blanc-Sablon</option>
<option class="bx--select-option" value="America/Boa_Vista">America/Boa_Vista</option>
<option class="bx--select-option" value="America/Bogota">America/Bogota</option>
<option class="bx--select-option" value="America/Boise">America/Boise</option>
<option class="bx--select-option" value="America/Cambridge_Bay">America/Cambridge_Bay</option>
<option class="bx--select-option" value="America/Campo_Grande">America/Campo_Grande</option>
<option class="bx--select-option" value="America/Cancun">America/Cancun</option>
<option class="bx--select-option" value="America/Caracas">America/Caracas</option>
<option class="bx--select-option" value="America/Cayenne">America/Cayenne</option>
<option class="bx--select-option" value="America/Cayman">America/Cayman</option>
<option class="bx--select-option" value="America/Chicago">America/Chicago</option>
<option class="bx--select-option" value="America/Chihuahua">America/Chihuahua</option>
<option class="bx--select-option" value="America/Costa_Rica">America/Costa_Rica</option>
<option class="bx--select-option" value="America/Creston">America/Creston</option>
<option class="bx--select-option" value="America/Cuiaba">America/Cuiaba</option>
<option class="bx--select-option" value="America/Curacao">America/Curacao</option>
<option class="bx--select-option" value="America/Danmarkshavn">America/Danmarkshavn</option>
<option class="bx--select-option" value="America/Dawson">America/Dawson</option>
<option class="bx--select-option" value="America/Dawson_Creek">America/Dawson_Creek</option>
<option class="bx--select-option" value="America/Denver">America/Denver</option>
<option class="bx--select-option" value="America/Detroit">America/Detroit</option>
<option class="bx--select-option" value="America/Dominica">America/Dominica</option>
<option class="bx--select-option" value="America/Edmonton">America/Edmonton</option>
<option class="bx--select-option" value="America/Eirunepe">America/Eirunepe</option>
<option class="bx--select-option" value="America/El_Salvador">America/El_Salvador</option>
<option class="bx--select-option" value="America/Fort_Nelson">America/Fort_Nelson</option>
<option class="bx--select-option" value="America/Fortaleza">America/Fortaleza</option>
<option class="bx--select-option" value="America/Glace_Bay">America/Glace_Bay</option>
<option class="bx--select-option" value="America/Goose_Bay">America/Goose_Bay</option>
<option class="bx--select-option" value="America/Grand_Turk">America/Grand_Turk</option>
<option class="bx--select-option" value="America/Grenada">America/Grenada</option>
<option class="bx--select-option" value="America/Guadeloupe">America/Guadeloupe</option>
<option class="bx--select-option" value="America/Guatemala">America/Guatemala</option>
<option class="bx--select-option" value="America/Guayaquil">America/Guayaquil</option>
<option class="bx--select-option" value="America/Guyana">America/Guyana</option>
<option class="bx--select-option" value="America/Halifax">America/Halifax</option>
<option class="bx--select-option" value="America/Havana">America/Havana</option>
<option class="bx--select-option" value="America/Hermosillo">America/Hermosillo</option>
<option class="bx--select-option" value="America/Indiana/Indianapolis">America/Indiana/Indianapolis</option>
<option class="bx--select-option" value="America/Indiana/Knox">America/Indiana/Knox</option>
<option class="bx--select-option" value="America/Indiana/Marengo">America/Indiana/Marengo</option>
<option class="bx--select-option" value="America/Indiana/Petersburg">America/Indiana/Petersburg</option>
<option class="bx--select-option" value="America/Indiana/Tell_City">America/Indiana/Tell_City</option>
<option class="bx--select-option" value="America/Indiana/Vevay">America/Indiana/Vevay</option>
<option class="bx--select-option" value="America/Indiana/Vincennes">America/Indiana/Vincennes</option>
<option class="bx--select-option" value="America/Indiana/Winamac">America/Indiana/Winamac</option>
<option class="bx--select-option" value="America/Inuvik">America/Inuvik</option>
<option class="bx--select-option" value="America/Iqaluit">America/Iqaluit</option>
<option class="bx--select-option" value="America/Jamaica">America/Jamaica</option>
<option class="bx--select-option" value="America/Juneau">America/Juneau</option>
<option class="bx--select-option" value="America/Kentucky/Louisville">America/Kentucky/Louisville</option>
<option class="bx--select-option" value="America/Kentucky/Monticello">America/Kentucky/Monticello</option>
<option class="bx--select-option" value="America/Kralendijk">America/Kralendijk</option>
<option class="bx--select-option" value="America/La_Paz">America/La_Paz</option>
<option class="bx--select-option" value="America/Lima">America/Lima</option>
<option class="bx--select-option" value="America/Los_Angeles">America/Los_Angeles</option>
<option class="bx--select-option" value="America/Lower_Princes">America/Lower_Princes</option>
<option class="bx--select-option" value="America/Maceio">America/Maceio</option>
<option class="bx--select-option" value="America/Managua">America/Managua</option>
<option class="bx--select-option" value="America/Manaus">America/Manaus</option>
<option class="bx--select-option" value="America/Marigot">America/Marigot</option>
<option class="bx--select-option" value="America/Martinique">America/Martinique</option>
<option class="bx--select-option" value="America/Matamoros">America/Matamoros</option>
<option class="bx--select-option" value="America/Mazatlan">America/Mazatlan</option>
<option class="bx--select-option" value="America/Menominee">America/Menominee</option>
<option class="bx--select-option" value="America/Merida">America/Merida</option>
<option class="bx--select-option" value="America/Metlakatla">America/Metlakatla</option>
<option class="bx--select-option" value="America/Mexico_City">America/Mexico_City</option>
<option class="bx--select-option" value="America/Miquelon">America/Miquelon</option>
<option class="bx--select-option" value="America/Moncton">America/Moncton</option>
<option class="bx--select-option" value="America/Monterrey">America/Monterrey</option>
<option class="bx--select-option" value="America/Montevideo">America/Montevideo</option>
<option class="bx--select-option" value="America/Montserrat">America/Montserrat</option>
<option class="bx--select-option" value="America/Nassau">America/Nassau</option>
<option class="bx--select-option" value="America/New_York">America/New_York</option>
<option class="bx--select-option" value="America/Nipigon">America/Nipigon</option>
<option class="bx--select-option" value="America/Nome">America/Nome</option>
<option class="bx--select-option" value="America/Noronha">America/Noronha</option>
<option class="bx--select-option" value="America/North_Dakota/Beulah">America/North_Dakota/Beulah</option>
<option class="bx--select-option" value="America/North_Dakota/Center">America/North_Dakota/Center</option>
<option class="bx--select-option" value="America/North_Dakota/New_Salem">America/North_Dakota/New_Salem</option>
<option class="bx--select-option" value="America/Nuuk">America/Nuuk</option>
<option class="bx--select-option" value="America/Ojinaga">America/Ojinaga</option>
<option class="bx--select-option" value="America/Panama">America/Panama</option>
<option class="bx--select-option" value="America/Pangnirtung">America/Pangnirtung</option>
<option class="bx--select-option" value="America/Paramaribo">America/Paramaribo</option>
<option class="bx--select-option" value="America/Phoenix">America/Phoenix</option>
<option class="bx--select-option" value="America/Port-au-Prince">America/Port-au-Prince</option>
<option class="bx--select-option" value="America/Port_of_Spain">America/Port_of_Spain</option>
<option class="bx--select-option" value="America/Porto_Velho">America/Porto_Velho</option>
<option class="bx--select-option" value="America/Puerto_Rico">America/Puerto_Rico</option>
<option class="bx--select-option" value="America/Punta_Arenas">America/Punta_Arenas</option>
<option class="bx--select-option" value="America/Rainy_River">America/Rainy_River</option>
<option class="bx--select-option" value="America/Rankin_Inlet">America/Rankin_Inlet</option>
<option class="bx--select-option" value="America/Recife">America/Recife</option>
<option class="bx--select-option" value="America/Regina">America/Regina</option>
<option class="bx--select-option" value="America/Resolute">America/Resolute</option>
<option class="bx--select-option" value="America/Rio_Branco">America/Rio_Branco</option>
<option class="bx--select-option" value="America/Santarem">America/Santarem</option>
<option class="bx--select-option" value="America/Santiago">America/Santiago</option>
<option class="bx--select-option" value="America/Santo_Domingo">America/Santo_Domingo</option>
<option class="bx--select-option" value="America/Sao_Paulo">America/Sao_Paulo</option>
<option class="bx--select-option" value="America/Scoresbysund">America/Scoresbysund</option>
<option class="bx--select-option" value="America/Sitka">America/Sitka</option>
<option class="bx--select-option" value="America/St_Barthelemy">America/St_Barthelemy</option>
<option class="bx--select-option" value="America/St_Johns">America/St_Johns</option>
<option class="bx--select-option" value="America/St_Kitts">America/St_Kitts</option>
<option class="bx--select-option" value="America/St_Lucia">America/St_Lucia</option>
<option class="bx--select-option" value="America/St_Thomas">America/St_Thomas</option>
<option class="bx--select-option" value="America/St_Vincent">America/St_Vincent</option>
<option class="bx--select-option" value="America/Swift_Current">America/Swift_Current</option>
<option class="bx--select-option" value="America/Tegucigalpa">America/Tegucigalpa</option>
<option class="bx--select-option" value="America/Thule">America/Thule</option>
<option class="bx--select-option" value="America/Thunder_Bay">America/Thunder_Bay</option>
<option class="bx--select-option" value="America/Tijuana">America/Tijuana</option>
<option class="bx--select-option" value="America/Toronto">America/Toronto</option>
<option class="bx--select-option" value="America/Tortola">America/Tortola</option>
<option class="bx--select-option" value="America/Vancouver">America/Vancouver</option>
<option class="bx--select-option" value="America/Whitehorse">America/Whitehorse</option>
<option class="bx--select-option" value="America/Winnipeg">America/Winnipeg</option>
<option class="bx--select-option" value="America/Yakutat">America/Yakutat</option>
<option class="bx--select-option" value="America/Yellowknife">America/Yellowknife</option>
<option class="bx--select-option" value="Antarctica/Casey">Antarctica/Casey</option>
<option class="bx--select-option" value="Antarctica/Davis">Antarctica/Davis</option>
<option class="bx--select-option" value="Antarctica/DumontDUrville">Antarctica/DumontDUrville</option>
<option class="bx--select-option" value="Antarctica/Macquarie">Antarctica/Macquarie</option>
<option class="bx--select-option" value="Antarctica/Mawson">Antarctica/Mawson</option>
<option class="bx--select-option" value="Antarctica/McMurdo">Antarctica/McMurdo</option>
<option class="bx--select-option" value="Antarctica/Palmer">Antarctica/Palmer</option>
<option class="bx--select-option" value="Antarctica/Rothera">Antarctica/Rothera</option>
<option class="bx--select-option" value="Antarctica/Syowa">Antarctica/Syowa</option>
<option class="bx--select-option" value="Antarctica/Troll">Antarctica/Troll</option>
<option class="bx--select-option" value="Antarctica/Vostok">Antarctica/Vostok</option>
<option class="bx--select-option" value="Arctic/Longyearbyen">Arctic/Longyearbyen</option>
<option class="bx--select-option" value="Asia/Aden">Asia/Aden</option>
<option class="bx--select-option" value="Asia/Almaty">Asia/Almaty</option>
<option class="bx--select-option" value="Asia/Amman">Asia/Amman</option>
<option class="bx--select-option" value="Asia/Anadyr">Asia/Anadyr</option>
<option class="bx--select-option" value="Asia/Aqtau">Asia/Aqtau</option>
<option class="bx--select-option" value="Asia/Aqtobe">Asia/Aqtobe</option>
<option class="bx--select-option" value="Asia/Ashgabat">Asia/Ashgabat</option>
<option class="bx--select-option" value="Asia/Atyrau">Asia/Atyrau</option>
<option class="bx--select-option" value="Asia/Baghdad">Asia/Baghdad</option>
<option class="bx--select-option" value="Asia/Bahrain">Asia/Bahrain</option>
<option class="bx--select-option" value="Asia/Baku">Asia/Baku</option>
<option class="bx--select-option" value="Asia/Bangkok">Asia/Bangkok</option>
<option class="bx--select-option" value="Asia/Barnaul">Asia/Barnaul</option>
<option class="bx--select-option" value="Asia/Beirut">Asia/Beirut</option>
<option class="bx--select-option" value="Asia/Bishkek">Asia/Bishkek</option>
<option class="bx--select-option" value="Asia/Brunei">Asia/Brunei</option>
<option class="bx--select-option" value="Asia/Chita">Asia/Chita</option>
<option class="bx--select-option" value="Asia/Choibalsan">Asia/Choibalsan</option>
<option class="bx--select-option" value="Asia/Colombo">Asia/Colombo</option>
<option class="bx--select-option" value="Asia/Damascus">Asia/Damascus</option>
<option class="bx--select-option" value="Asia/Dhaka">Asia/Dhaka</option>
<option class="bx--select-option" value="Asia/Dili">Asia/Dili</option>
<option class="bx--select-option" value="Asia/Dubai">Asia/Dubai</option>
<option class="bx--select-option" value="Asia/Dushanbe">Asia/Dushanbe</option>
<option class="bx--select-option" value="Asia/Famagusta">Asia/Famagusta</option>
<option class="bx--select-option" value="Asia/Gaza">Asia/Gaza</option>
<option class="bx--select-option" value="Asia/Hebron">Asia/Hebron</option>
<option class="bx--select-option" value="Asia/Ho_Chi_Minh">Asia/Ho_Chi_Minh</option>
<option class="bx--select-option" value="Asia/Hong_Kong">Asia/Hong_Kong</option>
<option class="bx--select-option" value="Asia/Hovd">Asia/Hovd</option>
<option class="bx--select-option" value="Asia/Irkutsk">Asia/Irkutsk</option>
<option class="bx--select-option" value="Asia/Jakarta">Asia/Jakarta</option>
<option class="bx--select-option" value="Asia/Jayapura">Asia/Jayapura</option>
<option class="bx--select-option" value="Asia/Jerusalem">Asia/Jerusalem</option>
<option class="bx--select-option" value="Asia/Kabul">Asia/Kabul</option>
<option class="bx--select-option" value="Asia/Kamchatka">Asia/Kamchatka</option>
<option class="bx--select-option" value="Asia/Karachi">Asia/Karachi</option>
<option class="bx--select-option" value="Asia/Kathmandu">Asia/Kathmandu</option>
<option class="bx--select-option" value="Asia/Khandyga">Asia/Khandyga</option>
<option class="bx--select-option" value="Asia/Kolkata">Asia/Kolkata</option>
<option class="bx--select-option" value="Asia/Krasnoyarsk">Asia/Krasnoyarsk</option>
<option class="bx--select-option" value="Asia/Kuala_Lumpur">Asia/Kuala_Lumpur</option>
<option class="bx--select-option" value="Asia/Kuching">Asia/Kuching</option>
<option class="bx--select-option" value="Asia/Kuwait">Asia/Kuwait</option>
<option class="bx--select-option" value="Asia/Macau">Asia/Macau</option>
<option class="bx--select-option" value="Asia/Magadan">Asia/Magadan</option>
<option class="bx--select-option" value="Asia/Makassar">Asia/Makassar</option>
<option class="bx--select-option" value="Asia/Manila">Asia/Manila</option>
<option class="bx--select-option" value="Asia/Muscat">Asia/Muscat</option>
<option class="bx--select-option" value="Asia/Nicosia">Asia/Nicosia</option>
<option class="bx--select-option" value="Asia/Novokuznetsk">Asia/Novokuznetsk</option>
<option class="bx--select-option" value="Asia/Novosibirsk">Asia/Novosibirsk</option>
<option class="bx--select-option" value="Asia/Omsk">Asia/Omsk</option>
<option class="bx--select-option" value="Asia/Oral">Asia/Oral</option>
<option class="bx--select-option" value="Asia/Phnom_Penh">Asia/Phnom_Penh</option>
<option class="bx--select-option" value="Asia/Pontianak">Asia/Pontianak</option>
<option class="bx--select-option" value="Asia/Pyongyang">Asia/Pyongyang</option>
<option class="bx--select-option" value="Asia/Qatar">Asia/Qatar</option>
<option class="bx--select-option" value="Asia/Qostanay">Asia/Qostanay</option>
<option class="bx--select-option" value="Asia/Qyzylorda">Asia/Qyzylorda</option>
<option class="bx--select-option" value="Asia/Riyadh">Asia/Riyadh</option>
<option class="bx--select-option" value="Asia/Sakhalin">Asia/Sakhalin</option>
<option class="bx--select-option" value="Asia/Samarkand">Asia/Samarkand</option>
<option class="bx--select-option" value="Asia/Seoul">Asia/Seoul</option>
<option class="bx--select-option" value="Asia/Shanghai">Asia/Shanghai</option>
<option class="bx--select-option" value="Asia/Singapore">Asia/Singapore</option>
<option class="bx--select-option" value="Asia/Srednekolymsk">Asia/Srednekolymsk</option>
<option class="bx--select-option" value="Asia/Taipei">Asia/Taipei</option>
<option class="bx--select-option" value="Asia/Tashkent">Asia/Tashkent</option>
<option class="bx--select-option" value="Asia/Tbilisi">Asia/Tbilisi</option>
<option class="bx--select-option" value="Asia/Tehran">Asia/Tehran</option>
<option class="bx--select-option" value="Asia/Thimphu">Asia/Thimphu</option>
<option class="bx--select-option" value="Asia/Tokyo">Asia/Tokyo</option>
<option class="bx--select-option" value="Asia/Tomsk">Asia/Tomsk</option>
<option class="bx--select-option" value="Asia/Ulaanbaatar">Asia/Ulaanbaatar</option>
<option class="bx--select-option" value="Asia/Urumqi">Asia/Urumqi</option>
<option class="bx--select-option" value="Asia/Ust-Nera">Asia/Ust-Nera</option>
<option class="bx--select-option" value="Asia/Vientiane">Asia/Vientiane</option>
<option class="bx--select-option" value="Asia/Vladivostok">Asia/Vladivostok</option>
<option class="bx--select-option" value="Asia/Yakutsk">Asia/Yakutsk</option>
<option class="bx--select-option" value="Asia/Yangon">Asia/Yangon</option>
<option class="bx--select-option" value="Asia/Yekaterinburg">Asia/Yekaterinburg</option>
<option class="bx--select-option" value="Asia/Yerevan">Asia/Yerevan</option>
<option class="bx--select-option" value="Atlantic/Azores">Atlantic/Azores</option>
<option class="bx--select-option" value="Atlantic/Bermuda">Atlantic/Bermuda</option>
<option class="bx--select-option" value="Atlantic/Canary">Atlantic/Canary</option>
<option class="bx--select-option" value="Atlantic/Cape_Verde">Atlantic/Cape_Verde</option>
<option class="bx--select-option" value="Atlantic/Faroe">Atlantic/Faroe</option>
<option class="bx--select-option" value="Atlantic/Madeira">Atlantic/Madeira</option>
<option class="bx--select-option" value="Atlantic/Reykjavik">Atlantic/Reykjavik</option>
<option class="bx--select-option" value="Atlantic/South_Georgia">Atlantic/South_Georgia</option>
<option class="bx--select-option" value="Atlantic/St_Helena">Atlantic/St_Helena</option>
<option class="bx--select-option" value="Atlantic/Stanley">Atlantic/Stanley</option>
<option class="bx--select-option" value="Australia/Adelaide">Australia/Adelaide</option>
<option class="bx--select-option" value="Australia/Brisbane">Australia/Brisbane</option>
<option class="bx--select-option" value="Australia/Broken_Hill">Australia/Broken_Hill</option>
<option class="bx--select-option" value="Australia/Darwin">Australia/Darwin</option>
<option class="bx--select-option" value="Australia/Eucla">Australia/Eucla</option>
<option class="bx--select-option" value="Australia/Hobart">Australia/Hobart</option>
<option class="bx--select-option" value="Australia/Lindeman">Australia/Lindeman</option>
<option class="bx--select-option" value="Australia/Lord_Howe">Australia/Lord_Howe</option>
<option class="bx--select-option" value="Australia/Melbourne">Australia/Melbourne</option>
<option class="bx--select-option" value="Australia/Perth">Australia/Perth</option>
<option class="bx--select-option" value="Australia/Sydney">Australia/Sydney</option>
<option class="bx--select-option" value="Canada/Atlantic">Canada/Atlantic</option>
<option class="bx--select-option" value="Canada/Central">Canada/Central</option>
<option class="bx--select-option" value="Canada/Eastern">Canada/Eastern</option>
<option class="bx--select-option" value="Canada/Mountain">Canada/Mountain</option>
<option class="bx--select-option" value="Canada/Newfoundland">Canada/Newfoundland</option>
<option class="bx--select-option" value="Canada/Pacific">Canada/Pacific</option>
<option class="bx--select-option" value="Europe/Amsterdam">Europe/Amsterdam</option>
<option class="bx--select-option" value="Europe/Andorra">Europe/Andorra</option>
<option class="bx--select-option" value="Europe/Astrakhan">Europe/Astrakhan</option>
<option class="bx--select-option" value="Europe/Athens">Europe/Athens</option>
<option class="bx--select-option" value="Europe/Belgrade">Europe/Belgrade</option>
<option class="bx--select-option" value="Europe/Berlin">Europe/Berlin</option>
<option class="bx--select-option" value="Europe/Bratislava">Europe/Bratislava</option>
<option class="bx--select-option" value="Europe/Brussels">Europe/Brussels</option>
<option class="bx--select-option" value="Europe/Bucharest">Europe/Bucharest</option>
<option class="bx--select-option" value="Europe/Budapest">Europe/Budapest</option>
<option class="bx--select-option" value="Europe/Busingen">Europe/Busingen</option>
<option class="bx--select-option" value="Europe/Chisinau">Europe/Chisinau</option>
<option class="bx--select-option" value="Europe/Copenhagen">Europe/Copenhagen</option>
<option class="bx--select-option" value="Europe/Dublin">Europe/Dublin</option>
<option class="bx--select-option" value="Europe/Gibraltar">Europe/Gibraltar</option>
<option class="bx--select-option" value="Europe/Guernsey">Europe/Guernsey</option>
<option class="bx--select-option" value="Europe/Helsinki">Europe/Helsinki</option>
<option class="bx--select-option" value="Europe/Isle_of_Man">Europe/Isle_of_Man</option>
<option class="bx--select-option" value="Europe/Istanbul">Europe/Istanbul</option>
<option class="bx--select-option" value="Europe/Jersey">Europe/Jersey</option>
<option class="bx--select-option" value="Europe/Kaliningrad">Europe/Kaliningrad</option>
<option class="bx--select-option" value="Europe/Kiev">Europe/Kiev</option>
<option class="bx--select-option" value="Europe/Kirov">Europe/Kirov</option>
<option class="bx--select-option" value="Europe/Lisbon">Europe/Lisbon</option>
<option class="bx--select-option" value="Europe/Ljubljana">Europe/Ljubljana</option>
<option class="bx--select-option" value="Europe/London">Europe/London</option>
<option class="bx--select-option" value="Europe/Luxembourg">Europe/Luxembourg</option>
<option class="bx--select-option" value="Europe/Madrid">Europe/Madrid</option>
<option class="bx--select-option" value="Europe/Malta">Europe/Malta</option>
<option class="bx--select-option" value="Europe/Mariehamn">Europe/Mariehamn</option>
<option class="bx--select-option" value="Europe/Minsk">Europe/Minsk</option>
<option class="bx--select-option" value="Europe/Monaco">Europe/Monaco</option>
<option class="bx--select-option" value="Europe/Moscow">Europe/Moscow</option>
<option class="bx--select-option" value="Europe/Oslo">Europe/Oslo</option>
<option class="bx--select-option" value="Europe/Paris">Europe/Paris</option>
<option class="bx--select-option" value="Europe/Podgorica">Europe/Podgorica</option>
<option class="bx--select-option" value="Europe/Prague">Europe/Prague</option>
<option class="bx--select-option" value="Europe/Riga">Europe/Riga</option>
<option class="bx--select-option" value="Europe/Rome">Europe/Rome</option>
<option class="bx--select-option" value="Europe/Samara">Europe/Samara</option>
<option class="bx--select-option" value="Europe/San_Marino">Europe/San_Marino</option>
<option class="bx--select-option" value="Europe/Sarajevo">Europe/Sarajevo</option>
<option class="bx--select-option" value="Europe/Saratov">Europe/Saratov</option>
<option class="bx--select-option" value="Europe/Simferopol">Europe/Simferopol</option>
<option class="bx--select-option" value="Europe/Skopje">Europe/Skopje</option>
<option class="bx--select-option" value="Europe/Sofia">Europe/Sofia</option>
<option class="bx--select-option" value="Europe/Stockholm">Europe/Stockholm</option>
<option class="bx--select-option" value="Europe/Tallinn">Europe/Tallinn</option>
<option class="bx--select-option" value="Europe/Tirane">Europe/Tirane</option>
<option class="bx--select-option" value="Europe/Ulyanovsk">Europe/Ulyanovsk</option>
<option class="bx--select-option" value="Europe/Uzhgorod">Europe/Uzhgorod</option>
<option class="bx--select-option" value="Europe/Vaduz">Europe/Vaduz</option>
<option class="bx--select-option" value="Europe/Vatican">Europe/Vatican</option>
<option class="bx--select-option" value="Europe/Vienna">Europe/Vienna</option>
<option class="bx--select-option" value="Europe/Vilnius">Europe/Vilnius</option>
<option class="bx--select-option" value="Europe/Volgograd">Europe/Volgograd</option>
<option class="bx--select-option" value="Europe/Warsaw">Europe/Warsaw</option>
<option class="bx--select-option" value="Europe/Zagreb">Europe/Zagreb</option>
<option class="bx--select-option" value="Europe/Zaporozhye">Europe/Zaporozhye</option>
<option class="bx--select-option" value="Europe/Zurich">Europe/Zurich</option>
<option class="bx--select-option" value="GMT">GMT</option>
<option class="bx--select-option" value="Indian/Antananarivo">Indian/Antananarivo</option>
<option class="bx--select-option" value="Indian/Chagos">Indian/Chagos</option>
<option class="bx--select-option" value="Indian/Christmas">Indian/Christmas</option>
<option class="bx--select-option" value="Indian/Cocos">Indian/Cocos</option>
<option class="bx--select-option" value="Indian/Comoro">Indian/Comoro</option>
<option class="bx--select-option" value="Indian/Kerguelen">Indian/Kerguelen</option>
<option class="bx--select-option" value="Indian/Mahe">Indian/Mahe</option>
<option class="bx--select-option" value="Indian/Maldives">Indian/Maldives</option>
<option class="bx--select-option" value="Indian/Mauritius">Indian/Mauritius</option>
<option class="bx--select-option" value="Indian/Mayotte">Indian/Mayotte</option>
<option class="bx--select-option" value="Indian/Reunion">Indian/Reunion</option>
<option class="bx--select-option" value="Pacific/Apia">Pacific/Apia</option>
<option class="bx--select-option" value="Pacific/Auckland">Pacific/Auckland</option>
<option class="bx--select-option" value="Pacific/Bougainville">Pacific/Bougainville</option>
<option class="bx--select-option" value="Pacific/Chatham">Pacific/Chatham</option>
<option class="bx--select-option" value="Pacific/Chuuk">Pacific/Chuuk</option>
<option class="bx--select-option" value="Pacific/Easter">Pacific/Easter</option>
<option class="bx--select-option" value="Pacific/Efate">Pacific/Efate</option>
<option class="bx--select-option" value="Pacific/Fakaofo">Pacific/Fakaofo</option>
<option class="bx--select-option" value="Pacific/Fiji">Pacific/Fiji</option>
<option class="bx--select-option" value="Pacific/Funafuti">Pacific/Funafuti</option>
<option class="bx--select-option" value="Pacific/Galapagos">Pacific/Galapagos</option>
<option class="bx--select-option" value="Pacific/Gambier">Pacific/Gambier</option>
<option class="bx--select-option" value="Pacific/Guadalcanal">Pacific/Guadalcanal</option>
<option class="bx--select-option" value="Pacific/Guam">Pacific/Guam</option>
<option class="bx--select-option" value="Pacific/Honolulu">Pacific/Honolulu</option>
<option class="bx--select-option" value="Pacific/Kanton">Pacific/Kanton</option>
<option class="bx--select-option" value="Pacific/Kiritimati">Pacific/Kiritimati</option>
<option class="bx--select-option" value="Pacific/Kosrae">Pacific/Kosrae</option>
<option class="bx--select-option" value="Pacific/Kwajalein">Pacific/Kwajalein</option>
<option class="bx--select-option" value="Pacific/Majuro">Pacific/Majuro</option>
<option class="bx--select-option" value="Pacific/Marquesas">Pacific/Marquesas</option>
<option class="bx--select-option" value="Pacific/Midway">Pacific/Midway</option>
<option class="bx--select-option" value="Pacific/Nauru">Pacific/Nauru</option>
<option class="bx--select-option" value="Pacific/Niue">Pacific/Niue</option>
<option class="bx--select-option" value="Pacific/Norfolk">Pacific/Norfolk</option>
<option class="bx--select-option" value="Pacific/Noumea">Pacific/Noumea</option>
<option class="bx--select-option" value="Pacific/Pago_Pago">Pacific/Pago_Pago</option>
<option class="bx--select-option" value="Pacific/Palau">Pacific/Palau</option>
<option class="bx--select-option" value="Pacific/Pitcairn">Pacific/Pitcairn</option>
<option class="bx--select-option" value="Pacific/Pohnpei">Pacific/Pohnpei</option>
<option class="bx--select-option" value="Pacific/Port_Moresby">Pacific/Port_Moresby</option>
<option class="bx--select-option" value="Pacific/Rarotonga">Pacific/Rarotonga</option>
<option class="bx--select-option" value="Pacific/Saipan">Pacific/Saipan</option>
<option class="bx--select-option" value="Pacific/Tahiti">Pacific/Tahiti</option>
<option class="bx--select-option" value="Pacific/Tarawa">Pacific/Tarawa</option>
<option class="bx--select-option" value="Pacific/Tongatapu">Pacific/Tongatapu</option>
<option class="bx--select-option" value="Pacific/Wake">Pacific/Wake</option>
<option class="bx--select-option" value="Pacific/Wallis">Pacific/Wallis</option>
<option class="bx--select-option" value="US/Alaska">US/Alaska</option>
<option class="bx--select-option" value="US/Arizona">US/Arizona</option>
<option class="bx--select-option" value="US/Central">US/Central</option>
<option class="bx--select-option" value="US/Eastern">US/Eastern</option>
<option class="bx--select-option" value="US/Hawaii">US/Hawaii</option>
<option class="bx--select-option" value="US/Mountain">US/Mountain</option>
<option class="bx--select-option" value="US/Pacific">US/Pacific</option>
<option class="bx--select-option" value="UTC">UTC</option>
  </select>
  <svg focusable="false" preserveAspectRatio="xMidYMid meet"
      xmlns="http://www.w3.org/2000/svg" fill="currentColor"
      class="bx--select__arrow" width="16" height="16" viewBox="0 0 16 16"
      aria-hidden="true">
    <path d="M8 11L3 6 3.7 5.3 8 9.6 12.3 5.3 13 6z"></path>
  </svg>
</div>
  </div>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)
