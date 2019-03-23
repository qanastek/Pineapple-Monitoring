graph TD
AutoCheckUser --> CollectData
CollectData --> |POST| SEND

Server --> |POST| IssueDetector__Program
IssueDetector__Program --> MailSender__SendEmail
MailSender__SendEmail --> |SMTP| EMAIL

Server --> SaveData__SaveData
SaveData__SaveData --> |SQL| InsertInto__history.db
InsertInto__history.db --> |HTTP| RETURN_CODE_200