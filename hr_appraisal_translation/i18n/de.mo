��    �      l    �      �  '   �  /     $   I     n     w     �     �     �     �     �  �  �  �  1  �    "   �  *   �  $   �  B    @  Y    �     �!  =   �"  	  �"  e   �#  n   S$  �   �$  0   �%  /   �%     &     &  
   &     !&     ?&     N&     a&     z&  	   �&     �&     �&  (   �&  '   �&     '     '  $   .'     S'     j'  #   y'     �'     �'     �'     �'     �'     (  !   (  
   7(     B(     X(     a(     q(     �(     �(     �(  !   �(     �(     �(     �(     )     )     $)  %   =)  	   c)     m)  	   s)     })     �)     �)     �)     �)      �)  	   �)     �)     �)     �)     *  
   '*  
   2*     =*     K*     P*  	   Y*     c*  
   j*     u*     �*     �*     �*     �*     �*     �*     �*     �*     �*     +     /+     J+     X+  	   h+     r+     �+  H   �+     �+     �+  	   	,     ,     (,     =,     ],     b,     t,     z,     �,  '   �,  0   �,  0   �,     -  	   -     )-  	   A-     K-  
   W-     b-     o-     �-     �-     �-     �-     �-     �-     �-     �-     �-     .     %.     -.     @.     W.     `.     n.     w.     �.     �.     �.     �.     �.     �.  +    /  &   ,/     S/     m/     s/     /     �/  
   �/     �/  8   �/  	   �/     �/     0     #0     60     S0     d0     q0     z0  ;   �0  x   �0     81     U1  
   ]1     h1  i   �1  5   �1  �   '2     �2     �2     �2  )   �2     �2     3     &3     33     83  '   >3     f3     w3  �   �3  C   (4  �   l4  �   85  �   �5     o6     �6    �6  '   �7  2   �7  *   8     -8     68     C8     I8     N8     [8     `8  �  e8  �  "=  �  A  #   �D  -   �D  (   E  B  6E  @  yF    �G    �H  >   �I    )J  h   DK  o   �K  �   L  2   �L  =   0M     nM     M     �M     �M     �M     �M  #   �M      N  	   N     N     'N  0   GN  ,   xN     �N     �N  (   �N     �N     O  $   'O     LO     ]O     uO     �O  &   �O     �O  0   �O     P     P  
   >P     IP  
   [P     fP     tP     zP  $   �P     �P     �P  '   �P  #   Q  	   )Q  $   3Q  4   XQ     �Q     �Q     �Q     �Q     �Q     �Q     �Q     �Q  )   �Q  
   R     &R     .R     :R  !   ZR     |R     �R  
   �R     �R     �R     �R     �R  	   �R     �R     �R     �R     �R     S     S     S     6S     BS     ZS  $   vS     �S     �S     �S     �S     �S     �S  Q   T     eT     xT  
   �T     �T     �T     �T     �T     �T     �T      U     U  ,    U  ?   MU  U   �U     �U     �U     �U  
   V     V     *V     6V     <V     OV     iV     ~V     �V  
   �V     �V     �V     �V      �V     W     ,W     4W     MW     mW     yW     �W     �W     �W     �W     �W     X     "X     6X  1   ?X  4   qX     �X     �X     �X     �X     �X  
   Y     Y  F   3Y     zY     �Y     �Y     �Y  !   �Y     �Y     �Y     Z     Z  :   'Z  �   bZ  &   [     -[  
   5[  "   @[  ^   c[  5   �[  �   �[     �\  	   �\     �\  (   �\     �\  #   ]     3]     C]     L]  -   U]     �]     �]  �   �]  ^   e^  �   �^  �   �_  �   u`     )a     <a     K   X   �   �   7               I   �   m      �      �   �   V   *   H       h   A   �   l   d   �       �           �   �           �           ,       �   �      Y       �      %   }   �       �          8      )       �   J       !   �   �   �   �       j   �   �      u   �   ]   D   �   Q   �   �       :   |       P          q          o   g   `   2   T   �   �       9   v   �              �   L      {   k      6         p   ;   (   �      S   �       b           ~       x   +       �      i   @           �       1   �   C       M                   <   '   �               �   �   �   �       �   0   G   f   F   �                  �   �   \   �   W   /           #   -   �       �   R   �   �   4      	   &           y       �   5   �      .      r   �   n   
   �      �   _          �   E   �   �   �   �   �   $           U   �   ?   �      �           �   ^       "       t   =   s   N   �          [      c           �   e      z   �      Z   O       �   �   �   w              �       B           a       3   �   �      >    ${(object.name or '').replace('/','_')} ${object.employee_id.name}: Appraisal Confirmed ${object.name} requests an Appraisal %s Goals %s months %s 100 % 25 % 360 Feedback 50 % 75 % <div style="margin: 0px; padding: 0px;">
                    <p style="margin: 0px; padding: 0px; font-size: 13px;">
                        Dear ${ctx.get('employee_to_name', 'employee')},
                        <br/><br/>
                        An appraisal was requested.
                        <br/>
                        Please schedule an appraisal date together.
                        <br/><br/>
                        Thank you!
                        The HR department
                        <br/><br/>
                        % if ctx.get('recipient_users'):
                        <p style="margin: 16px 0px 16px 0px;">
                            <a href="${ctx['url']}" style="background-color:#875A7B; padding: 8px 16px 8px 16px; text-decoration: none; color: #fff; border-radius: 5px;">
                                View Appraisal
                            </a>
                        </p>
                        % endif
                        <br/><br/>
                        <tr><td style="padding:15px 20px 10px 20px;">${(object.signature or '')| safe}</td></tr>
                    </p>
                </div>
             <div style="margin: 0px; padding: 0px;">
                    <p style="margin: 0px; padding: 0px; font-size: 13px;">
                        Dear ${ctx['partner_to_name']},
                        <br/><br/>
                        I wish to request an appraisal.<br/>
                        % if ctx.get('recipient_users'):
                        Here is the link of my appraisal:
                        <p style="margin: 16px 0px 16px 0px;">
                            <a href="${ctx['url']}" style="background-color:#875A7B; padding: 8px 16px 8px 16px; text-decoration: none; color: #fff; border-radius: 5px;">
                                View Appraisal
                            </a>
                        </p>
                        % endif
                        <br/><br/>
                        <tr><td style="padding:15px 20px 10px 20px;">${(object.employee_id.user_id.signature or '')| safe}</td></tr>
                    </p>
                </div>
             <div style="margin: 0px; padding: 0px;">
                    <p style="margin: 0px; padding: 0px; font-size: 13px;">
                        Dear ${ctx['partner_to_name']},
                        <br/><br/>
                        I would like to start an Appraisal for you.

                        % if ctx.get('recipient_users'):
                        <p style="margin: 16px 0px 16px 0px;">
                            <a href="${ctx['url']}" style="background-color:#875A7B; padding: 8px 16px 8px 16px; text-decoration: none; color: #fff; border-radius: 5px;">
                                View Appraisal
                            </a>
                        </p>
                        % endif
                        <br/><br/>
                        <tr><td style="padding:15px 20px 10px 20px;">${(object.signature or '')| safe}</td></tr>
                    </p>
                </div>
             <span class="bg-info">Ready</span> <span class="bg-secondary">Canceled</span> <span class="bg-success">Done</span> <span class="col-3 text-right" attrs="{'invisible': ['|', ('employee_feedback_published', '=', True), ('state', '=', 'new')]}">Unpublished</span>
                                <span class="col-3 text-right" attrs="{'invisible': ['|', ('employee_feedback_published', '=', False), ('state', '=', 'new')]}">Published</span> <span class="col-3 text-right" attrs="{'invisible': ['|', ('manager_feedback_published', '=', True), ('state', '=', 'new')]}">Unpublished</span>
                                <span class="col-3 text-right" attrs="{'invisible': ['|', ('manager_feedback_published', '=', False), ('state', '=', 'new')]}">Published</span> <span class="o_form_label">360 Feedback</span>
                                <span class="fa fa-lg fa-building-o" title="Values set here are company-specific." role="img" aria-label="Values set here are company-specific." groups="base.group_multi_company"/> <span class="o_form_label">Appraisal Plans</span>
                                <span class="fa fa-lg fa-building-o" title="Values set here are company-specific." role="img" aria-label="Values set here are company-specific." groups="base.group_multi_company"/> <span class="o_form_label">Confirmation Email Template</span> <span class="o_form_label">Feedback Templates</span>
                                <span class="fa fa-lg fa-building-o" title="Values set here are company-specific." role="img" aria-label="Values set here are company-specific." groups="base.group_multi_company"/> <span class="o_stat_text">
                            Last Appraisal
                        </span> <span class="o_stat_text">Employee's</span>
                            <span class="o_stat_text">Goals</span> <span class="o_stat_value" attrs="{'invisible': [('meeting_id', '=', False)]}">1 Meeting</span>
                            <span class="o_stat_value" attrs="{'invisible': [('meeting_id', '!=', False)]}">No Meeting</span> <span class="o_stat_value">Last Appraisal</span> <strong><span>Final Interview: </span></strong> Action Needed Active Activities Activity Exception Decoration Activity State Activity Type Icon Add existing contacts... After Appraisal Appraisal Analysis Appraisal Assessment Note Appraisal Confirm Employee Mail Template Appraisal Confirm Manager Mail Template Appraisal Deadline Appraisal Employee Appraisal Employee Feedback Template Appraisal Form to Fill Appraisal Goal Appraisal Manager Feedback Template Appraisal Plan Appraisal Requested Appraisal Sent Appraisal Statistics Appraisal to Confirm and Send Appraisal to start Appraisal: Run employee appraisal Appraisals Appraisals to Process Archived Assessment Note Attachment Count Attachments Author Author of the message. Automatically Generate Appraisals Basic Employee Calendar Event Can See Employee Publish Can See Manager Publish Cancel Cancel Future Appraisals Cancel all appraisals after this date Cancelled Color Companies Company Compose Email Config Settings Configuration Confirm Confirm and send appraisal of %s Confirmed Contents Create Date Create a New Appraisal Create a new appraisal Created by Created on Creation Date Date Deadline Deadline: Delete Department Departure Wizard Description Desired Deadline Display Name Done Dropdown menu Email address of the sender Employee Employee Appraisal Employee Appraisal Plan Employee Feedback Published Employee Feedback Template Employee Name Employee's Name Employees Exceeds expectations Extended Filters... Fill appraisal for <a href="#" data-oe-model="%s" data-oe-id="%s">%s</a> Final Interview Final Interview Date Followers Followers (Channels) Followers (Partners) Font awesome icon e.g. fa-tasks From Future Activities Goals Group By Group by... Icon to indicate an exception activity. If checked, new messages require your attention. If checked, some messages have a delivery error. Image Image 128 In progress Evaluations Interview Is Follower Is Manager Job Position Jobs Configuration Last Appraisal Date Last Modified on Last Updated by Last Updated on Late Late Activities Main Attachment Manager Feedback Manager Feedback Published Mark as Done Meeting Meets expectations Message Delivery error Messages My Appraisals My Goals Needs improvement Next Activity Deadline Next Activity Summary Next Activity Type Next Appraisal Date Number of Actions Number of errors Number of messages which requires an action Number of messages with delivery error Number of unread messages Owner Parent User People I Manage Public Employee Recipients Related Partner Related user name for the resource to manage its access. Reporting Request an Appraisal Responsible User SMS Delivery error Schedule The Final Interview Search Appraisal Send Request Sequence Settings Show all records which has next action date is before today Status based on activities
Overdue: Due date is already passed
Today: Activity date is today
Planned: Future activities. Strongly Exceed Expectations Subject Subject... The date of the last appraisal The date of the next appraisal is computed by the appraisal plan's dates (first appraisal + periodicity). The duration time must be bigger or equal to 1 month. The employee %s arrived %s months ago. An appraisal for %s is created. You can assess %s & determinate the date for '1to1' meeting before %s To Do To Start Today Activities Type of the exception activity on record. Unread Messages Unread Messages Counter Use template User Users Waiting Feedback from Employee/Managers Website Messages Website communication history You arrived %s months ago. Your appraisal is created you can assess yourself here. Your manager will determinate the date for your '1to1' meeting. You cannot delete appraisal which is not in draft or canceled state You will be able to plan an appraisal with your employees, to ask your appraisal with your
            manager, to realize 360° Feedback with the Survey app, to make custom forms and to see the results. Your employee's last appraisal was %s months ago. An appraisal for %s is created. You can assess %s & determinate the date for '1to1' meeting before %s Your last appraisal was %s months ago. Your appraisal is created you can assess yourself here. Your manager will determinate the date for your '1to1' meeting. oe_kanban_text_red text-danger Project-Id-Version: Odoo Server 14.0+e
Report-Msgid-Bugs-To: 
PO-Revision-Date: 2020-12-23 15:12+0100
Last-Translator: 
Language-Team: 
MIME-Version: 1.0
Content-Type: text/plain; charset=UTF-8
Content-Transfer-Encoding: 8bit
Plural-Forms: 
Language: de
X-Generator: Poedit 2.4.2
 ${(object.name or '').replace('/','_')} ${object.employee_id.name}: Beurteilung bestätigt ${objekt.name} fordert eine Beurteilung an %s Ziele %s Monate %s 100 % 25 % 360 Feedback 50 % 75 % <div style="margin: 0px; padding: 0px;">
                    <p style="margin: 0px; padding: 0px; font-size: 13px;">
                        Lieber ${ctx.get('employee_to_name', 'employee')},
                        <br/><br/>
                        Es wurde eine Beurteilung angefordert.
                        <br/>
                        Bitte vereinbaren Sie einen gemeinsamen Termin für die Mitarbeiterbeurteilung.
                        <br/><br/>
                        Wir danken Ihnen!
                        Die Personalabteilung
                        <br/><br/>
                        % if ctx.get('recipient_users'):
                        <p style="margin: 16px 0px 16px 0px;">
                            <a href="${ctx['url']}" style="background-color:#875A7B; padding: 8px 16px 8px 16px; text-decoration: none; color: #fff; border-radius: 5px;">
                                Bewertung ansehen
                            </a>
                        </p>
                        % endif
                        <br/><br/>
                        <tr><td style="padding:15px 20px 10px 20px;">${(object.signature or '')| safe}</td></tr>
                    </p>
                </div> <div style="margin: 0px; padding: 0px;">
                    <p style="margin: 0px; padding: 0px; font-size: 13px;">
                        Guten Tag ${ctx['partner_to_name']},
                        <br/><br/>
                        Ich möchte gerne eine Bewertung erhalten.<br/>
                        % if ctx.get('recipient_users'):
                        Hier ist der Link zu meiner Bewertung:
                        <p style="margin: 16px 0px 16px 0px;">
                            <a href="${ctx['url']}" style="background-color:#875A7B; padding: 8px 16px 8px 16px; text-decoration: none; color: #fff; border-radius: 5px;">
                                Bewertung ansehen
                            </a>
                        </p>
                        % endif
                        <br/><br/>
                        <tr><td style="padding:15px 20px 10px 20px;">${(object.employee_id.user_id.signature or '')| safe}</td></tr>
                    </p>
                </div>
             <div style="margin: 0px; padding: 0px;">
                    <p style="margin: 0px; padding: 0px; font-size: 13px;">
                        Guten Tag ${ctx['partner_to_name']},
                        <br/><br/>
                       Gerne würde ich eine Bewertung mit Ihnen beginnen.

                        % if ctx.get('recipient_users'):
                        <p style="margin: 16px 0px 16px 0px;">
                            <a href="${ctx['url']}" style="background-color:#875A7B; padding: 8px 16px 8px 16px; text-decoration: none; color: #fff; border-radius: 5px;">
                                Bewertung ansehen
                            </a>
                        </p>
                        % endif
                        <br/><br/>
                        <tr><td style="padding:15px 20px 10px 20px;">${(object.signature or '')| safe}</td></tr>
                    </p>
                </div>
             <span class="bg-info">Bereit</span> <span class="bg-secondary">Abgebrochen</span> <span class="bg-success">Erledigt</span> <span class="col-3 text-right" attrs="{'invisible': ['|', ('employee_feedback_published', '=', True), ('state', '=', 'new')]}">Unpublished</span>
                                <span class="col-3 text-right" attrs="{'invisible': ['|', ('employee_feedback_published', '=', False), ('state', '=', 'new')]}">Published</span> <span class="col-3 text-right" attrs="{'invisible': ['|', ('manager_feedback_published', '=', True), ('state', '=', 'new')]}">Unpublished</span>
                                <span class="col-3 text-right" attrs="{'invisible': ['|', ('manager_feedback_published', '=', False), ('state', '=', 'new')]}">Published</span> <span class="o_form_label">360 Feedback</span>
                                <span class="fa fa-lg fa-building-o" title="Hier eingestellte Werte sind firmenspezifisch." role="img" aria-label="Hier eingestellte Werte sind firmenspezifisch." groups="base.group_multi_company"/> <span class="o_form_label">Gutachten-Pläne</span>
                                <span class="fa fa-lg fa-building-o" title="Hier eingestellte Werte sind firmenspezifisch." role="img" aria-label="Hier eingestellte Werte sind firmenspezifisch." groups="base.group_multi_company"/> <span class="o_form_label">Bestätigungs-E-Mail-Vorlage</span> <span class="o_form_label">Feedback-Vorlagen</span>
                                <span class="fa fa-lg fa-building-o" title="Hier eingestellte Werte sind firmenspezifisch." role="img" aria-label="Hier eingestellte Werte sind firmenspezifisch." groups="base.group_multi_company"/> <span class="o_stat_text">
                            Letzte Schätzung
                        </span> <span class="o_stat_text">Mitarbeiter</span>
                            <span class="o_stat_text">Ziele</span> <span class="o_stat_value" attrs="{'invisible': [('meeting_id', '=', False)]}">1 Meeting</span>
                            <span class="o_stat_value" attrs="{'invisible': [('meeting_id', '!=', False)]}">Kein Meeting</span> <span class="o_stat_value">Letzte Bewertung</span> <strong><span>Finales Beurteilungsgespräch: </span></strong> Aktion notwendig Aktiv Aktivitäten Aktivität Ausnahme-Dekoration Status der Aktivität Aktivitäts-Typ-Icon Bestehende Kontakte hinzufügen … Nach Bewertung Statistik Beurteilungen Beurteilung Beurteilungshinweis Beurteilung bestätigen Mitarbeiter Mail Vorlage Beurteilung Bestätigen Manager Mail Vorlage Beurteilung Frist Beurteilung Mitarbeiter Beurteilung Mitarbeiter-Feedback Vorlage Bewertungsformular ausfüllen Beurteilungsziel Beurteilung Manager Feedback-Vorlage Beurteilungsplan Beurteilung angefordert Beurteilung versendet Bewertungsauswertungen Beurteilung zum Bestätigen und Senden anstehende Beurteilungen Beurteilung: Mitarbeiterbeurteilung durchführen Bewertungen durchzuführende Beurteilungen Archiviert Bewertung Hinweis # Anhänge Dateianhänge Autor Autor der Nachricht. Automatisch Beurteilungen generieren Basis-Mitarbeiter Kalender Veranstaltung Kann sehen Mitarbeiter veröffentlichen Kann sehen Manager veröffentlichen Abbrechen Zukünftige Beurteilungen stornieren Stornieren Sie alle Begutachtungen nach diesem Datum Abgebrochen Farbe Unternehmen Unternehmen E-Mail schreiben Konfiguration  Konfiguration Bestätigen Beurteilung von %s bestätigen und senden Bestätigt Inhalte Erstellt am Eine neue Beurteilung erstellen Erstellen Sie eine neue Bewertung Erstellt von Erstellt am Erzeugt am Datum Frist Frist: Löschen Abteilung Abreise Wizard Beschreibung Gewünschte Deadline Anzeigename Erledigt Dropdownmenu E-Mail Adresse des Absenders Mitarbeiter Mitarbeiter Beurteilung Mitarbeiterbeurteilungsplan Mitarbeiter-Feedback veröffentlicht Mitarbeiter-Feedback-Vorlage Mitarbeitername Mitarbeiter Name Personal Übertrifft die Erwartungen Erweiterte Filter... Beurteilung ausfüllen für <a href="#" data-oe-model="%s" data-oe-id="%s">%s</a> Abschlussbefragung Schlussgespräch Abonnenten Abonnenten (Kanäle) Abonnenten (Partner) FontAwesome Icon, z.B. fa-tasks Von Anstehende Aktivitäten Ziele Gruppieren nach Gruppierung ... Icon, um eine Ausnahmeaktivität anzuzeigen. Falls markiert, benötigen neue Nachrichten Ihre Kenntnisnahme. Das Senden mancher Nachrichten ist fehlgeschlagen wenn dieses Fenster angekreuzt ist. Bild Bild 128 Beurteilungen in Bearbeitung Fragebogen Ist ein Abonnent Ist Manager Beruf Jobs Konfiguration Letztes Beurteilungsdatum Zuletzt geändert am Zuletzt aktualisiert durch Zuletzt aktualisiert am Verspätet Verspätete Aktivitäten Hauptanhänge Manager Feedback Manager-Feedback veröffentlicht Als erledigt markieren Meeting Erfüllt die Erwartungen Error beim senden der Nachricht Nachrichten Meine Einschätzungen Meine Ziele Verbesserungsbedürftig Nächste Aktivitätsfrist Zusammenfassung nächste Aktion Nächster Aktivitätstyp Nächstes Beurteilungsdatum Anzahl der Aktionen # Fehler Anzahl der Nachrichten, die eine Aktion erfordern Anzahl der Nachrichten mit einem Fehler beim Senden. Anzahl ungelesener Nachrichten Besitzer Übergeordneter Benutzer Meine Mitarbeiter Öffentlicher Mitarbeiter Empfänger Zugehöriger Partner Der mit der Ressource verbunden Benutzer für die Zugriffsberechtigung Berichtswesen Beurteilung anfordern Manager Veranstaltung SMS Zustellungsfehler Terminiere die Abschlussbefragung Suche Beurteilung Anfrage senden Reihenfolge Einstellungen Alle Datensätze mit vor heute geplanten Aktionen anzeigen Status basierend auf Aktivitäten
Überfällig: Fälligkeitsdatum bereits überschritten
Heute: Aktivität besitzt heutiges Datum
Geplant: anstehende Aktivitäten. Starke Überschreitung der Erwartungen Betreff Betreff... Das Datum der letzten Begutachtung Das Datum der nächsten Beurteilung wird automatisch errechnet (Erste Beurteilung + Intervall) Die Zeitdauer muss größer oder gleich 1 Monat sein. Der Mitarbeiter %s ist vor %s Monaten eingetroffen. Eine Beurteilung für %s ist erstellt. Sie können %s beurteilen & den Termin für das '1zu1' Meeting vor %s bestimmen Zu erledigen Zu Beginn Heutige Aktivitäten Typ der Ausnahmeaktivität im Datensatz. Ungelesene Nachrichten Zähler der ungelesenen Nachrichten Benutze Vorlage Benutzer Benutzer Warten auf Feedback von Mitarbeitern/Managern Website-Nachrichten Website-Kommunikationshistorie Sie sind vor %s Monaten angekommen. Ihre Beurteilung ist erstellt, hier können Sie sich selbst einschätzen. Ihr Vorgesetzter legt den Termin für Ihr "1zu1"-Gespräch fest. Sie können keine Beurteilung löschen, die sich nicht im Entwurfs- oder Stornostatus befindet Sie werden in der Lage sein, eine Beurteilung mit Ihren Mitarbeitern zu planen, Ihre Beurteilung mit Ihrem
            Manager zu führen, 360°-Feedback mit der Umfrage-App zu realisieren, eigene Formulare zu erstellen und die Ergebnisse zu sehen. Die letzte Beurteilung Ihres Mitarbeiters war vor %s Monaten. Eine Beurteilung für %s wird erstellt. Sie können %s beurteilen & den Termin für das '1zu1'-Gespräch vor %s festlegen Ihre letzte Beurteilung ist %s Monate her. Ihre Beurteilung ist erstellt, hier können Sie sich selbst beurteilen. Ihr Vorgesetzter legt den Termin für Ihr "1zu1"-Gespräch fest. oe_kanban_text_red text-danger 