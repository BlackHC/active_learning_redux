store = {}
store['timestamp']=1620294885
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/rejection_ood_experiment.py', '--id=7']
store['commit']='2edd2424ec449a84ea20a7324261784a7627b78d'
store['github_url']='2edd2424ec449a84ea20a7324261784a7627b78d'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/rejection_ood_experiment.py'
store['job_id']=7
store['worker_id']=7
store['num_workers']=40
store['config']={'seed': 8, 'acquisition_size': 50, 'max_training_set': 450, 'num_pool_samples': 100, 'num_eval_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'validation_set_size': 1024, 'validation_split_random_state': 0, 'initial_training_set_size': 20, 'min_samples_per_epoch': 5056, 'mnist_repetitions': 1, 'add_dataset_noise': False, 'acquisition_function': 'batchbald_redux.acquisition_functions.BALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationPoolModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 0.0}
store['log']={}
store['dataset_info']={'training': "(FastMNIST (train; 58976 samples)) + ('OoD Dataset (60000 samples)' | constant_target{'target': tensor(-1, device='cuda:0'), 'num_classes': 10})", 'test': "'FastMNIST (test, 10000 samples)'"}
store['initial_training_set_indices']=[30392, 53434, 12640, 8533, 22304, 37915, 58226, 44119, 3091, 14640, 58125, 39579, 43812, 53689, 52296, 46037, 22015, 40334, 57520, 43803]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 2.3248918056488037})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 2.456958293914795})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 2.661208391189575})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 2.6907408237457275})
store['active_learning_steps'][0]['training']['best_epoch']=1
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.6848, 'crossentropy': 2.0842927734375}
store['active_learning_steps'][0]['acquisition']={'indices': [20037, 11379, 23347, 40217, 42131, 47781, 22605, 34678, 52785, 41553, 48668, 35481, 59730, 29343, 15406, 20089, 17784, 25341, 47689, 40712, 9691, 19981, 45207, 8234, 13203, 9044, 42245, 31087, 38112, 34524, 41635, 32856, 32794, 47759, 40786, 47983, 19911, 23143, 42515, 44202, 4863, 42839, 38256, 21375, 59723, 20025, 47031, 4727, 54654, 23388], 'labels': [8, 0, 8, 0, 0, 3, 0, 8, 3, 0, 8, 0, 0, 5, 8, 8, 8, 8, 3, 7, 0, 8, 8, 8, 0, 5, 0, 8, 8, 8, 0, 2, 3, 2, 9, 5, 8, 8, 8, 8, 7, 2, 2, 8, 0, 8, 0, 8, 8, 7], 'scores': [1.2294400334358215, 1.1936703324317932, 1.1905514001846313, 1.1888534426689148, 1.1870081424713135, 1.181320607662201, 1.1791449785232544, 1.1774577498435974, 1.176138162612915, 1.1718991994857788, 1.1662774682044983, 1.1656161546707153, 1.1631893515586853, 1.1627302169799805, 1.1614086031913757, 1.1591248512268066, 1.1588207483291626, 1.1586589813232422, 1.1571726202964783, 1.156821846961975, 1.1555883288383484, 1.153644859790802, 1.1517339944839478, 1.1509330868721008, 1.1500078439712524, 1.1498379111289978, 1.1485921144485474, 1.1476786136627197, 1.1473318338394165, 1.146734595298767, 1.1453362703323364, 1.1443659663200378, 1.1430774927139282, 1.1417993903160095, 1.1366813778877258, 1.1344313621520996, 1.1316716074943542, 1.1313729882240295, 1.1310492157936096, 1.130739450454712, 1.1264237761497498, 1.12587308883667, 1.124958336353302, 1.1239829063415527, 1.1236684322357178, 1.1232334971427917, 1.1210100054740906, 1.1201075911521912, 1.1193708777427673, 1.1193357706069946]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 1.5523563623428345})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 1.5897846221923828})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 1.794421672821045})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 2.0101406574249268})
store['active_learning_steps'][1]['training']['best_epoch']=1
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.6805, 'crossentropy': 1.5028728515625}
store['active_learning_steps'][1]['acquisition']={'indices': [26907, 49805, 10978, 54035, 59333, 24223, 22537, 9810, 5045, 13243, 3603, 58259, 46129, 47028, 49438, 58470, 17518, 45761, 53033, 52658, 29005, 53152, 14912, 59797, 12117, 43547, 25362, 49784, 19343, 48216, 56220, 49149, 17212, 36492, 55987, 56017, 17131, 31327, 50319, 52851, 49060, 39130, 27641, 6345, 42697, 48227, 59298, 59281, 20663, 2125], 'labels': [2, 2, 2, 7, 2, 8, 4, 9, 9, 7, 0, 6, 2, 4, 8, 9, 0, 4, 2, 4, 2, 5, 6, 2, 3, 2, 8, 5, 2, 4, 7, 3, 2, 8, 2, 7, 3, 2, 4, 2, 6, 6, 2, 9, 4, 0, 2, 2, 6, 2], 'scores': [0.8106940984725952, 0.8073318004608154, 0.8060142397880554, 0.8049890995025635, 0.801661491394043, 0.7941082715988159, 0.780135452747345, 0.7791349291801453, 0.7783253788948059, 0.7768125534057617, 0.7700185179710388, 0.7666759490966797, 0.7662200927734375, 0.7654393315315247, 0.7624308466911316, 0.760769248008728, 0.7604328393936157, 0.7597293853759766, 0.7550060153007507, 0.7523932456970215, 0.7509627342224121, 0.7507603168487549, 0.7498080730438232, 0.7443115711212158, 0.7427780032157898, 0.7412803173065186, 0.7412258386611938, 0.7409480810165405, 0.7400846481323242, 0.7384078502655029, 0.737342119216919, 0.7353689670562744, 0.7353029251098633, 0.7337503433227539, 0.7332823872566223, 0.7313221096992493, 0.7300240993499756, 0.7297581434249878, 0.7296918630599976, 0.7289221286773682, 0.728739857673645, 0.7277576923370361, 0.726747989654541, 0.7265759706497192, 0.7265622615814209, 0.7261728048324585, 0.7257932424545288, 0.7252362966537476, 0.7249946594238281, 0.7245069742202759]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.7548828125, 'crossentropy': 1.1739466190338135})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.7939453125, 'crossentropy': 1.1092067956924438})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.7939453125, 'crossentropy': 1.3208320140838623})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 1.317995309829712})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.8017578125, 'crossentropy': 1.4377124309539795})
store['active_learning_steps'][2]['training']['best_epoch']=2
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.8121, 'crossentropy': 1.04442578125}
store['active_learning_steps'][2]['acquisition']={'indices': [13030, 10916, 52574, 2000, 20641, 26898, 17083, 5730, 36614, 47365, 6846, 39700, 26034, 7322, 41069, 37071, 3300, 2352, 40070, 813, 57542, 46187, 36642, 23468, 36335, 5268, 34800, 37743, 49395, 14113, 7895, 34664, 1881, 45256, 32415, 53344, 31988, 50924, 37231, 55503, 20933, 14063, 55727, 46620, 24111, 36132, 24467, 56362, 26733, 7983], 'labels': [0, 0, 2, 5, 9, 7, 6, 0, 2, 4, 2, 5, 5, 3, 0, 6, 2, 0, 7, 2, 0, 3, 5, 2, 2, 0, 5, 2, 1, 2, 2, 2, 2, 5, 5, 0, 3, 0, 6, 0, 5, 2, 0, 2, 3, 3, 2, 0, 2, 2], 'scores': [0.9841951131820679, 0.9713659286499023, 0.9134470224380493, 0.9020370841026306, 0.8959155678749084, 0.8832526206970215, 0.8809309005737305, 0.8776848912239075, 0.8744678497314453, 0.8722593188285828, 0.8713779449462891, 0.8700147867202759, 0.8640739917755127, 0.8634293675422668, 0.8630211353302002, 0.8585063219070435, 0.8582011461257935, 0.8539290428161621, 0.8520117998123169, 0.8517874479293823, 0.8517487049102783, 0.8510317206382751, 0.8510048389434814, 0.8508355021476746, 0.8502938151359558, 0.8486346006393433, 0.8449629545211792, 0.8440515398979187, 0.8428177237510681, 0.8417441844940186, 0.841398298740387, 0.8413466811180115, 0.8411104679107666, 0.8409711718559265, 0.8409527540206909, 0.8407153487205505, 0.8405121564865112, 0.838520884513855, 0.8371424674987793, 0.8370875120162964, 0.8362199068069458, 0.8357042670249939, 0.8342487812042236, 0.8338173627853394, 0.8327622413635254, 0.8318027853965759, 0.8316660523414612, 0.8315483331680298, 0.8305887579917908, 0.8304007053375244]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 1.0507640838623047})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.8111088275909424})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.7676348686218262})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.8592343330383301})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.823852002620697})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.8285592794418335})
store['active_learning_steps'][3]['training']['best_epoch']=3
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.881, 'crossentropy': 0.734194677734375}
store['active_learning_steps'][3]['acquisition']={'indices': [38623, 4083, 46441, 9770, 52169, 23642, 16860, 2118, 7559, 15601, 25622, 14337, 24377, 47936, 27767, 52550, 39893, 23746, 27503, 7577, 7571, 55372, 5750, 6466, 21174, 39873, 11298, 23028, 52624, 11842, 6096, 8439, 38895, 10473, 19382, 40434, 43532, 5474, 38512, 19380, 37315, 35664, 47068, 27193, 13365, 26850, 59509, 56682, 19190, 14732], 'labels': [8, 8, 6, 5, 2, 2, 8, 7, 6, 9, 5, 7, 6, 8, 5, 2, 6, 5, 2, 6, 6, 6, 6, 2, 2, 8, 2, 2, 1, 5, 5, 9, 6, 6, 6, 5, 8, 8, 5, 4, 6, 6, 4, 5, 8, 2, 6, 2, 9, 6], 'scores': [0.979085385799408, 0.970654308795929, 0.9494268894195557, 0.9475713968276978, 0.9309438467025757, 0.9274258017539978, 0.9250848889350891, 0.9134024977684021, 0.9117231369018555, 0.8990054726600647, 0.8974899053573608, 0.8972471952438354, 0.8970527648925781, 0.896099328994751, 0.8937254548072815, 0.891417384147644, 0.8906184434890747, 0.8858729004859924, 0.8850142359733582, 0.880013644695282, 0.8792226314544678, 0.8790766596794128, 0.874826192855835, 0.8744753003120422, 0.8744490146636963, 0.873731791973114, 0.871911346912384, 0.8714305758476257, 0.8711981177330017, 0.8710846304893494, 0.8708898425102234, 0.8703336715698242, 0.8701378107070923, 0.8680722713470459, 0.8674038648605347, 0.8649341464042664, 0.86408531665802, 0.8627375364303589, 0.8620613217353821, 0.8611587882041931, 0.860491931438446, 0.8600314259529114, 0.8594690561294556, 0.8584957122802734, 0.8584656119346619, 0.8581054210662842, 0.8575202822685242, 0.8573334217071533, 0.8565648794174194, 0.8564589023590088]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 1.1975963115692139})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.659896731376648})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5965143442153931})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.590496301651001})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6246926784515381})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6165512204170227})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6265140771865845})
store['active_learning_steps'][4]['training']['best_epoch']=4
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.9161, 'crossentropy': 0.5570505859375}
store['active_learning_steps'][4]['acquisition']={'indices': [1812, 26444, 12830, 43000, 14787, 14843, 47475, 18398, 22692, 9948, 33383, 45520, 4153, 33130, 14687, 23490, 15180, 19064, 45590, 14735, 41802, 50403, 14815, 28375, 18527, 23452, 25246, 24613, 42121, 43256, 58560, 45810, 28617, 52394, 16600, 14627, 29711, 15949, 18190, 32427, 47093, 32902, 18008, 29839, 19188, 15893, 42317, 9384, 18924, 7762], 'labels': [4, 1, 4, 9, 9, 9, 5, 4, 9, 8, 1, 8, 2, 9, 9, 3, 4, 4, 4, 9, 2, -1, 9, 5, 3, 5, 2, 9, 5, 3, 0, 9, 5, 3, 4, 9, 8, 5, 4, 0, 8, 5, 4, 2, 1, 5, 5, 5, 3, 3], 'scores': [1.0794073343276978, 1.0257882475852966, 1.0062888264656067, 0.9847784042358398, 0.9734019041061401, 0.9696190357208252, 0.9672385454177856, 0.9642134308815002, 0.9641681909561157, 0.9610997438430786, 0.960854709148407, 0.950169026851654, 0.9467591047286987, 0.9461158514022827, 0.9422799348831177, 0.9391253590583801, 0.938920259475708, 0.9374375343322754, 0.9349063634872437, 0.9333198070526123, 0.9314368367195129, 0.9299899339675903, 0.9265974760055542, 0.9253104329109192, 0.9224954843521118, 0.9210142493247986, 0.9203399121761322, 0.9197303652763367, 0.9167704582214355, 0.9163556694984436, 0.9162551760673523, 0.9156877398490906, 0.9138478636741638, 0.913061261177063, 0.9120570421218872, 0.9117021560668945, 0.9115284085273743, 0.9108943939208984, 0.9107226729393005, 0.9105526208877563, 0.9101846218109131, 0.9098091125488281, 0.906564474105835, 0.9063153266906738, 0.9059104919433594, 0.9053213596343994, 0.9049094915390015, 0.9049078822135925, 0.9048108458518982, 0.9048072099685669]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7626953125, 'crossentropy': 0.9929133653640747})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.5794744491577148})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.49502235651016235})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.491447389125824})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5137604475021362})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.48092514276504517})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.5045284032821655})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.5509559512138367})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.5140568614006042})
store['active_learning_steps'][5]['training']['best_epoch']=6
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.9418, 'crossentropy': 0.458706494140625}
store['active_learning_steps'][5]['acquisition']={'indices': [31456, 15781, 19495, 28757, 38912, 41453, 7833, 7829, 52708, 26358, 28102, 34429, 20171, 59747, 23140, 59726, 51261, 40066, 27514, 1075, 40378, 51508, 25159, 49624, 30144, 34520, 49525, 37583, 16834, 5175, 49497, 40654, 22677, 1364, 54316, 20869, 45017, 55073, 13983, 44570, 19356, 40457, 42703, 29803, 39822, 22824, 26020, 21040, 5315, 22033], 'labels': [9, 5, 3, 3, -1, 3, 5, -1, 4, 3, 0, 4, 5, 5, 7, 5, 4, 4, 4, 7, -1, 6, 0, 6, 9, 6, 8, -1, 5, 4, 0, 5, 4, 9, 6, 3, 4, 4, 3, 7, 6, 0, 0, 6, 9, 9, 5, 9, 3, 5], 'scores': [1.0994081497192383, 1.0857625007629395, 1.0576934814453125, 1.0460517406463623, 1.0436155796051025, 1.0401980876922607, 1.0342615842819214, 1.0317045450210571, 1.0273078083992004, 1.0184540152549744, 1.0117473602294922, 1.0112742185592651, 0.9994015097618103, 0.9954531788825989, 0.98955237865448, 0.9820849299430847, 0.9809750318527222, 0.9704088568687439, 0.9671037197113037, 0.9667842388153076, 0.9652946591377258, 0.9644448459148407, 0.9643090963363647, 0.9621847867965698, 0.9607564210891724, 0.9590569138526917, 0.9569283723831177, 0.9563321471214294, 0.9558638334274292, 0.9538445472717285, 0.9523359537124634, 0.950372040271759, 0.9482883810997009, 0.9474691152572632, 0.9462490975856781, 0.9429323673248291, 0.941674530506134, 0.9412339329719543, 0.9404401183128357, 0.9376525282859802, 0.9374063909053802, 0.9371583461761475, 0.9359131455421448, 0.9352658987045288, 0.9350687861442566, 0.9347155690193176, 0.9339253306388855, 0.9332422018051147, 0.9331486225128174, 0.9324800372123718]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 1.0964267253875732})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6239036321640015})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5104071497917175})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.5197679996490479})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.4837675094604492})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.4925820827484131})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4751198887825012})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5607995986938477})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.5547082424163818})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.528968334197998})
store['active_learning_steps'][6]['training']['best_epoch']=7
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.9396, 'crossentropy': 0.457786962890625}
store['active_learning_steps'][6]['acquisition']={'indices': [16117, 35864, 19597, 39411, 12663, 18473, 16628, 59309, 20196, 52304, 17057, 29117, 44736, 2803, 19396, 43471, 47511, 39561, 50578, 7949, 8971, 1814, 42973, 37469, 11745, 38280, 37450, 1674, 19362, 39668, 1376, 45982, 34640, 41309, 56480, 39429, 34819, 32880, 17265, 4822, 11232, 28745, 24457, 59294, 15276, 16731, 22687, 48587, 42702, 35944], 'labels': [9, 5, 9, 2, 8, 4, 9, 8, 9, 9, 4, 7, 5, 3, 5, 7, 7, 2, 9, -1, 9, 4, 4, 2, 9, 5, 4, 9, 8, 8, 7, 4, 1, 7, 9, 2, 8, 0, 2, 4, 3, 7, 8, 8, 7, -1, 9, 3, 1, 3], 'scores': [1.0081913471221924, 1.0052873492240906, 1.000275433063507, 0.9970532655715942, 0.9969729781150818, 0.9929800629615784, 0.9879437685012817, 0.9802525639533997, 0.9779582023620605, 0.9779438376426697, 0.9752628207206726, 0.9718155264854431, 0.9696311354637146, 0.9678689241409302, 0.9656533598899841, 0.962534487247467, 0.9612569808959961, 0.9606630206108093, 0.9573071599006653, 0.9532756209373474, 0.9504320621490479, 0.9498778581619263, 0.9495972990989685, 0.9493902325630188, 0.9469824433326721, 0.9443924427032471, 0.9439103603363037, 0.9435775876045227, 0.9426067471504211, 0.94126957654953, 0.9397862553596497, 0.9391623735427856, 0.9378404021263123, 0.9365456104278564, 0.9359137415885925, 0.9327977895736694, 0.9322537183761597, 0.9315870404243469, 0.9315047860145569, 0.9307090044021606, 0.9305806457996368, 0.9236807227134705, 0.9207721948623657, 0.9199609160423279, 0.9154496788978577, 0.9140180349349976, 0.913585364818573, 0.9123708605766296, 0.9107743501663208, 0.9102848768234253]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 1.174464464187622})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.613757312297821})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.48809319734573364})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.44947758316993713})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.4111320972442627})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.4147406816482544})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.40775734186172485})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.4194706082344055})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.44930338859558105})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.4431079924106598})
store['active_learning_steps'][7]['training']['best_epoch']=7
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.9515, 'crossentropy': 0.367114697265625}
store['active_learning_steps'][7]['acquisition']={'indices': [22561, 22607, 41965, 23956, 54885, 49563, 9559, 41933, 9687, 30123, 27928, 18150, 5013, 31014, 3367, 32419, 5129, 48360, 7793, 52889, 30900, 22595, 54892, 41573, 10555, 40775, 17005, 13388, 52690, 34328, 59928, 32387, 38641, 49354, 49517, 47260, 21390, 38698, 57507, 50461, 31339, 24263, 5103, 13021, 57575, 50736, 13729, 44287, 32776, 5684], 'labels': [6, 4, 2, 4, 6, 8, 8, 5, 0, 0, 2, 8, 2, 8, 0, 4, 2, 3, 8, -1, 5, 4, 3, 3, 1, 6, 1, 3, 3, 8, 6, 4, 8, 0, 6, 6, 3, 5, 0, 7, 6, 9, 2, 5, 0, -1, 0, 6, 4, 6], 'scores': [1.0278886556625366, 0.9857492446899414, 0.9704736471176147, 0.9597428441047668, 0.9582179188728333, 0.957061767578125, 0.9454357624053955, 0.9414374828338623, 0.9369803071022034, 0.9346212148666382, 0.9262953996658325, 0.9232885241508484, 0.9170547127723694, 0.9154037833213806, 0.9141178131103516, 0.9132983088493347, 0.911190927028656, 0.9078671932220459, 0.9074690937995911, 0.9059358239173889, 0.8979107141494751, 0.8964638113975525, 0.8959088921546936, 0.893210768699646, 0.8894509077072144, 0.8862922787666321, 0.8852349519729614, 0.8848482370376587, 0.8844396471977234, 0.8811818957328796, 0.8791674375534058, 0.8777161240577698, 0.8738830089569092, 0.8729515075683594, 0.8690993189811707, 0.8690070509910583, 0.8689265251159668, 0.8685441613197327, 0.8632808327674866, 0.86064612865448, 0.860182523727417, 0.8600972890853882, 0.8599745035171509, 0.857638418674469, 0.8571370840072632, 0.8570400476455688, 0.8564556837081909, 0.8543670773506165, 0.8533570170402527, 0.84917151927948]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.2595562934875488})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.6116554737091064})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.4235004782676697})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.35932019352912903})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.386593759059906})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3255805969238281})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3331681787967682})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3571731448173523})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3732900023460388})
store['active_learning_steps'][8]['training']['best_epoch']=6
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.9584, 'crossentropy': 0.3362562744140625}
store['active_learning_steps'][8]['acquisition']={'indices': [17079, 54858, 43745, 9390, 48006, 33484, 12297, 36818, 47288, 25008, 7438, 54950, 56643, 12305, 17540, 13376, 52392, 58422, 48842, 18405, 23008, 35326, 17010, 51238, 51464, 57728, 33505, 43609, 46368, 5868, 24424, 12018, 47291, 20170, 2991, 58832, 35474, 47595, 40874, 12903, 50231, 55310, 8693, 18042, 27358, 50840, 33358, 635, 5308, 57665], 'labels': [6, 3, 8, 9, 6, 6, 9, 7, 6, 8, 7, 8, 2, 9, 1, 3, 1, 9, 8, 9, 8, 5, 3, 2, 0, 9, 2, 8, 8, 9, 1, 7, 1, 9, 8, 3, 7, 7, 6, 9, 8, 1, 3, 0, 8, 2, 9, 5, 7, 8], 'scores': [0.9160706996917725, 0.9084032773971558, 0.906954288482666, 0.8997288346290588, 0.890073835849762, 0.8837393522262573, 0.8775855898857117, 0.8755868673324585, 0.872467577457428, 0.8721736669540405, 0.8700498342514038, 0.8671450614929199, 0.8595969676971436, 0.8561099171638489, 0.8556545972824097, 0.849487841129303, 0.8491233587265015, 0.8429275751113892, 0.8411906361579895, 0.8377807140350342, 0.8366451859474182, 0.8342232704162598, 0.8319616913795471, 0.8315435647964478, 0.8232703804969788, 0.8217282891273499, 0.8210091590881348, 0.8209784626960754, 0.8191948533058167, 0.8163763284683228, 0.8159607648849487, 0.8142133355140686, 0.8138195872306824, 0.8134149312973022, 0.8115102648735046, 0.8104660511016846, 0.8101950287818909, 0.8052281737327576, 0.8037500977516174, 0.8034749627113342, 0.8031710386276245, 0.8026173114776611, 0.802047610282898, 0.8007861971855164, 0.7979153394699097, 0.7965731024742126, 0.7957117557525635, 0.7952420711517334, 0.7950716614723206, 0.7942943572998047]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7900390625, 'crossentropy': 1.1870369911193848})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.5300173759460449})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.4207567572593689})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3814675807952881})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.332817018032074})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3169217109680176})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.30771833658218384})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2839915156364441})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.28980982303619385})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2819802165031433})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.27307721972465515})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3024199604988098})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.29244697093963623})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.31439247727394104})
store['active_learning_steps'][9]['training']['best_epoch']=11
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.9659, 'crossentropy': 0.3062811767578125}
