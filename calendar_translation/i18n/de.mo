��    �      �  %  �      0  "   1  %   T  P   z  0   �     �       �  2    %  /  "7     RH  *   fH     �H     �H     �H     �H  z   �H     <I  
   CI     NI     WI     eI     mI  
   ~I     �I     �I     �I  	   �I     �I  
   �I     �I     �I     �I     �I     �I     �I     J     /J     >J     RJ     cJ  x   |J     �J     K     	K  
   K  
   K     %K     *K     8K     <K     IK     VK     [K     cK     lK     xK     �K     �K     �K     �K     �K     �K     �K     �K     �K     L     L     "L     2L     JL     SL     \L     eL  	   nL     xL     �L     �L     �L  
   �L     �L     �L  
   �L     �L  5   M     9M  	   KM     UM     jM     M     �M     �M     �M  	   �M     �M     �M     �M     �M     �M  0   �M  0   
N  o   ;N     �N  
   �N     �N     �N     �N  %   �N     O     $O     0O     IO     NO     _O     oO  3   O  3   �O     �O     �O     P     P  J   P     `P     pP     �P     �P     �P     �P     �P     �P     �P     �P     �P     �P     �P     �P     �P     Q      Q     -Q     CQ     ZQ     tQ     �Q     �Q     �Q  +   �Q  &   �Q     R     1R     KR     _R     gR     uR     }R      �R     �R  
   �R     �R  	   �R     �R     �R  	   �R     S     S     S  #   &S     JS     YS     eS     iS     rS     �S     �S     �S  	   �S     �S  
   �S  9   �S     T  &   T     CT  8   HT     �T     �T     �T     �T     �T     �T  j   �T  �   "U  K   �U  9   V      QV     rV     xV     |V     �V     �V     �V     �V     �V  	   �V     �V     �V     �V     �V     �V     �V  	   �V     W     	W     W     W  )   $W     NW    bW  $   {X  (   �X  Q   �X  1   Y      MY     nY  �  �Y  [  �k  m  �}     O�  8   e�     ��  
   ��     ��     Ə  �   ֏     `�     f�  
   s�     ~�  
   ��     ��     ��  
   ��  
   ̐     א  
   �     �     �     �     !�     (�     .�     7�  &   F�     m�     �     ��     ��     ��  �   ё  	   }�     ��     ��     ��     ��     ��     ��     Ē     Ȓ     ג     �     �     �     ��     �     �     �     (�     9�     R�     Z�     `�  #   q�  #   ��     ��     ��     ғ  !   �     �     �     �     $�     -�     5�     D�     [�     z�     ��     ��     Ȕ  	   ֔     ��  :   �     "�  
   6�     A�     V�  
   k�     v�     ~�  
   ��     ��     ��     ��     ��  *   ��     �  ?   �  U   0�  \   ��  	   �  	   �     ��     �     �  $   %�     J�     V�     g�     ��     ��     ��     ��  ,   ӗ  4    �     5�     9�     K�     Y�  L   ]�     ��     ��     ʘ     ט     �     �     �     �     #�     &�  
   -�     8�     ?�     N�  !   _�     ��     ��     ��     ��     ә     �     �     �     .�  1   7�  4   i�     ��     ��     ך     �     ��     �  
   �  #   �     =�     K�     X�     g�     z�     ��     ��     ��     ��     Л  &   ��     �     �     ,�     /�     7�     T�     d�     l�     ��     ��  
   ��  H   ��     �      �     �  F   �     ^�     f�     i�     q�     ��     ��  �   ��  �   '�  U   ٞ  2   /�  &   b�     ��     ��  
   ��     ��     ��     ��     ��     ş     ɟ     П     ؟  #   �     �     �      �     #�  	   ,�     6�     =�     C�  .   Y�     ��         ?   (   7   e   �       I   ]      0   P       �          c       l   �       �               m   a   =      �   �   �       z   �   2   �       �       �   ;   �   �   g   �           _   �   �   ^   K                C   )   Z   M   -   �   �               %       �   6   �          �   �   �       q   f   '   �   �   �   �       �   �   �   �   i       /   �          &   k           �   X         5   +                   �   �   �   [      h   �          U   :   �               �   �       �   w           \   E   �   �   S   �                      R   9   4   {           �   �       <      �   �                  y           �   B      �           v       b   @   	       j   �   �   �   �   `           H   �   �   V   �   �   1   �   ~   �   �   �   O   �   N      �       �   o   J   G   �   �   �          �   3   �       Y          #          F   Q       �   L   .   �   "   t           x           �       �       T       $   ,   �   �      
       �           �   D      �   p   |       �          �      W   �   r            >   s   8   �       u   *   A   �       }      d   �      n   �       !   �           �   �    ${object.event_id.name} - Reminder ${object.event_id.name}: Date updated %(date_start)s at %(time_start)s To
 %(date_end)s at %(time_end)s (%(timezone)s) %(day)s at (%(start)s To %(end)s) (%(timezone)s) %s has accepted invitation %s has declined invitation <div>
    % set colors = ctx.get('colors', {})
    % set recurrent = object.recurrence_id and not ctx['ignore_recurrence']
    <p>
        Hello ${object.common_name},<br/><br/>
        ${object.event_id.user_id.partner_id.name} invited you to the ${object.event_id.name} meeting of ${object.event_id.user_id.company_id.name}.
    </p>
    <div style="text-align: center; margin: 16px 0px 16px 0px;">
        % set target = 'recurrence' if recurrent else 'meeting'
        <a href="/calendar/${target}/accept?token=${object.access_token}&amp;id=${object.event_id.id}" style="padding: 5px 10px; color: #FFFFFF; text-decoration: none; background-color: #875A7B; border: 1px solid #875A7B; border-radius: 3px">
            Accept</a>
        <a href="/calendar/${target}/decline?token=${object.access_token}&amp;id=${object.event_id.id}" style="padding: 5px 10px; color: #FFFFFF; text-decoration: none; background-color: #875A7B; border: 1px solid #875A7B; border-radius: 3px">
            Decline</a>
        <a href="/calendar/meeting/view?token=${object.access_token}&amp;id=${object.event_id.id}" style="padding: 5px 10px; color: #FFFFFF; text-decoration: none; background-color: #875A7B; border: 1px solid #875A7B; border-radius: 3px">
            View</a>
    </div>
    <table border="0" cellpadding="0" cellspacing="0"><tr>
        % if not recurrent:
        <td width="130px;">
            <div style="border-top-left-radius: 3px; border-top-right-radius: 3px; font-size: 12px; border-collapse: separate; text-align: center; font-weight: bold; color: #ffffff; min-height: 18px; background-color: #875A7B; border: 1px solid #875A7B;">
                ${object.event_id.get_interval('dayname', tz=object.partner_id.tz if not object.event_id.allday else None)}
            </div>
            <div style="font-size: 48px; min-height: auto; font-weight: bold; text-align: center; color: #5F5F5F; background-color: #F8F8F8; border: 1px solid #875A7B;">
                ${object.event_id.get_interval('day', tz=object.partner_id.tz if not object.event_id.allday else None)}
            </div>
            <div style="font-size: 12px; text-align: center; font-weight: bold; color: #ffffff; background-color: #875A7B;">
                ${object.event_id.get_interval('month', tz=object.partner_id.tz if not object.event_id.allday else None)}
            </div>
            <div style="border-collapse: separate; color: #5F5F5F; text-align: center; font-size: 12px; border-bottom-right-radius: 3px; font-weight: bold; border: 1px solid #875A7B; border-bottom-left-radius: 3px;">
                ${not object.event_id.allday and object.event_id.get_interval('time', tz=object.partner_id.tz) or ''}
            </div>
        </td>
        <td width="20px;"/>
        % endif
        <td style="padding-top: 5px;">
            <p><strong>Details of the event</strong></p>
            <ul>
                % if object.event_id.location:
                    <li>Location: ${object.event_id.location}
                        (<a target="_blank" href="http://maps.google.com/maps?oi=map&amp;q=${object.event_id.location}">View Map</a>)
                    </li>
                % endif
                % if object.event_id.description :
                    <li>Description: ${object.event_id.description}</li>
                % endif
                % if recurrent:
                    <li>When: ${object.recurrence_id.name}</li>
                % endif
                % if not object.event_id.allday and object.event_id.duration
                    <li>Duration: ${('%dH%02d' % (object.event_id.duration,round(object.event_id.duration*60)%60))}</li>
                % endif
                <li>Attendees
                <ul>
                % for attendee in object.event_id.attendee_ids:
                    <li>
                        <div style="display: inline-block; border-radius: 50%; width: 10px; height: 10px; background:${colors[attendee.state] or 'white'};"> </div>
                        % if attendee.common_name != object.common_name:
                            <span style="margin-left:5px">${attendee.common_name}</span>
                        % else:
                            <span style="margin-left:5px">You</span>
                        % endif
                    </li>
                % endfor
                </ul></li>
            </ul>
        </td>
    </tr></table>
    <br/>
    Thank you,
    % if object.event_id.user_id.signature:
        <br/>
        ${object.event_id.user_id.signature | safe}
    % endif
</div>
             <div>
    % set colors = ctx.get('colors', {})
    % set recurrent = object.recurrence_id and not ctx['ignore_recurrence']
    <p>
        Hello ${object.common_name},<br/><br/>
        The date of the meeting has been updated. The meeting ${object.event_id.name} created by ${object.event_id.user_id.partner_id.name} is now scheduled for ${object.event_id.get_display_time_tz(tz=object.partner_id.tz)}.
    </p>
    <div style="text-align: center; margin: 16px 0px 16px 0px;">
        % set target = 'recurrence' if recurrent else 'meeting'
        <a href="/calendar/${target}/accept?token=${object.access_token}&amp;id=${object.event_id.id}" style="padding: 5px 10px; color: #FFFFFF; text-decoration: none; background-color: #875A7B; border: 1px solid #875A7B; border-radius: 3px">
            Accept</a>
        <a href="/calendar/${target}/decline?token=${object.access_token}&amp;id=${object.event_id.id}" style="padding: 5px 10px; color: #FFFFFF; text-decoration: none; background-color: #875A7B; border: 1px solid #875A7B; border-radius: 3px">
            Decline</a>
        <a href="/calendar/meeting/view?token=${object.access_token}&amp;id=${object.event_id.id}" style="padding: 5px 10px; color: #FFFFFF; text-decoration: none; background-color: #875A7B; border: 1px solid #875A7B; border-radius: 3px">
            View</a>
    </div>
    <table border="0" cellpadding="0" cellspacing="0"><tr>
        % if not recurrent:
        <td width="130px;">
            <div style="border-top-left-radius: 3px; border-top-right-radius: 3px; font-size: 12px; border-collapse: separate; text-align: center; font-weight: bold; color: #ffffff; min-height: 18px; background-color: #875A7B; border: 1px solid #875A7B;">
                ${object.event_id.get_interval('dayname', tz=object.partner_id.tz if not object.event_id.allday else None)}
            </div>
            <div style="font-size: 48px; min-height: auto; font-weight: bold; text-align: center; color: #5F5F5F; background-color: #F8F8F8; border: 1px solid #875A7B;">
                ${object.event_id.get_interval('day', tz=object.partner_id.tz if not object.event_id.allday else None)}
            </div>
            <div style="font-size: 12px; text-align: center; font-weight: bold; color: #ffffff; background-color: #875A7B;">
                ${object.event_id.get_interval('month', tz=object.partner_id.tz if not object.event_id.allday else None)}
            </div>
            <div style="border-collapse: separate; color: #5F5F5F; text-align: center; font-size: 12px; border-bottom-right-radius: 3px; font-weight: bold; border: 1px solid #875A7B; border-bottom-left-radius: 3px;">
                ${not object.event_id.allday and object.event_id.get_interval('time', tz=object.partner_id.tz) or ''}
            </div>
        </td>
        <td width="20px;"/>
        % endif
        <td style="padding-top: 5px;">
            <p><strong>Details of the event</strong></p>
            <ul>
                % if object.event_id.location:
                    <li>Location: ${object.event_id.location}
                        (<a target="_blank" href="http://maps.google.com/maps?oi=map&amp;q=${object.event_id.location}">View Map</a>)
                    </li>
                % endif
                % if object.event_id.description :
                    <li>Description: ${object.event_id.description}</li>
                % endif
                % if recurrent:
                    <li>When: ${object.recurrence_id.name}</li>
                % endif
                % if not object.event_id.allday and object.event_id.duration
                    <li>Duration: ${('%dH%02d' % (object.event_id.duration,round(object.event_id.duration*60)%60))}</li>
                % endif
                <li>Attendees
                <ul>
                % for attendee in object.event_id.attendee_ids:
                    <li>
                        <div style="display: inline-block; border-radius: 50%; width: 10px; height: 10px; background: ${colors[attendee.state] or 'white'};"> </div>
                        % if attendee.common_name != object.common_name:
                            <span style="margin-left:5px">${attendee.common_name}</span>
                        % else:
                            <span style="margin-left:5px">You</span>
                        % endif
                    </li>
                % endfor
                </ul></li>
            </ul>
        </td>
    </tr></table>
    <br/>
    Thank you,
    % if object.event_id.user_id.signature:
        <br/>
        ${object.event_id.user_id.signature | safe}
    % endif
</div>
             <div>
    % set colors = {'needsAction': 'grey', 'accepted': 'green', 'tentative': '#FFFF00',  'declined': 'red'}
    <!--
        In a recurring event case, the object.event_id is always the first event
        This makes the event date (and a lot of other information) incorrect
    -->
    % set event_id = ctx.get('force_event_id') or object.event_id
    <p>
        Hello ${object.common_name},<br/><br/>
        This is a reminder for the below event :
    </p>
    <div style="text-align: center; margin: 16px 0px 16px 0px;">
        <a href="/calendar/meeting/accept?token=${object.access_token}&amp;id=${object.event_id.id}" style="padding: 5px 10px; color: #FFFFFF; text-decoration: none; background-color: #875A7B; border: 1px solid #875A7B; border-radius: 3px">
            Accept</a>
        <a href="/calendar/meeting/decline?token=${object.access_token}&amp;id=${object.event_id.id}" style="padding: 5px 10px; color: #FFFFFF; text-decoration: none; background-color: #875A7B; border: 1px solid #875A7B; border-radius: 3px">
            Decline</a>
        <a href="/calendar/meeting/view?token=${object.access_token}&amp;id=${object.event_id.id}" style="padding: 5px 10px; color: #FFFFFF; text-decoration: none; background-color: #875A7B; border: 1px solid #875A7B; border-radius: 3px">
            View</a>
    </div>
    <table border="0" cellpadding="0" cellspacing="0"><tr>
        <td width="130px;">
            <div style="border-top-left-radius: 3px; border-top-right-radius: 3px; font-size: 12px; border-collapse: separate; text-align: center; font-weight: bold; color: #ffffff; min-height: 18px; background-color: #875A7B; border: 1px solid #875A7B;">
                ${event_id.get_interval('dayname', tz=object.partner_id.tz if not event_id.allday else None)}
            </div>
            <div style="font-size: 48px; min-height: auto; font-weight: bold; text-align: center; color: #5F5F5F; background-color: #F8F8F8; border: 1px solid #875A7B;">
                ${event_id.get_interval('day', tz=object.partner_id.tz if not event_id.allday else None)}
            </div>
            <div style="font-size: 12px; text-align: center; font-weight: bold; color: #ffffff; background-color: #875A7B;">
                ${event_id.get_interval('month', tz=object.partner_id.tz if not event_id.allday else None)}
            </div>
            <div style="border-collapse: separate; color: #5F5F5F; text-align: center; font-size: 12px; border-bottom-right-radius: 3px; font-weight: bold; border: 1px solid #875A7B; border-bottom-left-radius: 3px;">
                ${not event_id.allday and event_id.get_interval('time', tz=object.partner_id.tz) or ''}
            </div>
        </td>
        <td width="20px;"/>
        <td style="padding-top: 5px;">
            <p><strong>Details of the event</strong></p>
            <ul>
                % if object.event_id.location:
                    <li>Location: ${object.event_id.location}
                        (<a target="_blank" href="http://maps.google.com/maps?oi=map&amp;q=${object.event_id.location}">View Map</a>)
                    </li>
                % endif
                % if object.event_id.description :
                    <li>Description: ${object.event_id.description}</li>
                % endif
                % if not object.event_id.allday and object.event_id.duration
                    <li>Duration: ${('%dH%02d' % (object.event_id.duration,(object.event_id.duration*60)%60))}</li>
                % endif
                <li>Attendees
                <ul>
                % for attendee in object.event_id.attendee_ids:
                    <li>
                        <div style="display: inline-block; border-radius: 50%; width: 10px; height: 10px; background:${colors[attendee.state] or 'white'};"> </div>
                        % if attendee.common_name != object.common_name:
                            <span style="margin-left:5px">${attendee.common_name}</span>
                        % else:
                            <span style="margin-left:5px">You</span>
                        % endif
                    </li>
                % endfor
                </ul></li>
            </ul>
        </td>
    </tr></table>
    <br/>
    Thank you,
    % if object.event_id.user_id.signature:
        <br/>
        ${object.event_id.user_id.signature | safe}
    % endif
</div>
             <span> hours</span> A user cannot have the same contact twice. Accept Accepted Action Needed Action to Perform Actions may trigger specific behavior like opening calendar view or automatically mark as done when a document is uploaded Active Activities Activity Activity Type All Day All Day, %(day)s All events Archived Attachment Count Attendee Status Attendees Availability Base Event Busy By day Byday Calendar Calendar Alarm Calendar Attendee Information Calendar Contacts Calendar Event Calendar Invitation Calendar Meeting Calendar: Event Reminder Choose what to do with other events in the recurrence. Updating All Events is not allowed when dates or time is modified Common name Contact Count Created by Created on Date Date of month Day Day of Month Day of month Days Decline Declined Description Display Name Document Document ID Document Model Document Model Name Dtstart Duration Duration in minutes Edit Recurrent event Edit recurring event Email Email - 3 Hours Email - 6 Hours Email of Invited Person Employee End Date End Type End date Ending at Event Alarm Event Alarm Manager Event Meeting Type Event Recurrence Rule Event Time Every %(count)s %(period)s,  Everyone Feedback:  First First you have to specify the date of the invitation. Follow Recurrence Followers Followers (Channels) Followers (Partners) Forever Fourth Fr Free Free/Busy Fri Friday Group By Grouping by %s is not allowed. Hours If checked, new messages require your attention. If checked, some messages have a delivery error. If the active field is set to false, it will allow you to hide the event alarm information without removing it. Interval Invitation Invitation Token Invitation details Invitation for Invitation to ${object.event_id.name} Invitations Is Follower Is the Event Highlighted Last Last Modified on Last Updated by Last Updated on Last notification marked as read from base Calendar Let the event automatically repeat at that interval Location Location of Event Main Attachment Me Meeting '%(name)s' starts '%(start_datetime)s' and ends '%(end_datetime)s' Meeting Details Meeting Subject Meeting Types Meeting linked Message Delivery error Messages Minutes Misc Mon Monday Month By Months My Meetings Needs Action No I'm not going. No feedback yet Notification Notification - 1 Days Notification - 1 Hours Notification - 15 Minutes Notification - 2 Hours Notification - 30 Minutes Number of Actions Number of errors Number of messages which requires an action Number of messages with delivery error Number of repetitions Number of unread messages Only internal users Only me Open Calendar Options Participant Partner-related data of the user Privacy Recurrence Recurrence Termination Recurrent Recurrent Rule Remind Before Reminders Repeat Repeat Every Repeat Until Repeat every (Days/Week/Month/Year) Repeat x times Responsible Sat Saturday Schedule a new meeting Search Meetings Second Select attendees... Send mail Show Time as Start Date Start date of an event, without time for full days events Starting at Status of the attendee's participation Stop Stop date of an event, without time for full days events Subject Sun Sunday Tag name already exists ! Tags The The activity is linked to a meeting. Deleting it will remove the meeting as well. Do you want to proceed ? The calendar is shared between employees and fully integrated with
            other applications such as the employee leaves or the business
            opportunities. The ending date and time cannot be earlier than the starting date and time. The ending date cannot be earlier than the starting date. The interval cannot be negative. Third Thu Thursday Timezone Today's Meetings Tue Tuesday Type Uncertain Unit Unread Messages Unread Messages Counter Until Users Wed Wednesday Weekday Weeks Years Yes I'm going. You cannot duplicate a calendar attendee. e.g. Business Lunch Project-Id-Version: Odoo Server 14.0+e
Report-Msgid-Bugs-To: 
PO-Revision-Date: 2020-12-23 17:04+0100
Last-Translator: 
Language-Team: 
MIME-Version: 1.0
Content-Type: text/plain; charset=UTF-8
Content-Transfer-Encoding: 8bit
Plural-Forms: 
Language: de
X-Generator: Poedit 2.4.2
 ${object.event_id.name} - Erinnerung ${object.event_id.name}: Aktualisiert am %(date_start)s at %(time_start)s bis
 %(date_end)s at %(time_end)s (%(timezone)s) %(day)s am (%(start)s bis %(end)s) (%(timezone)s) %s hat die Einladung angenommen. %s hat die Einladung abgelehnt. <div>
    % set colors = ctx.get('colors', {})
    % set recurrent = object.recurrence_id und nicht ctx['ignore_recurrence']
    <p>
        Hallo ${object.common_name},<br/><br/>
        ${object.event_id.user_id.partner_id.name} hat Sie zum Treffen von ${object.event_id.name} von ${object.event_id.user_id.company_id.name} eingeladen.
    </p>
    <div style="text-align: center; margin: 16px 0px 16px 0px;">
        % set target = 'wiederkehrend' if wiederkehrend else 'Besprechung'
        <a href="/calendar/${target}/accept?token=${object.access_token}&amp;id=${object.event_id.id}" style="padding: 5px 10px; color: #FFFFFF; text-decoration: none; background-color: #875A7B; border: 1px solid #875A7B; border-radius: 3px">
            Akzeptieren</a>
        <a href="/calendar/${target}/decline?token=${object.access_token}&amp;id=${object.event_id.id}" style="padding: 5px 10px; color: #FFFFFF; text-decoration: none; background-color: #875A7B; border: 1px solid #875A7B; border-radius: 3px">
            Ablehnen</a>
        <a href="/calendar/meeting/view?token=${object.access_token}&amp;id=${object.event_id.id}" style="padding: 5px 10px; color: #FFFFFF; text-decoration: none; background-color: #875A7B; border: 1px solid #875A7B; border-radius: 3px">
            Ansicht</a>
    </div>
    <table border="0" cellpadding="0" cellspacing="0"><tr>
        % wenn nicht wiederkehrend:
        <td width="130px;">
            <div style="border-top-left-radius: 3px; border-top-right-radius: 3px; font-size: 12px; border-collapse: separate; text-align: center; font-weight: bold; color: #ffffff; min-height: 18px; background-color: #875A7B; border: 1px solid #875A7B;">
                ${object.event_id.get_interval('dayname', tz=object.partner_id.tz if not object.event_id.allday else None)}
            </div>
            <div style="font-size: 48px; min-height: auto; font-weight: bold; text-align: center; color: #5F5F5F; background-color: #F8F8F8; border: 1px solid #875A7B;">
                ${object.event_id.get_interval('day', tz=object.partner_id.tz if not object.event_id.allday else None)}
            </div>
            <div style="font-size: 12px; text-align: center; font-weight: bold; color: #ffffff; background-color: #875A7B;">
                ${object.event_id.get_interval('month', tz=object.partner_id.tz if not object.event_id.allday else None)}
            </div>
            <div style="border-collapse: separate; color: #5F5F5F; text-align: center; font-size: 12px; border-bottom-right-radius: 3px; font-weight: bold; border: 1px solid #875A7B; border-bottom-left-radius: 3px;">
                ${not object.event_id.allday und object.event_id.get_interval('time', tz=object.partner_id.tz) oder ''}
            </div>
        </td>
        <td width="20px;"/>
        % endif
        <td style="padding-top: 5px;">
            <p><strong>Details der Veranstaltung</strong></p>
            <ul>
                % if object.event_id.location:
                    <li>Ort: ${object.event_id.location}
                        (<a target="_blank" href="http://maps.google.com/maps?oi=map&amp;q=${objekt.ereignis_id.ort}">Karte ansehen</a>)
                    </li>
                % endif
                % if object.event_id.description :
                    <li>Beschreibung: ${object.event_id.description}</li>
                % endif
                % if wiederkehrend:
                    <li>Wann: ${object.recurrence_id.name}</li>
                % endif
                % if nicht object.event_id.allday und object.event_id.duration
                    <li>Dauer: ${('%dH%02d' % (object.event_id.duration,round(object.event_id.duration*60)%60))}</li>
                % endif
                <li>Teilnehmer
                <ul>
                % for attendee in object.event_id.attendee_ids:
                    <li>
                        <div style="display: inline-block; border-radius: 50%; width: 10px; height: 10px; background:${colors[attendee.state] or 'white'};"> </div>
                        % if attendee.common_name != object.common_name:
                            <span style="margin-left:5px">${teilnehmer.common_name}</span>
                        % else:
                            <span style="margin-left:5px">Du</span>
                        % endif
                    </li>
                % endif
                </ul></li>
            </ul>
        </td>
    </tr></table>
    <br/>
    Dankeschön,
    % if object.event_id.user_id.signature:
        <br/>
        ${object.event_id.user_id.signature | safe}
    % endif
</div> <div>
    % set colors = ctx.get('colors', {})
    % set recurrent = object.recurrence_id und nicht ctx['ignore_recurrence']
    <p>
        Hallo ${object.common_name},<br/><br/>
        Das Datum des Meetings wurde aktualisiert. Das von ${object.event_id.user_id.partner_id.name} erstellte Meeting ${object.event_id.user_id.partner_id.name} ist jetzt für ${object.event_id.get_display_time_tz(tz=object.partner_id.tz)} geplant.
    </p>
    <div style="text-align: center; margin: 16px 0px 16px 0px;">
        % set target = 'wiederkehrend' if wiederkehrend else 'meeting'
        <a href="/calendar/${target}/accept?token=${object.access_token}&amp;id=${object.event_id.id}" style="padding: 5px 10px; color: #FFFFFF; text-decoration: none; background-color: #875A7B; border: 1px solid #875A7B; border-radius: 3px">
            Akzeptieren</a>
        <a href="/calendar/${target}/decline?token=${object.access_token}&amp;id=${object.event_id.id}" style="padding: 5px 10px; color: #FFFFFF; text-decoration: none; background-color: #875A7B; border: 1px solid #875A7B; border-radius: 3px">
            Ablehnen</a>
        <a href="/calendar/meeting/view?token=${object.access_token}&amp;id=${object.event_id.id}" style="padding: 5px 10px; color: #FFFFFF; text-decoration: none; background-color: #875A7B; border: 1px solid #875A7B; border-radius: 3px">
            Ansicht</a>
    </div>
    <table border="0" cellpadding="0" cellspacing="0"><tr>
        % wenn nicht wiederkehrend:
        <td width="130px;">
            <div style="border-top-left-radius: 3px; border-top-right-radius: 3px; font-size: 12px; border-collapse: separate; text-align: center; font-weight: bold; color: #ffffff; min-height: 18px; background-color: #875A7B; border: 1px solid #875A7B;">
                ${object.event_id.get_interval('dayname', tz=object.partner_id.tz if not object.event_id.allday else None)}
            </div>
            <div style="font-size: 48px; min-height: auto; font-weight: bold; text-align: center; color: #5F5F5F; background-color: #F8F8F8; border: 1px solid #875A7B;">
                ${object.event_id.get_interval('day', tz=object.partner_id.tz if not object.event_id.allday else None)}
            </div>
            <div style="font-size: 12px; text-align: center; font-weight: bold; color: #ffffff; background-color: #875A7B;">
                ${object.event_id.get_interval('month', tz=object.partner_id.tz if not object.event_id.allday else None)}
            </div>
            <div style="border-collapse: separate; color: #5F5F5F; text-align: center; font-size: 12px; border-bottom-right-radius: 3px; font-weight: bold; border: 1px solid #875A7B; border-bottom-left-radius: 3px;">
                ${not object.event_id.allday und object.event_id.get_interval('time', tz=object.partner_id.tz) oder ''}
            </div>
        </td>
        <td width="20px;"/>
        % endif
        <td style="padding-top: 5px;">
            <p><strong>Details der Veranstaltung</strong></p>
            <ul>
                % if object.event_id.location:
                    <li>Ort: ${object.event_id.location}
                        (<a target="_blank" href="http://maps.google.com/maps?oi=map&amp;q=${objekt.ereignis_id.ort}">Karte ansehen</a>)
                    </li>
                % endif
                % if object.event_id.description :
                    <li>Beschreibung: ${object.event_id.description}</li>
                % endif
                % if wiederkehrend:
                    <li>Wann: ${object.recurrence_id.name}</li>
                % endif
                % if nicht object.event_id.allday und object.event_id.duration
                    <li>Dauer: ${('%dH%02d' % (object.event_id.duration,round(object.event_id.duration*60)%60))}</li>
                % endif
                <li>Teilnehmer
                <ul>
                % for attendee in object.event_id.attendee_ids:
                    <li>
                        <div style="display: inline-block; border-radius: 50%; width: 10px; height: 10px; background: ${colors[attendee.state] or 'white'};"> </div>
                        % if attendee.common_name != object.common_name:
                            <span style="margin-left:5px">${teilnehmer.common_name}</span>
                        % else:
                            <span style="margin-left:5px">Du</span>
                        % endif
                    </li>
                % endif
                </ul></li>
            </ul>
        </td>
    </tr></table>
    <br/>
    Dankeschön,
    % if object.event_id.user_id.signature:
        <br/>
        ${object.event_id.user_id.signature | safe}
    % endif
</div>
           <div>
    % set colors = {'needsAction': 'grey', 'accepted': 'green', 'tentative': '#FFFF00', 'declined': 'red'}
    <!--
        Im Falle eines wiederkehrenden Ereignisses ist die object.event_id immer das erste Ereignis
        Dadurch wird das Ereignisdatum (und eine Menge anderer Informationen) falsch
    -->
    % set event_id = ctx.get('force_event_id') oder object.event_id
    <p>
        Hallo ${object.common_name},<br/><br/>
        Dies ist eine Erinnerung für das unten stehende Ereignis :
    </p>
    <div style="text-align: center; margin: 16px 0px 16px 0px;">
        <a href="/calendar/meeting/accept?token=${object.access_token}&amp;id=${object.event_id.id}" style="padding: 5px 10px; color: #FFFFFF; text-decoration: none; background-color: #875A7B; border: 1px solid #875A7B; border-radius: 3px">
            Akzeptieren</a>
        <a href="/calendar/meeting/decline?token=${object.access_token}&amp;id=${object.event_id.id}" style="padding: 5px 10px; color: #FFFFFF; text-decoration: none; background-color: #875A7B; border: 1px solid #875A7B; border-radius: 3px">
            Ablehnen</a>
        <a href="/calendar/meeting/view?token=${object.access_token}&amp;id=${object.event_id.id}" style="padding: 5px 10px; color: #FFFFFF; text-decoration: none; background-color: #875A7B; border: 1px solid #875A7B; border-radius: 3px">
            Ansicht</a>
    </div>
    <table border="0" cellpadding="0" cellspacing="0"><tr>
        <td width="130px;">
            <div style="border-top-left-radius: 3px; border-top-right-radius: 3px; font-size: 12px; border-collapse: separate; text-align: center; font-weight: bold; color: #ffffff; min-height: 18px; background-color: #875A7B; border: 1px solid #875A7B;">
                ${event_id.get_interval('dayname', tz=object.partner_id.tz if not event_id.allday else None)}
            </div>
            <div style="font-size: 48px; min-height: auto; font-weight: bold; text-align: center; color: #5F5F5F; background-color: #F8F8F8; border: 1px solid #875A7B;">
                ${event_id.get_interval('day', tz=object.partner_id.tz if not event_id.allday else None)}
            </div>
            <div style="font-size: 12px; text-align: center; font-weight: bold; color: #ffffff; background-color: #875A7B;">
                ${event_id.get_interval('month', tz=object.partner_id.tz if not event_id.allday else None)}
            </div>
            <div style="border-collapse: separate; color: #5F5F5F; text-align: center; font-size: 12px; border-bottom-right-radius: 3px; font-weight: bold; border: 1px solid #875A7B; border-bottom-left-radius: 3px;">
                ${not event_id.allday und event_id.get_interval('time', tz=object.partner_id.tz) oder ''}
            </div>
        </td>
        <td width="20px;"/>
        <td style="padding-top: 5px;">
            <p><strong>Details des Ereignisses</strong></p>
            <ul>
                % if object.event_id.location:
                    <li>Ort: ${object.event_id.location}
                        (<a target="_blank" href="http://maps.google.com/maps?oi=map&amp;q=${objekt.ereignis_id.ort}">Karte ansehen</a>)
                    </li>
                % endif
                % if object.event_id.description :
                    <li>Beschreibung: ${object.event_id.description}</li>
                % endif
                % if nicht object.event_id.allday und object.event_id.duration
                    <li>Dauer: ${('%dH%02d' % (object.event_id.duration,(object.event_id.duration*60)%60))}</li>
                % endif
                <li>Teilnehmer
                <ul>
                % for attendee in object.event_id.attendee_ids:
                    <li>
                        <div style="display: inline-block; border-radius: 50%; width: 10px; height: 10px; background:${colors[attendee.state] or 'white'};"> </div>
                        % if attendee.common_name != object.common_name:
                            <span style="margin-left:5px">${teilnehmer.common_name}</span>
                        % else:
                            <span style="margin-left:5px">Du</span>
                        % endif
                    </li>
                % endif
                </ul></li>
            </ul>
        </td>
    </tr></table>
    <br/>
    Dankeschön,
    % if object.event_id.user_id.signature:
        <br/>
        ${object.event_id.user_id.signature | safe}
    % endif
</div>
             <span> Stunden</span> Ein Benutzer kann nicht zweimal denselben Kontakt haben. Akzeptieren Akzeptiert Aktion notwendig Aktion beginnen Aktion führt gegebenfalls zu weiteren Funktionen wie Kalenderansicht oder automatischer Ausführung wenn ein Dokument hochgeladen wurde. Aktiv Aktivitäten Aktivität Aktivitätstyp Ganztägig Ganzer Tag, %(Tag)s Alle Veranstaltungen Archiviert # Anhänge Teilnehmerstatus Teilnehmer Frühester Beginn Basis-Ereignis Beschäftigt Am Tag Byday Kalender Kalender Alarm Informationen für Kalender-Teilnehmer Kalender Kontakte Kalender Veranstaltung Termineinladung Kalender Termin Kalender: Event Erinnerung Wählen Sie, was mit anderen Ereignissen in der Wiederholung geschehen soll. Das Aktualisieren aller Ereignisse ist nicht erlaubt, wenn Datum oder Uhrzeit geändert werden Gew. Name Kontakt Anzahl Erstellt von Erstellt am Datum Datum im Monat Tag Tag des Monats Tag im Monat Tage Absagen Abgesagt Beschreibung Anzeigename Dokument Dokument-ID Dokumentenmodell Name des Dokumentmodells Dtstart Dauer Dauer in Minuten Bearbeiten Wiederkehrendes Ereignis Wiederkehrendes Ereignis bearbeiten E-Mail Email - 3 Stunden Email - 6 Stunden E-Mail Adresse der eingel. Person Mitarbeiter Enddatum Ende Typ Enddatum Ende am Ereignis-Alarm Ereignis-Alarm-Manager Veranstultungs-Besprechungstyp Ereignis-Wiederholungs-Regel Veranstaltungstermin Alle %(count)s %(period)s,  Alle Benutzer Feedback: Erster Zunächst müssen Sie das Datum der Einladung akzeptieren. Wiederholung folgen Abonnenten Abonnenten (Kanäle) Abonnenten (Partner) Für immer Vierter Fr Verfügbar Verfügb./ Beschäft. Fr Freitag Gruppieren nach Die Gruppierung nach %s ist nicht erlaubt. Stunden Falls markiert, benötigen neue Nachrichten Ihre Kenntnisnahme. Das Senden mancher Nachrichten ist fehlgeschlagen wenn dieses Fenster angekreuzt ist. Wenn das Aktiv-Feld deaktiviert wird, wird die Erinnerung ausgeblendet ohne sie zu entfernen Intervall Einladung Zugang Token Einladungsdetails Einladung für Einladung an ${object.event_id.name} Einladungen Ist ein Abonnent Ist das Event hervorgehoben Letzter Zuletzt geändert am Zuletzt aktualisiert durch Zuletzt aktualisiert am Zuletzt gelesene Mitteilung aus dem Kalender Termin wird automatisch in diesem Abstand wiederholt Ort Veranstaltungsort Hauptanhänge Ich Meeting '%(name)s' beginnt '%(start_datetime)s' und endet '%(end_datetime)s' Meeting-Details Meeting Betreff Meetingtypen Termin verlinkt Error beim senden der Nachricht Nachrichten Minuten Diverse Mo Montag Monat nach Monate Meine Meetings Erfordert Aktion Nein, ich werde nicht teilnehmen. Noch keine Rückmeldung Benachrichtigung Erinnerung - 1 Tag Erinnerung - 1 Stunde Erinnerung - 15 Minuten Erinnerung - 2 Stunden Erinnerung - 30 Minuten Anzahl der Aktionen # Fehler Anzahl der Nachrichten, die eine Aktion erfordern Anzahl der Nachrichten mit einem Fehler beim Senden. Anzahl der Wiederholungen Anzahl ungelesener Nachrichten Nur interne Benutzer Nur ich Kalender öffnen Optionen Teilnehmer Partnerbezogene Daten des Benutzers Privatsphäre Wiederholung Erneute Absage Terminwiederholung Regel wiederk. Ereignis Benachritigen bevor  Erinnerungen Wiederholen Wiederhole alle Wiederholen bis Wiederhole alle (Tag/Woche/Monat/Jahr) Anzahl Wiederholungen Verantwortlich Sa Samstag Planen Sie ein neues Meeting Meetings suchen Sekunde Wähle Teilnehmer... E-Mail senden Verfügbarkeit Startdatum Start Datum eines Ereignisses, Ohne die Zeit für ganztägige Ereignisse Beginnend mit Status Teilnahme Stopp End Datum eines Ereignisses, Ohne die Zeit für ganztägige Ereignisse Betreff So Sonntag Schlagwort existiert bereits! Stichwörter Der Die Aktivität ist mit einer Besprechung verknüpft. Wenn Sie es löschen, wird auch die Besprechung gelöscht. Wollen Sie fortfahren? Der Kalender wird zwischen den Mitarbeitern geteilt und ist voll integriert mit
andere Anwendungen, wie z.B. der Austritt des Mitarbeiters oder andere geschäftliche Ereignisse. Das Enddatum und die Endzeit dürfen nicht vor dem Startdatum und der Endzeit liegen. Das Enddatum darf nicht vor dem Startdatum liegen. Das Intervall kann nicht negativ sein. Dritter Do Donnerstag Zeitzone heutige Meetings Di Dienstag Typ Unklar Einheit Ungelesene Nachrichten Zähler der ungelesenen Nachrichten Bis Benutzer Mi Mittwoch Wochentag Wochen Jahre Ich werde teilnehmen. Sie können einen Teilnehmer nicht duplizieren evtl. Geschäftsessen 