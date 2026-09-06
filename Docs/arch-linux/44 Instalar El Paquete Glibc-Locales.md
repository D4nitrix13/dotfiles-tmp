<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- Gitlab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# ***Instalación de paquetes con `pacman`***

**Para instalar paquetes en Arch Linux, se utiliza el gestor de paquetes `pacman`. Aquí se explica cómo instalar el paquete `glibc-locales` y generar locales utilizando `locale-gen`:**

```bash
sudo pacman -Syu glibc-locales --noconfirm
```

- **`sudo`:** *Ejecuta el comando con privilegios de superusuario.*
- **`pacman`:** *El gestor de paquetes de Arch Linux.*
- **`-S`:** *Subcomando para instalar paquetes.*
- **`glibc-locales`:** *Nombre del paquete a ser instalado.*

**Después de instalar el paquete, es necesario generar las locales:**

```bash
sudo locale-gen
```

- **glibc-locales** *es un paquete que forma parte de la GNU C Library (glibc), proporcionando los datos necesarios para la localización (locale) en sistemas Unix y Unix-like, como Linux. La localización implica adaptar el software a diferentes lenguajes, regiones y preferencias culturales.*

---

## ***¿Qué es glibc-locales?***

**`glibc-locales` incluye conjuntos de datos para manejar la localización, que abarcan información sobre:**

- *Formatos de fecha y hora*
- *Formatos de número y moneda*
- *Clasificación de caracteres y collation (ordenación)*
- *Traducciones de mensajes del sistema y del entorno de programación*
- *Otras configuraciones regionales y de idioma*

---

### ***Características y Funcionalidades***

1. **Soporte Multilingüe:** *Permite a los programas funcionar en múltiples idiomas y configuraciones regionales.*
2. **Formato de Datos:** *Gestiona cómo se presentan las fechas, horas, números y monedas según las convenciones locales.*
3. **Clasificación y Ordenación:** *Define las reglas de ordenación de cadenas de texto de acuerdo con las reglas locales de cada idioma.*
4. **Traducciones del Sistema:** *Proporciona traducciones de mensajes y textos del sistema operativo.*
5. **Configuración Regional:** *Permite la personalización de los entornos de usuario según las preferencias locales.*

---

### ***Ficheros de Localización***

- *Las locales se definen en ficheros que especifican las configuraciones regionales. Estos ficheros se encuentran comúnmente en `/usr/share/i18n/locales/`.*

