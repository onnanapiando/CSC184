Feature: Web application for accessing web resources

     As a user I wish to be able to access web resources using
     HTTP and FTP protocol   

     Scenario: Access web resources 
     Given I accessed the web resources of a site
     When I use the protocol ftp
     Then I get a file list for ftp containing:
     |                      ftp_files                                 |
     |CERT                                                            |
     |CTM -> development/CTM                                          |
     |CVSup -> development/CVSup                                      |
     |ERRATA                                                          |
     |ISO-IMAGES-amd64 -> releases/amd64/amd64/ISO-IMAGES             |
     |ISO-IMAGES-i386 -> releases/i386/i386/ISO-IMAGES                |
     |ISO-IMAGES-ia64 -> releases/ia64/ia64/ISO-IMAGES                |
     |ISO-IMAGES-pc98 -> releases/pc98/ISO-IMAGES                     |
     |ISO-IMAGES-powerpc -> releases/powerpc/powerpc/ISO-IMAGES       |
     |ISO-IMAGES-powerpc64 -> releases/powerpc/powerpc64/ISO-IMAGES   |
     |ISO-IMAGES-sparc64 -> releases/sparc64/sparc64/ISO-IMAGES       |
     |README.TXT                                                      |
     |TIMESTAMP                                                       |
     |branches                                                        |
     |development                                                     |
     |dir.sizes                                                       |
     |distfiles -> ports/distfiles                                    |
     |doc                                                             |
     |ports                                                           |
     |releases                                                        |
     |snapshots                                                       |
     |tools                                                           |
     |updates                                                         |

     Scenario: Access web resources 
     Given I accessed the web resources of a site
     When I use the protocol http
     Then I get a file list for http containing:
     |http_files                                                |
     |CERT                                                      |
     |CTM -> development/CTM                                    |
     |CVSup -> development/CVSup                                |
     |ERRATA                                                    |
     |ISO-IMAGES-amd64 -> releases/amd64/amd64/ISO-IMAGES       |
     |ISO-IMAGES-i386 -> releases/i386/i386/ISO-IMAGES          |
     |ISO-IMAGES-ia64 -> releases/ia64/ia64/ISO-IMAGES          |
     |ISO-IMAGES-pc98 -> releases/pc98/ISO-IMAGES               |
     |ISO-IMAGES-powerpc -> releases/powerpc/powerpc/ISO-IMAGES |
     |ISO-IMAGES-powerpc64 -> releases/powerpc/powerpc64/ISO-IMAGES|
     |ISO-IMAGES-sparc64 -> releases/sparc64/sparc64/ISO-IMAGES |
     |README.TXT                                                |
     |TIMESTAMP                                                 |
     |branches                                                  |
     |development                                               |
     |dir.sizes                                                 |
     |distfiles -> ports/distfiles                              |
     |doc                                                       |
     |ports                                                     |
     |releases                                                  |
     |snapshots                                                 | 
     |tools                                                     |
     |updates                                                   | 
