map_data = schools_filtered.groupby(['Geographic region',
                        'ACCREDAGENCY']).agg({"Name":"count",
                                              }