```bash
lsd /usr/share/i18n/locales/
 aa_DJ             es_CU                my_MM                   ve_ZA
 aa_ER             es_DO                nan_TW                  vi_VN
 aa_ET             es_EC                nan_TW@latin            wa_BE
 ab_GE             es_ES                nb_NO                   wa_BE@euro
 af_ZA             es_ES@euro           nds_DE                  wae_CH
 agr_PE            es_GT                nds_NL                  wal_ET
 ak_GH             es_HN                ne_NP                   wo_SN
 am_ET             es_MX                nhn_MX                  xh_ZA
 an_ES             es_NI                niu_NU                  yi_US
 anp_IN            es_PA                niu_NZ                  yo_NG
 ar_AE             es_PE                nl_AW                   yue_HK
 ar_BH             es_PR                nl_BE                   yuw_PG
 ar_DZ             es_PY                nl_BE@euro              zgh_MA
 ar_EG             es_SV                nl_NL                   zh_CN
 ar_IN             es_US                nl_NL@euro              zh_HK
 ar_IQ             es_UY                nn_NO                   zh_SG
 ar_JO             es_VE                nr_ZA                   zh_TW
 ar_KW             et_EE                nso_ZA                  zu_ZA
 ar_LB             eu_ES                oc_FR                  
 ar_LY             eu_ES@euro           om_ET                  
 ar_MA             fa_IR                om_KE                  
 ar_OM             ff_SN                or_IN                  
 ar_QA             fi_FI                os_RU                  
 ar_SA             fi_FI@euro           pa_IN                  
 ar_SD             fil_PH               pa_PK                  
 ar_SS             fo_FO                pap_AW                 
 ar_SY             fr_BE                pap_CW                 
 ar_TN             fr_BE@euro           pl_PL                  
 ar_YE             fr_CA                POSIX                  
 as_IN             fr_CH                ps_AF                  
 ast_ES            fr_FR                pt_BR                  
 ayc_PE            fr_FR@euro           pt_PT                  
 az_AZ             fr_LU                pt_PT@euro             
 az_IR             fr_LU@euro           quz_PE                 
 be_BY             fur_IT               raj_IN                 
 be_BY@latin       fy_DE                rif_MA                 
 bem_ZM            fy_NL                ro_RO                  
 ber_DZ            ga_IE                ru_RU                  
 ber_MA            ga_IE@euro           ru_UA                  
 bg_BG             gbm_IN               rw_RW                  
 bhb_IN            gd_GB                sa_IN                  
 bho_IN            gez_ER               sah_RU                 
 bho_NP            gez_ER@abegede       sat_IN                 
 bi_VU             gez_ET               sc_IT                  
 bn_BD             gez_ET@abegede       sd_IN                  
 bn_IN             gl_ES                sd_IN@devanagari       
 bo_CN             gl_ES@euro           se_NO                  
 bo_IN             gu_IN                sgs_LT                 
 br_FR             gv_GB                shn_MM                 
 br_FR@euro        ha_NG                shs_CA                 
 brx_IN            hak_TW               si_LK                  
 bs_BA             he_IL                sid_ET                 
 byn_ER            hi_IN                sk_SK                  
 C                 hif_FJ               sl_SI                  
 ca_AD             hne_IN               sm_WS                  
 ca_ES             hr_HR                so_DJ                  
 ca_ES@euro        hsb_DE               so_ET                  
 ca_ES@valencia    ht_HT                so_KE                  
 ca_FR             hu_HU                so_SO                  
 ca_IT             hy_AM                sq_AL                  
 ce_RU             i18n                 sq_MK                  
 chr_US            i18n_ctype           sr_ME                  
 ckb_IQ            ia_FR                sr_RS                  
 cmn_TW            id_ID                sr_RS@latin            
 cns11643_stroke   ig_NG                ss_ZA                  
 crh_RU            ik_CA                ssy_ER                 
 crh_UA            is_IS                st_ZA                  
 cs_CZ             iso14651_t1          su_ID                  
 csb_PL            iso14651_t1_common   sv_FI                  
 cv_RU             iso14651_t1_pinyin   sv_FI@euro             
 cy_GB             it_CH                sv_SE                  
 da_DK             it_IT                sw_KE                  
 de_AT             it_IT@euro           sw_TZ                  
 de_AT@euro        iu_CA                syr                    
 de_BE             ja_JP                szl_PL                 
 de_BE@euro        ka_GE                ta_IN                  
 de_CH             kab_DZ               ta_LK                  
 de_DE             kk_KZ                tcy_IN                 
 de_DE@euro        kl_GL                te_IN                  
 de_IT             km_KH                tg_TJ                  
 de_LI             kn_IN                th_TH                  
 de_LU             ko_KR                the_NP                 
 de_LU@euro        kok_IN               ti_ER                  
 doi_IN            ks_IN                ti_ET                  
 dsb_DE            ks_IN@devanagari     tig_ER                 
 dv_MV             ku_TR                tk_TM                  
 dz_BT             kv_RU                tl_PH                  
 el_CY             kw_GB                tn_ZA                  
 el_GR             ky_KG                to_TO                  
 el_GR@euro        lb_LU                tok                    
 en_AG             lg_UG                tpi_PG                 
 en_AU             li_BE                tr_CY                  
 en_BW             li_NL                tr_TR                  
 en_CA             lij_IT               translit_circle        
 en_DK             ln_CD                translit_cjk_compat    
 en_GB             lo_LA                translit_cjk_variants  
 en_HK             lt_LT                translit_combining     
 en_IE             lv_LV                translit_compat        
 en_IE@euro        lzh_TW               translit_emojis        
 en_IL             mag_IN               translit_font          
 en_IN             mai_IN               translit_fraction      
 en_NG             mai_NP               translit_hangul        
 en_NZ             mfe_MU               translit_narrow        
 en_PH             mg_MG                translit_neutral       
 en_SC             mhr_RU               translit_small         
 en_SG             mi_NZ                translit_wide          
 en_US             miq_NI               ts_ZA                  
 en_ZA             mjw_IN               tt_RU                  
 en_ZM             mk_MK                tt_RU@iqtelif          
 en_ZW             ml_IN                ug_CN                  
 eo                mn_MN                uk_UA                  
 es_AR             mni_IN               unm_US                 
 es_BO             mnw_MM               ur_IN                  
 es_CL             mr_IN                ur_PK                  
 es_CO             ms_MY                uz_UZ                  
 es_CR             mt_MT                uz_UZ@cyrillic
```

