store = {}
store['timestamp']=1620258834
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/uniform_target_ood_experiment.py', '--id=14']
store['commit']='8c7fc12bfba938daba445c0e68d9f8cf97c14443'
store['github_url']='8c7fc12bfba938daba445c0e68d9f8cf97c14443'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/uniform_target_ood_experiment.py'
store['job_id']=14
store['worker_id']=14
store['num_workers']=40
store['config']={'seed': 17, 'acquisition_size': 20, 'max_training_set': 450, 'num_pool_samples': 50, 'num_eval_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'validation_set_size': 1024, 'validation_split_random_state': 0, 'initial_training_set_size': 20, 'min_samples_per_epoch': 5056, 'mnist_repetitions': 1, 'ood_fmnist_repetitions': 1, 'add_dataset_noise': False, 'acquisition_function': 'batchbald_redux.acquisition_functions.TemperedBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationPoolModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 8}
store['log']={}
store['dataset_info']={'training': "(FastMNIST (train; 58976 samples) | one_hot_targets{'num_classes': 10}) + ('OoD Dataset (60000 samples)' | uniform_targets{'num_classes': 10})", 'test': "'FastMNIST (test, 10000 samples)'"}
store['initial_training_set_indices']=[30392, 53434, 12640, 8533, 22304, 37915, 58226, 44119, 3091, 14640, 58125, 39579, 43812, 53689, 52296, 46037, 22015, 40334, 57520, 43803]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 2.342047929763794})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 2.767544746398926})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 3.0798144340515137})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 2.883221387863159})
store['active_learning_steps'][0]['training']['best_epoch']=1
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.6694, 'crossentropy': 2.0522388671875}
store['active_learning_steps'][0]['acquisition']={'indices': [['id', 4147], ['id', 12452], ['id', 5137], ['id', 28838], ['id', 58467], ['id', 55064], ['id', 39134], ['id', 8359], ['id', 36582], ['id', 45710], ['id', 22551], ['id', 39662], ['id', 5762], ['id', 51487], ['id', 2068], ['id', 16997], ['id', 59216], ['id', 37321], ['id', 31191], ['id', 7372]], 'labels': [8, 6, 9, 9, 8, 9, 9, 8, 8, 8, 8, 8, 2, 8, 8, 0, 5, 9, 8, 0], 'scores': [0.8987460136413574, 0.9874816536903381, 0.7479208111763, 1.1444011330604553, 1.2098766565322876, 0.991144597530365, 1.0228415131568909, 0.7927231788635254, 1.0715548396110535, 0.8657576441764832, 0.8462108373641968, 1.018611192703247, 0.742216944694519, 0.681921660900116, 0.880553662776947, 0.9578781127929688, 0.948157012462616, 1.1395225524902344, 0.9350920915603638, 0.996907114982605]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 1.9259686470031738})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 2.058614730834961})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 2.4785614013671875})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 2.850343704223633})
store['active_learning_steps'][1]['training']['best_epoch']=1
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.6771, 'crossentropy': 1.781971875}
store['active_learning_steps'][1]['acquisition']={'indices': [['id', 6389], ['id', 18613], ['id', 20486], ['id', 41025], ['id', 52131], ['id', 41718], ['id', 2018], ['id', 10108], ['id', 49115], ['id', 55794], ['id', 14081], ['id', 28441], ['id', 34391], ['id', 19319], ['id', 20993], ['id', 2206], ['ood', 12187], ['id', 17071], ['id', 56271], ['id', 13845]], 'labels': [5, 2, 6, 5, 5, 8, 7, 6, 2, 5, 2, 3, 5, 5, 2, 4, 7, 2, 9, 6], 'scores': [0.846134603023529, 0.9307118654251099, 0.9747241139411926, 0.6827141642570496, 0.6902887225151062, 0.6756371259689331, 0.757433295249939, 0.5892816185951233, 0.9417687654495239, 0.7086800932884216, 0.8685092329978943, 0.6217244267463684, 0.6978278756141663, 0.633755624294281, 0.9892396330833435, 0.5376167297363281, 0.4524143934249878, 0.9055135250091553, 0.5532370805740356, 0.8797133564949036]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.724609375, 'crossentropy': 1.4335012435913086})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.74609375, 'crossentropy': 1.7034401893615723})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.744140625, 'crossentropy': 1.7444912195205688})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.7255859375, 'crossentropy': 2.0805492401123047})
store['active_learning_steps'][2]['training']['best_epoch']=1
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.7265, 'crossentropy': 1.32851689453125}
store['active_learning_steps'][2]['acquisition']={'indices': [['id', 3762], ['id', 55450], ['id', 43143], ['id', 20653], ['id', 1178], ['id', 19959], ['id', 46651], ['id', 17751], ['id', 43656], ['id', 13333], ['id', 49217], ['id', 2455], ['id', 7236], ['id', 31103], ['id', 11711], ['id', 37467], ['id', 46746], ['id', 17357], ['id', 53711], ['id', 54889]], 'labels': [8, 5, 7, 4, 3, 5, 9, 8, 8, 7, 8, 7, 7, 8, 2, 0, 0, 4, 3, 8], 'scores': [0.8254016637802124, 0.6496729850769043, 0.61170494556427, 0.6068322062492371, 0.5575153827667236, 0.7534818053245544, 0.5116325616836548, 0.44210779666900635, 0.7429212331771851, 0.7830846905708313, 0.7102798223495483, 0.7676215171813965, 0.533967912197113, 0.6333234310150146, 0.5541805624961853, 0.5686240792274475, 0.7401939034461975, 0.6622453331947327, 0.49726736545562744, 0.5853294134140015]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7529296875, 'crossentropy': 1.1824729442596436})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.8046875, 'crossentropy': 1.214720368385315})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7880859375, 'crossentropy': 1.3785316944122314})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7998046875, 'crossentropy': 1.341552495956421})
store['active_learning_steps'][3]['training']['best_epoch']=1
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.7873, 'crossentropy': 1.01615595703125}
store['active_learning_steps'][3]['acquisition']={'indices': [['id', 10455], ['id', 57255], ['id', 18386], ['id', 2481], ['id', 380], ['id', 32547], ['id', 54587], ['id', 15848], ['id', 12514], ['id', 46923], ['id', 3988], ['id', 46070], ['id', 14915], ['id', 41254], ['id', 36190], ['id', 4767], ['id', 39461], ['ood', 49292], ['id', 49769], ['id', 5679]], 'labels': [1, 7, 2, 3, 4, 5, 3, 3, 2, 3, 5, 3, 9, 9, 4, 8, 3, 5, 6, 3], 'scores': [0.45284783840179443, 0.3792296051979065, 0.4418288469314575, 0.5522175431251526, 0.4389125108718872, 0.5622337460517883, 0.5573167204856873, 0.5778472423553467, 0.632264256477356, 0.591251015663147, 0.6147009134292603, 0.5603253245353699, 0.5875533223152161, 0.5420782566070557, 0.4378194808959961, 0.7457493543624878, 0.6201179027557373, 0.3877127170562744, 0.4214956760406494, 0.616712212562561]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 0.8752428889274597})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.7850840091705322})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.7902705669403076})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.8565054535865784})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.9031306505203247})
store['active_learning_steps'][4]['training']['best_epoch']=2
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.8774, 'crossentropy': 0.728609521484375}
store['active_learning_steps'][4]['acquisition']={'indices': [['ood', 56265], ['id', 45256], ['id', 57435], ['id', 43123], ['id', 19909], ['ood', 2205], ['id', 1029], ['id', 31650], ['id', 43906], ['id', 15679], ['id', 2658], ['id', 39363], ['ood', 26167], ['id', 37974], ['id', 13703], ['id', 5170], ['id', 667], ['id', 10258], ['id', 14355], ['id', 23484]], 'labels': [8, 5, 0, 4, 5, 8, 0, 5, 4, 2, 7, 0, 3, 2, 3, 8, 0, 5, 2, 4], 'scores': [0.31181561946868896, 0.8588829040527344, 0.7191275358200073, 0.45938658714294434, 0.6400946974754333, 0.36194872856140137, 0.7326779365539551, 0.7401833534240723, 0.7046889066696167, 0.769311785697937, 0.6328827142715454, 0.6646967530250549, 0.424976110458374, 0.8185250759124756, 0.6104791164398193, 0.6400312781333923, 0.6169838309288025, 0.6847906708717346, 0.6544017791748047, 0.4061572551727295]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.8391950130462646})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.6928333640098572})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6821956634521484})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.7326532602310181})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.7853627800941467})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.7807179689407349})
store['active_learning_steps'][5]['training']['best_epoch']=3
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.8962, 'crossentropy': 0.618762744140625}
store['active_learning_steps'][5]['acquisition']={'indices': [['id', 56168], ['id', 47527], ['id', 44446], ['ood', 18578], ['id', 55425], ['id', 37440], ['id', 32926], ['id', 28950], ['id', 10210], ['ood', 40756], ['id', 49537], ['id', 22501], ['id', 3672], ['id', 29481], ['id', 37248], ['id', 23719], ['id', 13983], ['id', 52899], ['id', 15592], ['id', 32537]], 'labels': [2, 1, 1, 5, 7, 2, 8, 2, 3, 4, 2, 9, 2, 2, 4, 9, 3, 7, 9, 5], 'scores': [0.6859003901481628, 0.5730286836624146, 0.7092598080635071, 0.502411961555481, 0.7250418663024902, 0.5460123419761658, 0.5664346814155579, 0.8315712213516235, 0.8171738386154175, 0.31712889671325684, 0.6273910999298096, 0.8719843029975891, 0.7388922572135925, 0.6403100490570068, 0.49413156509399414, 0.6158750653266907, 0.5706871151924133, 0.6356441378593445, 0.5828081369400024, 0.6687502861022949]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.7064709663391113})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.49236562848091125})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5092731714248657})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5348105430603027})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5155138373374939})
store['active_learning_steps'][6]['training']['best_epoch']=2
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.9218, 'crossentropy': 0.483830419921875}
store['active_learning_steps'][6]['acquisition']={'indices': [['id', 28455], ['id', 11346], ['id', 9966], ['id', 11585], ['id', 26762], ['id', 24608], ['id', 33224], ['id', 48786], ['id', 47611], ['id', 59160], ['id', 14844], ['id', 30602], ['id', 31758], ['id', 46080], ['id', 49472], ['id', 46329], ['id', 22364], ['id', 48494], ['id', 33357], ['id', 1863]], 'labels': [5, 2, 0, 4, 8, 5, 1, 4, 6, 5, 9, 4, 8, 8, 7, 3, 0, 8, 3, 3], 'scores': [0.5572750568389893, 0.5200402736663818, 0.5444075465202332, 0.41322171688079834, 0.4902876615524292, 0.364668607711792, 0.5583028793334961, 0.38412290811538696, 0.6444969177246094, 0.6083020567893982, 0.7889043092727661, 0.623240053653717, 0.5016645789146423, 0.6069271564483643, 0.5925760865211487, 0.5989809036254883, 0.5688232183456421, 0.35848820209503174, 0.5155127644538879, 0.47734618186950684]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.743188738822937})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5002068281173706})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5069900155067444})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5060007572174072})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.4905124008655548})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5420820116996765})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.49263083934783936})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.554174542427063})
store['active_learning_steps'][7]['training']['best_epoch']=5
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.9377, 'crossentropy': 0.422940234375}
store['active_learning_steps'][7]['acquisition']={'indices': [['id', 53567], ['ood', 39859], ['id', 18135], ['id', 18739], ['id', 37696], ['id', 55011], ['id', 43001], ['id', 14561], ['id', 42892], ['id', 21442], ['id', 49509], ['id', 40437], ['id', 24887], ['id', 32706], ['id', 8300], ['id', 50155], ['id', 20641], ['id', 17756], ['id', 7786], ['ood', 53491]], 'labels': [5, 5, 2, 3, 2, 2, 9, 1, 7, 4, 8, 8, 5, 9, 8, 5, 9, 8, 0, 7], 'scores': [0.9025373458862305, 0.5416907072067261, 0.6852285861968994, 0.617160975933075, 0.5600026249885559, 0.7798568606376648, 0.5443732142448425, 0.598259687423706, 0.9237763285636902, 0.7823287844657898, 0.9559186100959778, 0.8291153311729431, 0.7815583944320679, 0.5187022984027863, 0.7848984599113464, 0.8144901990890503, 1.039065659046173, 0.7154159545898438, 0.850909948348999, 0.4790174961090088]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.8743177652359009})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.49928727746009827})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5194149613380432})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.4530554413795471})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5029287934303284})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.4632069766521454})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.48761409521102905})
store['active_learning_steps'][8]['training']['best_epoch']=4
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.9408, 'crossentropy': 0.404907861328125}
store['active_learning_steps'][8]['acquisition']={'indices': [['id', 46610], ['id', 42669], ['id', 6893], ['id', 57972], ['id', 4638], ['id', 26208], ['id', 17948], ['id', 11410], ['id', 8865], ['id', 27085], ['id', 13886], ['id', 56321], ['id', 13012], ['id', 27601], ['id', 18003], ['id', 44346], ['id', 4822], ['id', 17190], ['id', 54490], ['id', 424]], 'labels': [5, 3, 9, 4, 3, 3, 8, 5, 3, 8, 5, 3, 9, 9, 2, 6, 4, 9, 6, 9], 'scores': [0.7585852742195129, 0.4406262934207916, 0.6033966541290283, 0.8233845233917236, 0.5636403560638428, 0.7753137350082397, 0.6089767813682556, 0.7540185451507568, 0.5773609280586243, 0.8681639432907104, 0.629589170217514, 0.7316647171974182, 0.7437100410461426, 0.7449548244476318, 0.5904312133789062, 0.7005811929702759, 0.6847547292709351, 0.6364511847496033, 0.5745657682418823, 1.0033044219017029]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.855805516242981})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.4865776598453522})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.4561086893081665})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.4572581648826599})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.43791070580482483})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.416214257478714})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.501697838306427})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.45961689949035645})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.4796944260597229})
store['active_learning_steps'][9]['training']['best_epoch']=6
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.9463, 'crossentropy': 0.375432666015625}
store['active_learning_steps'][9]['acquisition']={'indices': [['id', 56468], ['id', 23629], ['id', 48548], ['id', 30109], ['id', 14645], ['id', 43126], ['id', 13074], ['id', 1674], ['ood', 38318], ['id', 57276], ['id', 35470], ['id', 10716], ['id', 31482], ['id', 9340], ['id', 17958], ['id', 57728], ['id', 50878], ['id', 22530], ['id', 40708], ['id', 1806]], 'labels': [5, 5, 9, 7, 8, 3, 0, 9, 5, 8, 6, 7, 3, 5, 9, 9, 7, 7, 8, 5], 'scores': [0.6204526424407959, 0.7579767107963562, 0.7748771905899048, 0.8849985599517822, 0.7511737942695618, 0.8501508235931396, 0.7024285793304443, 1.1600572764873505, 0.533402681350708, 0.6959441900253296, 0.7205804586410522, 0.7915955185890198, 0.5581982135772705, 0.770539402961731, 0.833961009979248, 1.1150209307670593, 0.6520712375640869, 0.5744093060493469, 0.7555918097496033, 0.8543978333473206]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 0.8795263767242432})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5076634883880615})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.40336862206459045})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.49036905169487})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.4547649025917053})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.39819246530532837})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.4362083077430725})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.4867013692855835})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4251474440097809})
store['active_learning_steps'][10]['training']['best_epoch']=6
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.9478, 'crossentropy': 0.3406080810546875}
store['active_learning_steps'][10]['acquisition']={'indices': [['id', 47888], ['id', 39943], ['id', 38321], ['id', 46800], ['id', 40312], ['id', 50431], ['id', 1814], ['id', 14715], ['id', 8712], ['id', 52191], ['id', 48618], ['id', 48584], ['id', 1248], ['id', 37161], ['id', 28788], ['id', 21164], ['id', 41714], ['id', 57985], ['id', 18042], ['id', 14062]], 'labels': [8, 4, 3, 9, 0, 3, 4, 4, 5, 3, 9, 9, 4, 3, 8, 2, 4, 4, 0, 8], 'scores': [0.6358451843261719, 0.5986711978912354, 0.6868413090705872, 0.6112139225006104, 0.749895453453064, 0.7244837880134583, 0.6061795949935913, 0.6641485691070557, 0.4953279495239258, 0.503382682800293, 0.5833078622817993, 0.7087572813034058, 0.7315200567245483, 0.7868089079856873, 0.6772958636283875, 0.3787929117679596, 0.7515170574188232, 0.6325202584266663, 0.6698211133480072, 0.6196191310882568]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 0.986116886138916})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5403261780738831})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.45103713870048523})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5312538146972656})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.39461150765419006})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.4595114588737488})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.4567112922668457})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.50289386510849})
store['active_learning_steps'][11]['training']['best_epoch']=5
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.9511, 'crossentropy': 0.333854296875}
store['active_learning_steps'][11]['acquisition']={'indices': [['id', 12739], ['id', 16716], ['id', 11645], ['id', 26405], ['ood', 33849], ['id', 4955], ['id', 28932], ['id', 50006], ['id', 53529], ['id', 41369], ['id', 51764], ['id', 52456], ['id', 50078], ['id', 44964], ['id', 40046], ['id', 13440], ['id', 42838], ['id', 40061], ['id', 55926], ['id', 57882]], 'labels': [9, 2, 3, 9, 1, 2, 2, 5, 5, 9, 5, 2, 9, 5, 7, 8, 9, 7, 3, 0], 'scores': [0.43683141469955444, 0.5568313598632812, 0.7878978252410889, 0.6311582326889038, 0.3487023115158081, 0.805225133895874, 0.6799489259719849, 0.598810613155365, 0.5567827820777893, 0.5593652725219727, 0.8566362261772156, 0.6620784997940063, 0.7746325135231018, 0.6866703629493713, 0.6488575339317322, 0.6516705751419067, 0.6776596307754517, 0.24315151572227478, 0.43859606981277466, 0.6596128940582275]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.787109375, 'crossentropy': 1.0556005239486694})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6046518087387085})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.4281950294971466})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4177570343017578})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.4087914228439331})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.4202989339828491})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.39667075872421265})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.464971125125885})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.4275270700454712})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3859984874725342})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.42270445823669434})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.3938700258731842})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.452960729598999})
store['active_learning_steps'][12]['training']['best_epoch']=10
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.9588, 'crossentropy': 0.3109196044921875}
store['active_learning_steps'][12]['acquisition']={'indices': [['id', 50180], ['id', 24970], ['id', 7995], ['ood', 33473], ['id', 718], ['id', 38974], ['id', 25766], ['id', 34829], ['id', 59303], ['ood', 4381], ['ood', 56850], ['id', 11767], ['id', 24462], ['id', 30792], ['id', 18408], ['id', 7920], ['id', 31545], ['id', 20905], ['id', 10979], ['id', 49064]], 'labels': [8, 1, 8, 1, 4, 1, 8, 5, 8, 5, 0, 4, 2, 4, 7, 2, 5, 8, 6, 8], 'scores': [0.5129375159740448, 0.7981510162353516, 0.7788581848144531, 0.23786425590515137, 0.7952061593532562, 0.710162490606308, 0.7636328935623169, 0.8338040709495544, 0.8521479368209839, 0.5258522629737854, 0.3194493055343628, 0.6094303727149963, 0.6918153762817383, 0.7176305055618286, 0.8239503502845764, 0.7677434384822845, 0.8126856088638306, 0.806840181350708, 0.5330200791358948, 1.0610766410827637]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 0.9300358295440674})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5722049474716187})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.4401470422744751})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.3855997622013092})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.4066828191280365})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.3838704526424408})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.42649078369140625})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.39307093620300293})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.45967674255371094})
store['active_learning_steps'][13]['training']['best_epoch']=6
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.9585, 'crossentropy': 0.3094186279296875}
store['active_learning_steps'][13]['acquisition']={'indices': [['id', 51273], ['id', 45666], ['id', 23020], ['id', 17055], ['id', 47032], ['id', 21094], ['id', 49804], ['id', 38920], ['id', 3524], ['id', 54520], ['id', 5073], ['id', 11885], ['id', 7924], ['id', 27458], ['id', 29810], ['id', 32072], ['id', 8619], ['id', 15141], ['id', 35971], ['id', 59731]], 'labels': [2, 1, 2, 8, 6, 1, 8, 7, 6, 9, 1, 8, 8, 2, 1, 8, 8, 4, 0, 5], 'scores': [0.46139127016067505, 0.6907978653907776, 0.8203123211860657, 0.6826525926589966, 0.6298075914382935, 0.4145970344543457, 0.5519438683986664, 0.819651186466217, 0.5176990032196045, 0.6318771839141846, 0.562868058681488, 0.7102829217910767, 0.7162785530090332, 0.6498986482620239, 0.48410940170288086, 0.6174378395080566, 0.7052094340324402, 0.42043888568878174, 0.5499696731567383, 0.7789194583892822]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 1.122072458267212})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5570787787437439})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.442982017993927})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.3817768394947052})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.37382185459136963})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.3660662770271301})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.34931644797325134})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.36724531650543213})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.36703693866729736})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.3734396696090698})
store['active_learning_steps'][14]['training']['best_epoch']=7
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.9607, 'crossentropy': 0.3181820556640625}
store['active_learning_steps'][14]['acquisition']={'indices': [['id', 55774], ['id', 15276], ['id', 37588], ['id', 30742], ['id', 54943], ['id', 46369], ['id', 33812], ['id', 10038], ['id', 45446], ['id', 22465], ['id', 14044], ['id', 38182], ['id', 20636], ['id', 6254], ['id', 25359], ['id', 45784], ['ood', 29871], ['id', 15548], ['id', 23886], ['id', 39423]], 'labels': [4, 7, 2, 1, 0, 5, 6, 9, 7, 6, 6, 9, 9, 1, 5, 9, 7, 1, 1, 9], 'scores': [0.5035853981971741, 0.7415606379508972, 0.6872036457061768, 0.8080242872238159, 0.6113902926445007, 0.747094988822937, 0.9429635405540466, 0.6126409769058228, 0.7107245326042175, 0.5692484378814697, 0.4720642566680908, 0.6412696242332458, 0.7934200763702393, 0.7766779661178589, 0.4193190038204193, 0.8176522254943848, 0.38361620903015137, 0.6685125827789307, 0.6252732872962952, 0.680085301399231]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 1.0599985122680664})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5938143730163574})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.44977790117263794})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.3699679970741272})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.4083258807659149})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.4231751561164856})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.38196009397506714})
store['active_learning_steps'][15]['training']['best_epoch']=4
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.9609, 'crossentropy': 0.3117007080078125}
store['active_learning_steps'][15]['acquisition']={'indices': [['id', 53997], ['id', 23052], ['id', 644], ['id', 11269], ['id', 42428], ['id', 56842], ['id', 59574], ['id', 19369], ['id', 44428], ['id', 11889], ['id', 49616], ['id', 2292], ['id', 42355], ['id', 32171], ['id', 15191], ['id', 22497], ['id', 51544], ['id', 7030], ['id', 45424], ['id', 44338]], 'labels': [8, 8, 7, 0, 5, 8, 5, 0, 6, 5, 7, 7, 3, 3, 0, 7, 1, 3, 4, 3], 'scores': [0.41892462968826294, 0.3576834201812744, 0.6098302602767944, 0.5570703744888306, 0.6511952877044678, 0.6720042824745178, 0.47423285245895386, 0.6987860798835754, 0.5493901371955872, 0.4761461615562439, 0.670411229133606, 0.5285170078277588, 0.39339369535446167, 0.6307846307754517, 0.6046772003173828, 0.5709282159805298, 0.6923021674156189, 0.704725444316864, 0.5862725973129272, 0.6149944961071014]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 1.0986818075180054})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5670096278190613})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.43061769008636475})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.38885459303855896})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.37232041358947754})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.35875624418258667})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.38038575649261475})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.41075360774993896})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.39739567041397095})
store['active_learning_steps'][16]['training']['best_epoch']=6
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.9606, 'crossentropy': 0.323434765625}
store['active_learning_steps'][16]['acquisition']={'indices': [['id', 2580], ['id', 29672], ['id', 6269], ['id', 7597], ['id', 33057], ['id', 394], ['id', 22149], ['id', 24250], ['id', 7781], ['id', 12066], ['id', 58777], ['id', 24982], ['id', 10534], ['id', 37256], ['id', 58812], ['id', 7058], ['id', 42472], ['id', 1652], ['id', 53558], ['id', 27739]], 'labels': [3, 9, 3, 0, 7, 1, 3, 5, 7, 8, 8, 2, 6, 6, 3, 3, 2, 7, 3, 2], 'scores': [0.5590579509735107, 0.8059988617897034, 0.7953625917434692, 0.8009931445121765, 0.6347557306289673, 0.48527365922927856, 0.754387617111206, 0.7076839208602905, 0.4154863655567169, 0.799923837184906, 0.584393322467804, 0.600259006023407, 0.44272005558013916, 0.5432515740394592, 0.5536811351776123, 0.5533994436264038, 0.5215432643890381, 0.6438527703285217, 0.5627263188362122, 0.6323193311691284]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 1.2153233289718628})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.6234415769577026})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.46792665123939514})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3884889781475067})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.35886305570602417})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3252474367618561})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3294634521007538})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.35169121623039246})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3626914620399475})
store['active_learning_steps'][17]['training']['best_epoch']=6
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.9618, 'crossentropy': 0.290715283203125}
store['active_learning_steps'][17]['acquisition']={'indices': [['id', 148], ['id', 8512], ['id', 35232], ['id', 19576], ['id', 36822], ['id', 31738], ['id', 40548], ['id', 17010], ['id', 41295], ['id', 58832], ['ood', 36482], ['id', 39668], ['id', 23086], ['id', 4062], ['id', 36475], ['id', 14842], ['id', 22083], ['id', 45024], ['id', 2931], ['id', 24660]], 'labels': [7, 1, 8, 9, 1, 8, 4, 3, 9, 3, 8, 8, 8, 5, 2, 9, 2, 5, 3, 5], 'scores': [0.568647027015686, 0.39330434799194336, 0.8138558268547058, 0.7584282755851746, 0.5283640027046204, 0.8824940919876099, 0.6535117626190186, 0.6951079368591309, 0.80814129114151, 0.7454984784126282, 0.49033987522125244, 0.9563037753105164, 0.6739428043365479, 0.7449286580085754, 0.5115343332290649, 0.28006020188331604, 0.711366593837738, 0.6652113199234009, 0.44957399368286133, 0.6571475267410278]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 1.0701552629470825})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6465665102005005})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.4194115400314331})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.38987284898757935})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3349388837814331})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3250253200531006})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.31418415904045105})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3530229926109314})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.35184985399246216})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.34143131971359253})
store['active_learning_steps'][18]['training']['best_epoch']=7
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.9654, 'crossentropy': 0.278799560546875}
store['active_learning_steps'][18]['acquisition']={'indices': [['id', 56098], ['id', 56224], ['id', 42078], ['id', 20930], ['id', 1352], ['id', 42711], ['id', 12581], ['id', 42799], ['id', 14749], ['id', 50753], ['id', 52800], ['id', 12986], ['ood', 10777], ['id', 17222], ['id', 11292], ['id', 48681], ['id', 42953], ['id', 49354], ['id', 44904], ['id', 48824]], 'labels': [6, 5, 4, 2, 9, 4, 4, 2, 0, 2, 9, 5, 1, 8, 1, 2, 4, 0, 4, 8], 'scores': [0.6145374178886414, 0.79255211353302, 0.9064888954162598, 0.7349795699119568, 0.9525167942047119, 0.7039174437522888, 0.6605141162872314, 0.5515252351760864, 0.8551963567733765, 0.48042547702789307, 0.8936537504196167, 0.7907053828239441, 0.36503303050994873, 0.6407915353775024, 0.7125422358512878, 0.7788981199264526, 0.7053056955337524, 0.8984690308570862, 0.7199454307556152, 0.7437846064567566]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.78125, 'crossentropy': 1.145449161529541})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6567057967185974})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.48702406883239746})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.4078481197357178})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.35283467173576355})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.33089613914489746})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3474321961402893})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3361966907978058})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.34960997104644775})
store['active_learning_steps'][19]['training']['best_epoch']=6
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.9621, 'crossentropy': 0.3017350341796875}
store['active_learning_steps'][19]['acquisition']={'indices': [['id', 12868], ['id', 25782], ['id', 28641], ['id', 30522], ['id', 39729], ['id', 37214], ['id', 12471], ['id', 26441], ['id', 51287], ['id', 22053], ['id', 16286], ['id', 23140], ['id', 51118], ['id', 37383], ['id', 49854], ['id', 3582], ['id', 15855], ['id', 4276], ['id', 17620], ['id', 21390]], 'labels': [9, 7, 7, 2, 7, 2, 7, 7, 1, 5, 0, 7, 2, 3, 9, 2, 5, 3, 0, 3], 'scores': [0.5554894804954529, 0.6688909530639648, 0.6968839764595032, 0.6023763120174408, 0.7197633981704712, 0.643297553062439, 0.7029729783535004, 0.6992924213409424, 0.5153940916061401, 0.7770559787750244, 0.6389186382293701, 0.6539919972419739, 0.5650662183761597, 0.6036167144775391, 0.4804670512676239, 0.5237463116645813, 0.6047906875610352, 0.5579705834388733, 0.6260225772857666, 0.7092347145080566]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.767578125, 'crossentropy': 1.2346038818359375})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.6757959127426147})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.4877028465270996})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.36630114912986755})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3611660897731781})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.32440727949142456})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2896750569343567})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.31519049406051636})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2900334596633911})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.27549585700035095})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2899206578731537})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.27877989411354065})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2893710136413574})
store['active_learning_steps'][20]['training']['best_epoch']=10
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.9698, 'crossentropy': 0.2526650146484375}
store['active_learning_steps'][20]['acquisition']={'indices': [['id', 27576], ['id', 40481], ['id', 33221], ['id', 52358], ['id', 7678], ['id', 23812], ['id', 44534], ['id', 38316], ['id', 31793], ['id', 47140], ['id', 36550], ['id', 4382], ['id', 52392], ['id', 37078], ['id', 28992], ['id', 5315], ['id', 52727], ['id', 32112], ['id', 22579], ['id', 57732]], 'labels': [5, 3, 5, 2, 3, 3, 9, 4, 4, 3, 9, 4, 1, 8, 0, 3, 4, 4, 2, 9], 'scores': [0.7906767725944519, 0.6287047863006592, 0.5639261305332184, 0.9376236796379089, 0.7536935806274414, 0.7788372039794922, 0.6088396310806274, 0.5966986417770386, 0.6341181695461273, 0.7544712722301483, 0.6096293330192566, 0.8485276699066162, 0.758858323097229, 0.8375142216682434, 0.5757197141647339, 0.87541663646698, 0.9893957376480103, 0.32603222131729126, 0.7318538129329681, 0.4598311185836792]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 1.0939927101135254})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5935041904449463})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.41376441717147827})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3363618552684784})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3190201222896576})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2661541998386383})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.27382272481918335})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2722571790218353})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.28759944438934326})
store['active_learning_steps'][21]['training']['best_epoch']=6
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.9724, 'crossentropy': 0.2533098876953125}
store['active_learning_steps'][21]['acquisition']={'indices': [['id', 28536], ['id', 5155], ['id', 26544], ['id', 47291], ['id', 54104], ['id', 39663], ['id', 56920], ['id', 37023], ['id', 52210], ['id', 20725], ['id', 48006], ['id', 50639], ['id', 33340], ['id', 45954], ['id', 35090], ['id', 34406], ['id', 59747], ['id', 42508], ['id', 38158], ['id', 46521]], 'labels': [3, 4, 4, 1, 0, 2, 7, 1, 5, 8, 6, 8, 5, 8, 2, 4, 5, 3, 8, 6], 'scores': [0.5847560167312622, 0.5220634937286377, 0.551558792591095, 0.6360266208648682, 0.5751134753227234, 0.6358451247215271, 0.473951518535614, 0.5065681338310242, 0.6183476448059082, 0.5213983058929443, 0.5359784960746765, 0.8736560940742493, 0.6205397844314575, 0.7501601576805115, 0.40907448530197144, 0.9383206367492676, 0.7285971641540527, 0.4617351293563843, 0.7602959871292114, 0.5981367230415344]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.7880859375, 'crossentropy': 1.2854866981506348})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.6459650993347168})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.42081141471862793})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.28362345695495605})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.32022786140441895})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2923201322555542})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2644619047641754})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.25842124223709106})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2435857355594635})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.29539430141448975})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.28177410364151})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2869865894317627})
store['active_learning_steps'][22]['training']['best_epoch']=9
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.9732, 'crossentropy': 0.2298468505859375}
