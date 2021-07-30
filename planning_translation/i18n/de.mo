��    �      �  �   �	      �  9   �  �  #  -  �  U   $  \   h$  D   �$  f   
%  [   q%  N   �%  "   &    ?&  E   Y'  �   �'     4(     G(  "   [(     ~(     �(  J   �(     )  
   )     $)  ;   7)  I   s)     �)     �)     �)     �)  7   *     @*     L*  "   T*     w*     �*  	   �*     �*     �*     �*     �*     �*      �*  c   +  
   j+  
   u+     �+     �+  4   �+  H   �+  @   ,     Z,  
   a,     l,     t,     �,  �   �,     |-  	   �-     �-  	   �-  L   �-  3   �-     (.  )   1.     [.     u.     �.     �.     �.     �.     �.     �.     �.     �.     �.     �.  	   /     /  P   !/     r/  \   �/     O0     c0     x0  *   �0     �0     �0     �0     �0     	1      1  -   :1  D   h1  .   �1     �1  	   �1     �1     �1     2     2     2     2     $2     -2     32     ;2  	   J2  
   T2  8   _2     �2     �2     �2  	   �2     �2     �2     �2     �2     �2     �2  D   �2  5   43     j3     s3     |3  
   �3     �3     �3     �3     �3  4   �3     	4  6   4  
   S4  $   ^4  	   �4     �4  0   �4     �4     �4     �4  1   �4     5      5  
   &5  9   15  4   k5  #   �5  ,   �5     �5  #   6     46     C6    F6  F   _7  �  �7  :  {?  [   �N  f   O  F   yO  r   �O  \   3P  O   �P  '   �P    Q  L   'R  �   tR     S     %S  &   9S     `S     ~S  Y   �S     �S     T     %T  K   <T  ]   �T     �T     �T     U     U  L   8U     �U  
   �U  )   �U     �U     �U     �U     �U     �U     V  /   V     JV  4   cV  �   �V     %W     2W     >W     DW  W   XW  [   �W  R   X     _X  	   hX  	   rX     |X     �X  H  �X     �Y     �Y     Z     Z  a   Z  J   yZ     �Z  3   �Z     [     [     *[     :[  
   C[     N[     k[  
   o[     z[     �[     �[     �[     �[     �[  ~   �[  �   w\  x   -]     �]     �]     �]  3   �]  0   0^     a^     ~^     �^     �^  '   �^  7   �^  W   &_  E   ~_     �_     �_  	   �_     �_     `     `  	   "`     ,`     4`     <`     C`     T`     n`     ~`  F   �`     �`     �`     �`     �`     a     a  	   a     "a     3a     :a  Z   Fa  >   �a     �a     �a     �a     b     b     b     6b     Kb  @   [b     �b  ?   �b  
   �b  ,   �b     *c     3c  >   Qc     �c     �c     �c  ;   �c     �c     �c     �c  >   d  B   Ld  &   �d  1   �d  (   �d  -   e     ?e     Re     o       �                 m       b   '   D       �   ~   O   "   �   v         
   A   �   �             	       �   G       Q   E       |          }   y   7   �       F       :   x             W       a   V       {      )   8   �   P   \   t                 �   �   [           @   �   (      !   R   Z           w   k       n           g   1   $   �   l              S   N                 /   Y   9       �   ?   &              6   C       `      ^   =   �              4   �       �   ,                *   j   p           z   �       �   I       3   �       �           d   B       h       %   J   �       -   �   i   #   u   �       L      _   M   2   H               ;   ]   +   .   <           q          K   �          �      r   c          5       >   U   e              f   0   s   X       T           <b class="tip_title">Tip: Record your planning faster</b> <div>
                    <p>
                    % if ctx.get('employee'):
                        Dear ${ctx['employee'].name},
                    % else:
                        Hello,
                    % endif
                        <br/><br/>
                    % if ctx.get('assigned_new_shift'):
                        You have been assigned new shifts:
                    % else:
                        Please, find your planning for the following period:
                    % endif
                    </p>
                    <br/>

                    <table style="table-layout: fixed; width: 80%; margin: auto;">
                        <tr>
                            <th style="padding: 5px;text-align: left; width: 15%;">From</th>
                            <td style="padding: 5px;">${format_date(ctx.get('start_datetime'))}</td>
                        </tr>
                        <tr>
                            <th style="padding: 5px;text-align: left; width: 15%;">To</th>
                            <td style="padding: 5px;">${format_date(ctx.get('end_datetime'))}</td>
                        </tr>
                    </table>

                    % if ctx.get('planning_url'):
                        <div style="margin: 15px;">
                            <a href="${ctx.get('planning_url')}" target="_blank" style="padding: 5px 10px; color: #FFFFFF; text-decoration: none; background-color: #875A7B; border: 1px solid #875A7B; border-radius: 3px">View Your Planning</a>
                        </div>
                    % endif

                    % if ctx.get('slot_unassigned_count'):
                    <div>
                        <p>There are new open shifts available. Please, assign yourself if you are available.</p>
                    </div>
                    % endif

                    % if ctx.get('message'):
                        <p>${ctx['message']}</p>
                    % endif
                </div>
             <div>
                    <p>Dear ${ctx.employee_name or ''},<br/><br/></p>
                    % if ctx.get('open_shift_available')
                    <p>A new open shift is available:</p>
                    % else
                    <p>You have been assigned the following schedule:</p>
                    % endif
                    <br/>
                    <table style="table-layout: fixed; width: 80%; margin: auto;">
                        <tr>
                            <th style="padding: 5px;text-align: left; width: 15%;">From</th>
                            <td style="padding: 5px;">${ctx.get('start_datetime')}</td>
                        </tr>
                        <tr>
                            <th style="padding: 5px;text-align: left; width: 15%;">To</th>
                            <td style="padding: 5px;">${ctx.get('end_datetime')}</td>
                        </tr>
                        % if object.role_id
                        <tr>
                            <th style="padding: 5px;text-align: left; width: 15%;">Role</th>
                            <td style="padding: 5px;">${object.role_id.name or ''}</td>
                        </tr>
                        % endif
                        % if object.project_id
                        <tr>
                            <th style="padding: 5px;text-align: left; width: 15%;">Project</th>
                            <td style="padding: 5px;">${object.project_id.name or ''}</td>
                        </tr>
                        % endif
                        % if object.task_id
                        <tr>
                            <th style="padding: 5px;text-align: left; width: 15%;">Task</th>
                            <td style="padding: 5px;">${object.task_id.name or ''}</td>
                        </tr>
                        % endif
                        % if object.name
                        <tr>
                            <th style="padding: 5px;text-align: left; width: 15%;">Note</th>
                            <td style="padding: 5px;">${object.name or ''}</td>
                        </tr>
                        % endif
                    </table>
                    % if ctx.get('available_link')
                    <div>
                        <br/>
                        <span>Please, assign yourself if you are available.</span>
                    </div>
                    % endif
                    <div style="text-align: center">
                        % if ctx.get('unavailable_link')
                        <div style="display: inline-block; margin: 15px; text-align: center">
                            <a href="${ctx.unavailable_link}" target="_blank" style="padding: 5px 10px; color: #875A7B; text-decoration: none; background-color: #FFFFFF; border: 1px solid #FFFFFF; border-radius: 3px">I am unavailable</a>
                        </div>
                        % endif
                        % if ctx.get('available_link')
                        <div style="display: inline-block; margin: 15px; text-align: center">
                            <a href="${ctx.available_link}" target="_blank" style="padding: 5px 10px; color: #875A7B; text-decoration: none; background-color: #FFFFFF; border: 1px solid #FFFFFF; border-radius: 3px">Assign me this shift</a>
                        </div>
                        % endif
                        % if ctx.get('link')
                        <div style="display: inline-block; margin: 15px; text-align: center">
                            <a href="${ctx.link}" target="_blank" style="padding: 5px 10px; color: #FFFFFF; text-decoration: none; background-color: #875A7B; border: 1px solid #875A7B; border-radius: 3px">View Planning</a>
                        </div>
                        % endif
                    </div>
                </div>
             <i class="fa fa-check-circle text-success"/> This shift is no longer assigned to you. <i class="fa fa-check-circle text-success"/> You were successfully assigned this open shift. <i class="fa fa-clock-o" role="img" aria-label="Date" title="Date"/> <i class="fa fa-exclamation-circle text-warning"/> This shift is already assigned to another employee. <i class="fa fa-long-arrow-right mx-2 oe_edit_only" aria-label="Arrow icon" title="Arrow"/> <i class="fa fa-long-arrow-right mx-2" aria-label="Arrow icon" title="Arrow"/> <span aria-label="Close">×</span> <span attrs="{'invisible': ['|', ('employee_id', '=', False), ('work_email', '!=', False)]}" class="fa fa-exclamation-triangle text-danger" role="alert" title="There is no work email address configured for this employee. You will not be able to send the planning to them."> </span> <span class="align-middle">for this employee at the same time.</span> <span class="o_form_label" name="project_forecast_msg">
                                    Recurring Shifts
                                </span> <span>Weeks</span> <span>months</span> <strong>Allocated Hours: </strong> <strong>Start Date: </strong> <strong>Stop Date: </strong> A recurrence repeating itself until a certain date must have its limit set ASSIGN ME THIS SHIFT Add record Additional message Additional message displayed in the email sent to employees All subsequent shifts will be deleted. Are you sure you want to continue? Allocated Hours Allocated Time (%) Allocation Type Allow Template Creation An shift must be in the same company as its recurrency. By Employee By Role Can Employee Un-Assign Themselves? Collapse rows Color Companies Company Config Settings Configuration Confirm Slots Deletion Copy previous week Create shifts to get statistics. Create your first shift by clicking on Add. Alternatively, you can use the (+) button on each cell. Created by Created on Date Default Planning Role Define the different roles filled by your employees. Delay for the rate at which recurring shift should be generated in month Delay for the rate at which recurring shifts should be generated Delete Department Discard Display Name Documentation Drag a shift to another day to reschedule it, or to another row to reassign the shift. If the shift was published, the user will automatically be notified of the change. Press CTRL (or Cmd on Mac) while dragging a shift to duplicate it. Dropdown menu Edit Slot Employee Employees Employees who will receive planning by email if you click on publish & send. Encode your shifts in one click by using templates. End Date Error: each employee token must be unique Every %s week(s) until %s Expand rows Extra Message Forecast Forever Forever, every %s week(s) From Future Give depth to your Group By Hours per Employee I Am Unavailable I Take It I am unavailable If checked, it means that the shift contains has changed since its last publish. If checked, this means the planning entry has been sent to the employee. Modifying the planning entry will mark it as not sent. If set, the recurrence stop at that date. Otherwise, the recurrence is applied indefinitely. Include Open Shifts Includes Open Shifts Is The Shift Sent Is This Shift Assigned To The Current User Is This Shift In The Past? Last Generated End Date Last Modified on Last Updated by Last Updated on Let Employee Unassign Themselves Let employees unassign themselves from shifts Let your employees un-assign themselves from shifts when unavailable Let's start managing your employees' schedule! My Planning My Shifts My Team No data yet! Note Open Shifts Past Period Planning Plans Publish Publish & Send Published Recurrency Related user name for the resource to manage its access. Repeat Repeat Every Repeat Until Reporting Role Roles Save Schedule Send Send schedule Send the schedule and mark the shifts as published. Congratulations! Send the schedule to your employees once it is ready. Sequence Settings Shift Shift List Shift Template Shift Template Form Shift Template List Shift Templates Shift end date should be greater than its start date Shifts in conflict Some changes were made since this shift was published. Start Date Start hour must be a positive number Stop Date Template Autocomplete The company does not allow you to self unassign. To Unpublished Until Up to which date should the plannings be repeated User Weeks Work Email You can not assign yourself to an already assigned shift. You can not unassign another employee than yourself. You cannot have a negative duration You cannot have a start hour greater than 24 You cannot have negative shift You don't the right to self assign. other shift(s) to Project-Id-Version: Odoo Server 14.0+e
Report-Msgid-Bugs-To: 
PO-Revision-Date: 2021-01-11 08:30+0100
Last-Translator: 
Language-Team: 
MIME-Version: 1.0
Content-Type: text/plain; charset=UTF-8
Content-Transfer-Encoding: 8bit
Plural-Forms: 
Language: de
X-Generator: Poedit 2.4.2
 <b class="tip_title">Tipp: Zeichnen Sie Ihre Planung schneller auf</b> <div>
                    <p>
                    % if ctx.get('employee'):
                        ${ctx['employee'].name},
                    % else:
                        Hallo,
                    % endif
                        <br/><br/>
                    % if ctx.get('assigned_new_shift'):
                        Es wurden Ihnen neue Schichten zugewiesen:
                    % else:
                        Bitte suchen Sie Ihre Planung für den folgenden Zeitraum:
                    % endif
                    </p>
                    <br/>

                    <table style="table-layout: fixed; width: 80%; margin: auto;">
                        <tr>
                            <th style="padding: 5px;text-align: left; width: 15%;">Von</th>
                            <td style="padding: 5px;">${format_date(ctx.get('start_datetime'))}</td>
                        </tr>
                        <tr>
                            <th style="padding: 5px;text-align: left; width: 15%;">Bis</th>
                            <td style="padding: 5px;">${format_date(ctx.get('end_datetime'))}</td>
                        </tr>
                    </table>

                    % if ctx.get('planung_url'):
                        <div style="margin: 15px;">
                            <a href="${ctx.get('planung_url')}" target="_blank" style="padding: 5px 10px; color: #FFFFFF; text-decoration: none; background-color: #875A7B; border: 1px solid #875A7B; border-radius: 3px">Ihre Planung ansehen</a>
                        </div>
                    % endif

                    % if ctx.get('slot_unassigned_count'):
                    <div>
                        <p>Es sind neue offene Schichten verfügbar. Bitte weisen Sie sich zu, wenn Sie verfügbar sind.</p>
                    </div>
                    % endif

                    % if ctx.get('message'):
                        <p>${ctx['message']}</p>
                    % endif
                </div>
             <div>
                    <p>Guten Tag ${ctx.employee_name or ''},<br/><br/></p>
                    % if ctx.get('open_shift_available')
                    <p>Eine neue zu besetzende Schicht ist verfügbar:</p>
                    % else
                    <p>Sie sind der folgenden Schicht zugewiesen worden:</p>
                    % endif
                    <br/>
                    <table style="table-layout: fixed; width: 80%; margin: auto;">
                        <tr>
                            <th style="padding: 5px;text-align: left; width: 15%;">Von</th>
                            <td style="padding: 5px;">${ctx.get('start_datetime')}</td>
                        </tr>
                        <tr>
                            <th style="padding: 5px;text-align: left; width: 15%;">bis</th>
                            <td style="padding: 5px;">${ctx.get('end_datetime')}</td>
                        </tr>
                        % if object.role_id
                        <tr>
                            <th style="padding: 5px;text-align: left; width: 15%;">Rolle</th>
                            <td style="padding: 5px;">${object.role_id.name or ''}</td>
                        </tr>
                        % endif
                        % if object.project_id
                        <tr>
                            <th style="padding: 5px;text-align: left; width: 15%;">Projekt</th>
                            <td style="padding: 5px;">${object.project_id.name or ''}</td>
                        </tr>
                        % endif
                        % if object.task_id
                        <tr>
                            <th style="padding: 5px;text-align: left; width: 15%;">Aufgabe</th>
                            <td style="padding: 5px;">${object.task_id.name or ''}</td>
                        </tr>
                        % endif
                        % if object.name
                        <tr>
                            Bemerkung
                            <td style="padding: 5px;">${object.name or ''}</td>
                        </tr>
                        % endif
                    </table>
                    % if ctx.get('available_link')
                    <div>
                        <br/>
                        <span>Bitte teilen Sie sich ein, falls Sie verfügbar sind.</span>
                    </div>
                    % endif
                    <div style="text-align: center">
                        % if ctx.get('unavailable_link')
                        <div style="display: inline-block; margin: 15px; text-align: center">
                            <a href="${ctx.unavailable_link}" target="_blank" style="padding: 5px 10px; color: #875A7B; text-decoration: none; background-color: #FFFFFF; border: 1px solid #FFFFFF; border-radius: 3px">Ich bin nicht verfügbar</a>
                        </div>
                        % endif
                        % if ctx.get('available_link')
                        <div style="display: inline-block; margin: 15px; text-align: center">
                            <a href="${ctx.available_link}" target="_blank" style="padding: 5px 10px; color: #875A7B; text-decoration: none; background-color: #FFFFFF; border: 1px solid #FFFFFF; border-radius: 3px">Bitte teilen Sie mich für diese Schicht ein</a>
                        </div>
                        % endif
                        % if ctx.get('link')
                        <div style="display: inline-block; margin: 15px; text-align: center">
                            <a href="${ctx.link}" target="_blank" style="padding: 5px 10px; color: #FFFFFF; text-decoration: none; background-color: #875A7B; border: 1px solid #875A7B; border-radius: 3px">Plan ansehen</a>
                        </div>
                        % endif
                    </div>
                </div>
             <i class="fa fa-check-circle text-success"/> Diese Schicht ist Ihnen nicht mehr zugewiesen. <i class="fa fa-check-circle text-success"/> Sie wurden erfolgreich dieser offenen Schicht zugeordnet. <i class="fa fa-clock-o" role="img" aria-label="Datum" title="Datum"/> <i class="fa fa-exclamation-circle text-warning"/> Diese Schicht ist bereits einem anderen Mitarbeiter zugewiesen. <i class="fa fa-long-arrow-right mx-2 oe_edit_only" aria-label="Pfeilsymbol" title="Pfeil"/> <i class="fa fa-long-arrow-right mx-2" aria-label="Pfeilsymbol" title="Pfeil"/> <span aria-label="Schließen">×</span> <span attrs="{'unsichtbar': ['|', ('employee_id', '=', False), ('work_email', '!=', False)]}" class="fa fa-exclamation-triangle text-danger" role="alert" title="Für diesen Mitarbeiter ist keine Arbeits-E-Mail-Adresse konfiguriert. Sie können die Planung nicht an ihn senden."> </span> <span class="align-middle">für diesen Mitarbeiter zur gleichen Zeit.</span> <span class="o_form_label" name="project_forecast_msg">
                                    Wiederkehrende Schichten
                                </span> <span>Wochen</span> <span>Monate</span> <strong>Zugewiesene Stunden: </strong> <strong>Startdatum: </strong> <strong>Enddatum: </strong> Eine Rekurrenz, die sich bis zu einem bestimmten Datum wiederholt, muss ihre Grenze haben WEISE MIR DIESE SCHICHT ZU Datensatz hinzufügen Zusätzliche Nachricht Zusätzliche Nachricht, die in der E-Mail an die Mitarbeiter angezeigt wird Alle nachfolgenden Schichten werden gelöscht. Sind Sie sicher, dass Sie fortfahren möchten? Zugewiesene Stunden Zugewiesene Zeit (%) Anspruchsart Vorlagenerstellung zulassen Eine Schicht muss sich in der gleichen Firma befinden wie ihre Wiederholung. Nach Mitarbeiter Nach Rolle Können sich Mitarbeiter selbst abmelden? Zeilen komprimieren Farbe Unternehmen Unternehmen Konfiguration  Konfiguration Bestätigen Sie die Löschung von Steckplätzen Vorherige Woche kopieren Erstellen Sie Schichten, um Statistiken zu erhalten. Erstellen Sie Ihre erste Schicht, indem Sie auf Hinzufügen klicken. Alternativ können Sie die Schaltfläche (+) auf jeder Zelle verwenden. Erstellt von Erstellt am Datum Standard Plan-Rolle Definieren Sie die verschiedenen Rollen, die von Ihren Mitarbeitern ausgefüllt werden. Verzögerung für die Rate, mit der die wiederkehrende Schicht im Monat erzeugt werden soll Verzögerung für die Rate, mit der wiederkehrende Schichten erzeugt werden sollen Löschen Abteilung Verwerfen Anzeigename Dokumentation Ziehen Sie eine Schicht auf einen anderen Tag, um sie neu zu planen, oder auf eine andere Zeile, um die Schicht neu zuzuordnen. Wenn die Schicht veröffentlicht wurde, wird der Benutzer automatisch über die Änderung benachrichtigt. Drücken Sie STRG (oder Cmd auf Mac), während Sie eine Schicht ziehen, um sie zu duplizieren. Dropdownmenu Steckplatz bearbeiten Mitarbeiter Personal Mitarbeiter, die die Planung per E-Mail erhalten, wenn Sie auf Veröffentlichen & Senden klicken. Codieren Sie Ihre Schichten mit einem Klick, indem Sie Vorlagen verwenden. Enddatum Fehler: jedes Mitarbeiter-Token muss eindeutig sein Alle %s Woche(n) bis %s Zeilen erweitern Extra Nachricht Prognose Für immer Für immer, alle %s Woche(n) Von Zukünftig Geben Sie Tiefe in Ihr Gruppieren nach Stunden pro Mitarbeiter Ich bin nicht verfügbar Ich nehme es Ich bin nicht verfügbar Wenn dieses Kontrollkästchen aktiviert ist, bedeutet es, dass die Schicht seit der letzten Veröffentlichung geändert wurde. Wenn das Häkchen gesetzt ist, bedeutet dies, dass die Planungsvorgabe an den Mitarbeiter gesendet wurde. Wenn Sie die Planungseingabe ändern, wird sie als nicht gesendet markiert. Wenn gesetzt, endet die Wiederholung an diesem Datum. Andernfalls wird die Wiederholung auf unbestimmte Zeit angewendet. Offene Schichten einbeziehen Enthält offene Schichten Wird die Verschiebung gesendet Ist diese Schicht dem aktuellen Benutzer zugewiesen Gehört diese Verschiebung der Vergangenheit an? Letztes generiertes Enddatum Zuletzt geändert am Zuletzt aktualisiert durch Zuletzt aktualisiert am Mitarbeiter sich selbst abmelden lassen Mitarbeitern gestatten, sich aus Schichten auszutragen. Lassen Sie Ihre Mitarbeiter sich von Schichten abmelden, wenn sie nicht verfügbar sind Lassen Sie uns beginnen, den Zeitplan Ihrer Mitarbeiter zu verwalten! Mein Schichtplan Meine Schichten Mein Team Noch keine Daten vorhanden! Notiz Offene Schichten Vergangen Periode Planung Pläne Veröffentlichen Veröffentlichen & Senden Veröffentlicht Häufigkeit Der mit der Ressource verbunden Benutzer für die Zugriffsberechtigung Wiederholen Wiederhole alle Wiederholen bis Berichtswesen Rolle Rollen Speichern Ausführungsplan Senden Plan senden Senden Sie den Zeitplan und markieren Sie die Schichten als veröffentlicht. Glückwunsch! Senden Sie den Plan an Ihre Mitarbeiter, sobald er fertig ist. Reihenfolge Einstellungen Schicht Schichtliste Schichtvorlage Schichtvorlagenformular Schichtvorlagenliste Schichtvorlagen Das Enddatum der Schicht sollte größer als das Startdatum sein Schichten im Konflikt Die Schicht wurde seit der letzten Veröffentlichung geändert. Startdatum Die Startstunde muss eine positive Zahl sein Enddatum Vorlage Autovervollständigen Das Unternehmen erlaubt Ihnen nicht, sich selbst zu entfernen. Bis Unveröffentlicht Bis Bis zu welchem Datum sollen die Planungen wiederholt werden Benutzer Wochen E-Mail (geschäftlich) Sie können sich keiner bereits zugewiesenen Schicht zuweisen. Sie können keinen anderen Mitarbeiter als sich selbst entfernen.  Sie können keine negative Dauer haben Sie können keine Startzeit größer als 24 haben Sie können keine negative Schicht haben Sie sind nicht befugt sich selbst zuzuweisen. andere Schicht(en) bis 