### ***Generación y Configuración de Locales en Arch Linux***

- *Para utilizar una locale específica, es necesario generarla y configurarla en el sistema.*

1. **Editar el Fichero de Configuración de Locales:**
   - Abre el fichero `/etc/locale.gen` y descomenta las locales que necesitas.*

   ```bash
   sudo nano /etc/locale.gen
   ```

   **Por ejemplo, para generar las locales en español (España) y en inglés (Estados Unidos), descomenta las siguientes líneas:**

   ```plaintext
   en_US.UTF-8 UTF-8
   es_ES.UTF-8 UTF-8
   ```

2. **Generar las Locales:**
   - *Ejecuta el comando `locale-gen` para generar las locales que descomentaste.*

   ```bash
   sudo locale-gen
   ```

3. **Configurar la Locale del Sistema:**
   - *Establece la locale por defecto del sistema en el fichero `/etc/locale.conf`.*

   ```bash
   sudo nano /etc/locale.conf
   ```

   **Añade la siguiente línea para establecer `en_US.UTF-8` como la locale por defecto:**

   ```plaintext
   LANG=en_US.UTF-8
   ```

4. **Aplicar la Configuración de Locale en la Sesión Actual:**
   - *Puedes establecer temporalmente la locale en la sesión actual usando el comando `export`.*

   ```bash
   export LANG=en_US.UTF-8
   ```

---

### ***Verificación de la Configuración de Locales***

**Para verificar las locales disponibles y la configuración actual del sistema, puedes utilizar los siguientes comandos:**

- **Mostrar Locales Disponibles:**

  ```bash
  locale -a
  ```

- **Mostrar la Configuración Actual de Locale:**

  ```bash
  locale
  ```

### ***Ejemplo de Uso***

**Supongamos que deseas que tu sistema utilice el español de España como la configuración regional por defecto:**

1. *Abre el fichero `/etc/locale.gen` y descomenta `es_ES.UTF-8 UTF-8`.*
2. *Ejecuta `sudo locale-gen`.*
3. *Configura `/etc/locale.conf` con `LANG=es_ES.UTF-8`.*

---

### ***Problemas Comunes***

- **Falta de Traducciones:** *Algunos programas pueden no tener traducciones completas para ciertas locales.*
- **Configuración Incorrecta:** *Si no se generan correctamente las locales, los programas pueden mostrar caracteres incorrectos o no funcionar como se espera.*

---

### ***Conclusión***

- *`glibc-locales` es esencial para la adaptación de software a diferentes configuraciones regionales y lingüísticas. Configurar adecuadamente las locales en Arch Linux asegura que tu sistema y aplicaciones funcionen correctamente según tus preferencias regionales y de idioma.*

- *Fichero `/etc/locale.gen`*

