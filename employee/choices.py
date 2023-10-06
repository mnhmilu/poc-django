PROJECT_STATUS_CHOICES = (        
    ('INITIATED', 'Initiated'),
    ('IN_DEV', 'In Development'),
    ('PAUSED', 'Paused'),    
    ('IN_QA', 'In QA'),
    ('COMPLETED', 'Completed')
)

EVENT_NAME_CHOICES = [
        ('Requirement Issue', 'Requirement Issue'),        
        ('Priority Changed', 'Priority Changed'),
        ('QA Feedback', 'QA Feedback'),
        ('API Dependency', 'API Dependency'),
        ('OTHERS', 'Others'),  # Add "OTHERS" as a choice
    ]