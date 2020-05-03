create table users ( 
                      id INTEGER PRIMARY KEY AUTOINCREMENT
                    , name text
                    , role text
                );
                
create table points (
                       awarder INTEGER
                     , awardee INTEGER
                     , point_change INTEGER
                     , timestamp timestamp default CURRENT_TIMESTAMP
                    );