```ini
# Configuration file for locale-gen
#
# lists of locales that are to be generated by the locale-gen command.
#
# Each line is of the form:
#
#     <locale> <charset>
#
#  where <locale> is one of the locales given in /usr/share/i18n/locales
#  and <charset> is one of the character sets listed in /usr/share/i18n/charmaps
#
#  The locale-gen command will generate all the locales,
#  placing them in /usr/lib/locale.
#
#  A list of supported locales is given in /usr/share/i18n/SUPPORTED
#  and is included in this file. Uncomment the needed locales below.
#
#aa_DJ.UTF-8 UTF-8  
#aa_DJ ISO-8859-1  
#aa_ER UTF-8  
#aa_ET UTF-8  
#af_ZA.UTF-8 UTF-8  
#af_ZA ISO-8859-1  
#agr_PE UTF-8  
#ak_GH UTF-8  
#am_ET UTF-8  
#an_ES.UTF-8 UTF-8  
#an_ES ISO-8859-15  
#anp_IN UTF-8  
#ar_AE.UTF-8 UTF-8  
#ar_AE ISO-8859-6  
#ar_BH.UTF-8 UTF-8  
#ar_BH ISO-8859-6  
#ar_DZ.UTF-8 UTF-8  
#ar_DZ ISO-8859-6  
#ar_EG.UTF-8 UTF-8  
#ar_EG ISO-8859-6  
#ar_IN UTF-8  
#ar_IQ.UTF-8 UTF-8  
#ar_IQ ISO-8859-6  
#ar_JO.UTF-8 UTF-8  
#ar_JO ISO-8859-6  
#ar_KW.UTF-8 UTF-8  
#ar_KW ISO-8859-6  
#ar_LB.UTF-8 UTF-8  
#ar_LB ISO-8859-6  
#ar_LY.UTF-8 UTF-8  
#ar_LY ISO-8859-6  
#ar_MA.UTF-8 UTF-8  
#ar_MA ISO-8859-6  
#ar_OM.UTF-8 UTF-8  
#ar_OM ISO-8859-6  
#ar_QA.UTF-8 UTF-8  
#ar_QA ISO-8859-6  
#ar_SA.UTF-8 UTF-8  
#ar_SA ISO-8859-6  
#ar_SD.UTF-8 UTF-8  
#ar_SD ISO-8859-6  
#ar_SS UTF-8  
#ar_SY.UTF-8 UTF-8  
#ar_SY ISO-8859-6  
#ar_TN.UTF-8 UTF-8  
#ar_TN ISO-8859-6  
#ar_YE.UTF-8 UTF-8  
#ar_YE ISO-8859-6  
#ayc_PE UTF-8  
#az_AZ UTF-8  
#az_IR UTF-8  
#as_IN UTF-8  
#ast_ES.UTF-8 UTF-8  
#ast_ES ISO-8859-15  
#be_BY.UTF-8 UTF-8  
#be_BY CP1251  
#be_BY@latin UTF-8  
#bem_ZM UTF-8  
#ber_DZ UTF-8  
#ber_MA UTF-8  
#bg_BG.UTF-8 UTF-8  
#bg_BG CP1251  
#bhb_IN.UTF-8 UTF-8  
#bho_IN UTF-8  
#bho_NP UTF-8  
#bi_VU UTF-8  
#bn_BD UTF-8  
#bn_IN UTF-8  
#bo_CN UTF-8  
#bo_IN UTF-8  
#br_FR.UTF-8 UTF-8  
#br_FR ISO-8859-1  
#br_FR@euro ISO-8859-15  
#brx_IN UTF-8  
#bs_BA.UTF-8 UTF-8  
#bs_BA ISO-8859-2  
#byn_ER UTF-8  
#ca_AD.UTF-8 UTF-8  
#ca_AD ISO-8859-15  
#ca_ES.UTF-8 UTF-8  
#ca_ES ISO-8859-1  
#ca_ES@euro ISO-8859-15  
#ca_ES@valencia UTF-8  
#ca_FR.UTF-8 UTF-8  
#ca_FR ISO-8859-15  
#ca_IT.UTF-8 UTF-8  
#ca_IT ISO-8859-15  
#ce_RU UTF-8  
#chr_US UTF-8  
#ckb_IQ UTF-8  
#cmn_TW UTF-8  
#crh_RU UTF-8  
#crh_UA UTF-8  
#cs_CZ.UTF-8 UTF-8  
#cs_CZ ISO-8859-2  
#csb_PL UTF-8  
#cv_RU UTF-8  
#cy_GB.UTF-8 UTF-8  
#cy_GB ISO-8859-14  
#da_DK.UTF-8 UTF-8  
#da_DK ISO-8859-1  
#de_AT.UTF-8 UTF-8  
#de_AT ISO-8859-1  
#de_AT@euro ISO-8859-15  
#de_BE.UTF-8 UTF-8  
#de_BE ISO-8859-1  
#de_BE@euro ISO-8859-15  
#de_CH.UTF-8 UTF-8  
#de_CH ISO-8859-1  
#de_DE.UTF-8 UTF-8  
#de_DE ISO-8859-1  
#de_DE@euro ISO-8859-15  
#de_IT.UTF-8 UTF-8  
#de_IT ISO-8859-1  
#de_LI.UTF-8 UTF-8  
#de_LU.UTF-8 UTF-8  
#de_LU ISO-8859-1  
#de_LU@euro ISO-8859-15  
#doi_IN UTF-8  
#dsb_DE UTF-8  
#dv_MV UTF-8  
#dz_BT UTF-8  
#el_GR.UTF-8 UTF-8  
#el_GR ISO-8859-7  
#el_GR@euro ISO-8859-7  
#el_CY.UTF-8 UTF-8  
#el_CY ISO-8859-7  
#en_AG UTF-8  
#en_AU.UTF-8 UTF-8  
#en_AU ISO-8859-1  
#en_BW.UTF-8 UTF-8  
#en_BW ISO-8859-1  
#en_CA.UTF-8 UTF-8  
#en_CA ISO-8859-1  
#en_DK.UTF-8 UTF-8  
#en_DK ISO-8859-1  
#en_GB.UTF-8 UTF-8  
#en_GB ISO-8859-1  
#en_HK.UTF-8 UTF-8  
#en_HK ISO-8859-1  
#en_IE.UTF-8 UTF-8  
#en_IE ISO-8859-1  
#en_IE@euro ISO-8859-15  
#en_IL UTF-8  
#en_IN UTF-8  
#en_NG UTF-8  
#en_NZ.UTF-8 UTF-8  
#en_NZ ISO-8859-1  
#en_PH.UTF-8 UTF-8  
#en_PH ISO-8859-1  
#en_SC.UTF-8 UTF-8  
#en_SG.UTF-8 UTF-8  
#en_SG ISO-8859-1  
en_US.UTF-8 UTF-8  
#en_US ISO-8859-1  
#en_ZA.UTF-8 UTF-8  
#en_ZA ISO-8859-1  
#en_ZM UTF-8  
#en_ZW.UTF-8 UTF-8  
#en_ZW ISO-8859-1  
#eo UTF-8  
#es_AR.UTF-8 UTF-8  
#es_AR ISO-8859-1  
#es_BO.UTF-8 UTF-8  
#es_BO ISO-8859-1  
#es_CL.UTF-8 UTF-8  
#es_CL ISO-8859-1  
#es_CO.UTF-8 UTF-8  
#es_CO ISO-8859-1  
#es_CR.UTF-8 UTF-8  
#es_CR ISO-8859-1  
#es_CU UTF-8  
#es_DO.UTF-8 UTF-8  
#es_DO ISO-8859-1  
#es_EC.UTF-8 UTF-8  
#es_EC ISO-8859-1  
#es_ES.UTF-8 UTF-8  
#es_ES ISO-8859-1  
#es_ES@euro ISO-8859-15  
#es_GT.UTF-8 UTF-8  
#es_GT ISO-8859-1  
#es_HN.UTF-8 UTF-8  
#es_HN ISO-8859-1  
#es_MX.UTF-8 UTF-8  
#es_MX ISO-8859-1  
#es_NI.UTF-8 UTF-8  
#es_NI ISO-8859-1  
#es_PA.UTF-8 UTF-8  
#es_PA ISO-8859-1  
#es_PE.UTF-8 UTF-8  
#es_PE ISO-8859-1  
#es_PR.UTF-8 UTF-8  
#es_PR ISO-8859-1  
#es_PY.UTF-8 UTF-8  
#es_PY ISO-8859-1  
#es_SV.UTF-8 UTF-8  
#es_SV ISO-8859-1  
es_US.UTF-8 UTF-8  
#es_US ISO-8859-1  
#es_UY.UTF-8 UTF-8  
#es_UY ISO-8859-1  
#es_VE.UTF-8 UTF-8  
#es_VE ISO-8859-1  
#et_EE.UTF-8 UTF-8  
#et_EE ISO-8859-1  
#et_EE.ISO-8859-15 ISO-8859-15  
#eu_ES.UTF-8 UTF-8  
#eu_ES ISO-8859-1  
#eu_ES@euro ISO-8859-15  
#fa_IR UTF-8  
#ff_SN UTF-8  
#fi_FI.UTF-8 UTF-8  
#fi_FI ISO-8859-1  
#fi_FI@euro ISO-8859-15  
#fil_PH UTF-8  
#fo_FO.UTF-8 UTF-8  
#fo_FO ISO-8859-1  
#fr_BE.UTF-8 UTF-8  
#fr_BE ISO-8859-1  
#fr_BE@euro ISO-8859-15  
#fr_CA.UTF-8 UTF-8  
#fr_CA ISO-8859-1  
#fr_CH.UTF-8 UTF-8  
#fr_CH ISO-8859-1  
#fr_FR.UTF-8 UTF-8  
#fr_FR ISO-8859-1  
#fr_FR@euro ISO-8859-15  
#fr_LU.UTF-8 UTF-8  
#fr_LU ISO-8859-1  
#fr_LU@euro ISO-8859-15  
#fur_IT UTF-8  
#fy_NL UTF-8  
#fy_DE UTF-8  
#ga_IE.UTF-8 UTF-8  
#ga_IE ISO-8859-1  
#ga_IE@euro ISO-8859-15  
#gbm_IN UTF-8  
#gd_GB.UTF-8 UTF-8  
#gd_GB ISO-8859-15  
#gez_ER UTF-8  
#gez_ER@abegede UTF-8  
#gez_ET UTF-8  
#gez_ET@abegede UTF-8  
#gl_ES.UTF-8 UTF-8  
#gl_ES ISO-8859-1  
#gl_ES@euro ISO-8859-15  
#gu_IN UTF-8  
#gv_GB.UTF-8 UTF-8  
#gv_GB ISO-8859-1  
#ha_NG UTF-8  
#hak_TW UTF-8  
#he_IL.UTF-8 UTF-8  
#he_IL ISO-8859-8  
#hi_IN UTF-8  
#hif_FJ UTF-8  
#hne_IN UTF-8  
#hr_HR.UTF-8 UTF-8  
#hr_HR ISO-8859-2  
#hsb_DE ISO-8859-2  
#hsb_DE.UTF-8 UTF-8  
#ht_HT UTF-8  
#hu_HU.UTF-8 UTF-8  
#hu_HU ISO-8859-2  
#hy_AM UTF-8  
#hy_AM.ARMSCII-8 ARMSCII-8  
#ia_FR UTF-8  
#id_ID.UTF-8 UTF-8  
#id_ID ISO-8859-1  
#ig_NG UTF-8  
#ik_CA UTF-8  
#is_IS.UTF-8 UTF-8  
#is_IS ISO-8859-1  
#it_CH.UTF-8 UTF-8  
#it_CH ISO-8859-1  
#it_IT.UTF-8 UTF-8  
#it_IT ISO-8859-1  
#it_IT@euro ISO-8859-15  
#iu_CA UTF-8  
#ja_JP.EUC-JP EUC-JP  
#ja_JP.UTF-8 UTF-8  
#ka_GE.UTF-8 UTF-8  
#ka_GE GEORGIAN-PS  
#kab_DZ UTF-8  
#kk_KZ.UTF-8 UTF-8  
#kk_KZ PT154  
#kl_GL.UTF-8 UTF-8  
#kl_GL ISO-8859-1  
#km_KH UTF-8  
#kn_IN UTF-8  
#ko_KR.EUC-KR EUC-KR  
#ko_KR.UTF-8 UTF-8  
#kok_IN UTF-8  
#ks_IN UTF-8  
#ks_IN@devanagari UTF-8  
#ku_TR.UTF-8 UTF-8  
#ku_TR ISO-8859-9  
#kv_RU UTF-8  
#kw_GB.UTF-8 UTF-8  
#kw_GB ISO-8859-1  
#ky_KG UTF-8  
#lb_LU UTF-8  
#lg_UG.UTF-8 UTF-8  
#lg_UG ISO-8859-10  
#li_BE UTF-8  
#li_NL UTF-8  
#lij_IT UTF-8  
#ln_CD UTF-8  
#lo_LA UTF-8  
#lt_LT.UTF-8 UTF-8  
#lt_LT ISO-8859-13  
#lv_LV.UTF-8 UTF-8  
#lv_LV ISO-8859-13  
#lzh_TW UTF-8  
#mag_IN UTF-8  
#mai_IN UTF-8  
#mai_NP UTF-8  
#mfe_MU UTF-8  
#mg_MG.UTF-8 UTF-8  
#mg_MG ISO-8859-15  
#mhr_RU UTF-8  
#mi_NZ.UTF-8 UTF-8  
#mi_NZ ISO-8859-13  
#miq_NI UTF-8  
#mjw_IN UTF-8  
#mk_MK.UTF-8 UTF-8  
#mk_MK ISO-8859-5  
#ml_IN UTF-8  
#mn_MN UTF-8  
#mni_IN UTF-8  
#mnw_MM UTF-8  
#mr_IN UTF-8  
#ms_MY.UTF-8 UTF-8  
#ms_MY ISO-8859-1  
#mt_MT.UTF-8 UTF-8  
#mt_MT ISO-8859-3  
#my_MM UTF-8  
#nan_TW UTF-8  
#nan_TW@latin UTF-8  
#nb_NO.UTF-8 UTF-8  
#nb_NO ISO-8859-1  
#nds_DE UTF-8  
#nds_NL UTF-8  
#ne_NP UTF-8  
#nhn_MX UTF-8  
#niu_NU UTF-8  
#niu_NZ UTF-8  
#nl_AW UTF-8  
#nl_BE.UTF-8 UTF-8  
#nl_BE ISO-8859-1  
#nl_BE@euro ISO-8859-15  
#nl_NL.UTF-8 UTF-8  
#nl_NL ISO-8859-1  
#nl_NL@euro ISO-8859-15  
#nn_NO.UTF-8 UTF-8  
#nn_NO ISO-8859-1  
#nr_ZA UTF-8  
#nso_ZA UTF-8  
#oc_FR.UTF-8 UTF-8  
#oc_FR ISO-8859-1  
#om_ET UTF-8  
#om_KE.UTF-8 UTF-8  
#om_KE ISO-8859-1  
#or_IN UTF-8  
#os_RU UTF-8  
#pa_IN UTF-8  
#pa_PK UTF-8  
#pap_AW UTF-8  
#pap_CW UTF-8  
#pl_PL.UTF-8 UTF-8  
#pl_PL ISO-8859-2  
#ps_AF UTF-8  
#pt_BR.UTF-8 UTF-8  
#pt_BR ISO-8859-1  
#pt_PT.UTF-8 UTF-8  
#pt_PT ISO-8859-1  
#pt_PT@euro ISO-8859-15  
#quz_PE UTF-8  
#raj_IN UTF-8  
#rif_MA UTF-8  
#ro_RO.UTF-8 UTF-8  
#ro_RO ISO-8859-2  
#ru_RU.KOI8-R KOI8-R  
#ru_RU.UTF-8 UTF-8  
#ru_RU ISO-8859-5  
#ru_UA.UTF-8 UTF-8  
#ru_UA KOI8-U  
#rw_RW UTF-8  
#sa_IN UTF-8  
#sah_RU UTF-8  
#sat_IN UTF-8  
#sc_IT UTF-8  
#sd_IN UTF-8  
#sd_IN@devanagari UTF-8  
#se_NO UTF-8  
#sgs_LT UTF-8  
#shn_MM UTF-8  
#shs_CA UTF-8  
#si_LK UTF-8  
#sid_ET UTF-8  
#sk_SK.UTF-8 UTF-8  
#sk_SK ISO-8859-2  
#sl_SI.UTF-8 UTF-8  
#sl_SI ISO-8859-2  
#sm_WS UTF-8  
#so_DJ.UTF-8 UTF-8  
#so_DJ ISO-8859-1  
#so_ET UTF-8  
#so_KE.UTF-8 UTF-8  
#so_KE ISO-8859-1  
#so_SO.UTF-8 UTF-8  
#so_SO ISO-8859-1  
#sq_AL.UTF-8 UTF-8  
#sq_AL ISO-8859-1  
#sq_MK UTF-8  
#sr_ME UTF-8  
#sr_RS UTF-8  
#sr_RS@latin UTF-8  
#ss_ZA UTF-8  
#ssy_ER UTF-8  
#st_ZA.UTF-8 UTF-8  
#st_ZA ISO-8859-1  
#su_ID UTF-8  
#sv_FI.UTF-8 UTF-8  
#sv_FI ISO-8859-1  
#sv_FI@euro ISO-8859-15  
#sv_SE.UTF-8 UTF-8  
#sv_SE ISO-8859-1  
#sw_KE UTF-8  
#sw_TZ UTF-8  
#syr UTF-8  
#szl_PL UTF-8  
#ta_IN UTF-8  
#ta_LK UTF-8  
#tcy_IN.UTF-8 UTF-8  
#te_IN UTF-8  
#tg_TJ.UTF-8 UTF-8  
#tg_TJ KOI8-T  
#th_TH.UTF-8 UTF-8  
#th_TH TIS-620  
#the_NP UTF-8  
#ti_ER UTF-8  
#ti_ET UTF-8  
#tig_ER UTF-8  
#tk_TM UTF-8  
#tl_PH.UTF-8 UTF-8  
#tl_PH ISO-8859-1  
#tn_ZA UTF-8  
#to_TO UTF-8  
#tok UTF-8  
#tpi_PG UTF-8  
#tr_CY.UTF-8 UTF-8  
#tr_CY ISO-8859-9  
#tr_TR.UTF-8 UTF-8  
#tr_TR ISO-8859-9  
#ts_ZA UTF-8  
#tt_RU UTF-8  
#tt_RU@iqtelif UTF-8  
#ug_CN UTF-8  
#uk_UA.UTF-8 UTF-8  
#uk_UA KOI8-U  
#unm_US UTF-8  
#ur_IN UTF-8  
#ur_PK UTF-8  
#uz_UZ.UTF-8 UTF-8  
#uz_UZ ISO-8859-1  
#uz_UZ@cyrillic UTF-8  
#ve_ZA UTF-8  
#vi_VN UTF-8  
#wa_BE ISO-8859-1  
#wa_BE@euro ISO-8859-15  
#wa_BE.UTF-8 UTF-8  
#wae_CH UTF-8  
#wal_ET UTF-8  
#wo_SN UTF-8  
#xh_ZA.UTF-8 UTF-8  
#xh_ZA ISO-8859-1  
#yi_US.UTF-8 UTF-8  
#yi_US CP1255  
#yo_NG UTF-8  
#yue_HK UTF-8  
#yuw_PG UTF-8  
#zgh_MA UTF-8  
#zh_CN.GB18030 GB18030  
#zh_CN.GBK GBK  
#zh_CN.UTF-8 UTF-8  
#zh_CN GB2312  
#zh_HK.UTF-8 UTF-8  
#zh_HK BIG5-HKSCS  
#zh_SG.UTF-8 UTF-8  
#zh_SG.GBK GBK  
#zh_SG GB2312  
#zh_TW.EUC-TW EUC-TW  
#zh_TW.UTF-8 UTF-8  
#zh_TW BIG5  
#zu_ZA.UTF-8 UTF-8  
#zu_ZA ISO-8859-1  
```
