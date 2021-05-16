store = {}
store['timestamp']=1620992117
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/rejection_ood_experiment.py', '--id=0']
store['commit']='7a88a46c213fc419b8e48358058ec72fe5b0f546'
store['github_url']='7a88a46c213fc419b8e48358058ec72fe5b0f546'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/rejection_ood_experiment.py'
store['job_id']=0
store['worker_id']=0
store['num_workers']=20
store['config']={'seed': 1234, 'acquisition_size': 10, 'max_training_set': 450, 'num_pool_samples': 100, 'num_validation_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'validation_set_size': 1024, 'evaluation_set_size': 100, 'validation_split_random_state': 0, 'initial_training_set_size': 20, 'min_samples_per_epoch': 5056, 'mnist_repetitions': 1, 'add_dataset_noise': False, 'acquisition_function': 'batchbald_redux.acquisition_functions.TemperedEvalBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationEvalModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 8}
store['log']={}
store['dataset_info']={'training': "(FastMNIST (train; 58976 samples)) + ('OoD Dataset (60000 samples)' | constant_target{'target': tensor(-1, device='cuda:0'), 'num_classes': 10})", 'test': "'FastMNIST (test, 10000 samples)'"}
store['initial_training_set_indices']=[53434, 8533, 14640, 39579, 30392, 58125, 37915, 3091, 57520, 43803, 44119, 52296, 58226, 40334, 46037, 22015, 22304, 43812, 12640, 53689]
store['evaluation_set_indices']=[29974, 55573, 35472, 44048, 48031, 5616, 10110, 47420, 56990, 34198, 3792, 5715, 15969, 32775, 19757, 34588, 28991, 47417, 26501, 12108, 5573, 48032, 40646, 43252, 2404, 36797, 29079, 40018, 37047, 41512, 45567, 801, 10664, 52801, 42890, 32972, 45974, 20801, 23496, 5803, 10508, 46870, 49549, 306, 38725, 13074, 19689, 27135, 16068, 18137, 2728, 43321, 29950, 380, 27254, 50466, 31965, 24052, 44454, 20076, 21423, 58741, 27145, 38430, 37354, 49986, 4321, 12610, 34482, 35794, 396, 50036, 46861, 57811, 53831, 49304, 51555, 29614, 767, 23451, 49512, 26479, 50997, 1774, 44803, 55187, 30013, 33736, 49169, 46464, 31444, 52440, 33486, 2206, 15675, 54426, 9574, 54012, 28833, 44428]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 2.173092842102051})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 2.454342842102051})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 2.655754566192627})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 2.6076624393463135})
store['active_learning_steps'][0]['training']['best_epoch']=1
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.6905, 'crossentropy': 1.99090078125}
store['active_learning_steps'][0]['eval_training']={}
store['active_learning_steps'][0]['eval_training']['epochs']=[]
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 1.1759510040283203})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 1.126133918762207})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.0919044017791748})
store['active_learning_steps'][0]['eval_training']['best_epoch']=3
store['active_learning_steps'][0]['acquisition']={'indices': [9437, 23730, 19737, 40043, 28127, 12963, 28585, 12120, 13825, 17401], 'labels': [9, 3, 2, 0, 6, 8, 6, -1, -1, 6], 'scores': [0.6764019131660461, 0.7895146608352661, 0.6045947074890137, 0.601856529712677, 0.6624993085861206, 0.8358274102210999, 0.6455262899398804, 0.5078756809234619, 0.5052822828292847, 0.7463016510009766]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 2.0021190643310547})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 2.49564266204834})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 2.6781318187713623})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 2.5847666263580322})
store['active_learning_steps'][1]['training']['best_epoch']=1
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.6884, 'crossentropy': 1.860336328125}
store['active_learning_steps'][1]['eval_training']={}
store['active_learning_steps'][1]['eval_training']['epochs']=[]
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 1.1043922901153564})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 1.133793592453003})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 1.1100869178771973})
store['active_learning_steps'][1]['eval_training']['best_epoch']=1
store['active_learning_steps'][1]['acquisition']={'indices': [47723, 36505, 23370, 19951, 46400, 42495, 55128, 31591, 29308, 14669], 'labels': [8, 2, 2, 8, 2, 8, 8, 8, 5, 8], 'scores': [0.6700044870376587, 0.45035189390182495, 0.41997385025024414, 0.6243601441383362, 0.5752883553504944, 0.595055103302002, 0.526043713092804, 0.47083473205566406, 0.38025474548339844, 0.5455458164215088]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 1.8595554828643799})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 2.473644971847534})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 1.9665913581848145})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 2.6601247787475586})
store['active_learning_steps'][2]['training']['best_epoch']=1
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.6998, 'crossentropy': 1.62426103515625}
store['active_learning_steps'][2]['eval_training']={}
store['active_learning_steps'][2]['eval_training']['epochs']=[]
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 1.0960043668746948})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 1.0428776741027832})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 0.9879586696624756})
store['active_learning_steps'][2]['eval_training']['best_epoch']=3
store['active_learning_steps'][2]['acquisition']={'indices': [5363, 33022, 59491, 38147, 37861, 10986, 55698, 28, 13253, 5265], 'labels': [5, 3, 4, 4, 2, 7, 3, 2, 5, 4], 'scores': [0.4863423705101013, 0.5981625318527222, 0.4978685975074768, 0.6572169065475464, 0.5632590651512146, 0.6380203366279602, 0.6983200311660767, 0.7002071440219879, 0.5382317304611206, 0.6561269760131836]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.78125, 'crossentropy': 1.2141821384429932})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.775390625, 'crossentropy': 1.4129769802093506})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7705078125, 'crossentropy': 1.6637017726898193})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7626953125, 'crossentropy': 1.8250733613967896})
store['active_learning_steps'][3]['training']['best_epoch']=1
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.8057, 'crossentropy': 1.1244369140625}
store['active_learning_steps'][3]['eval_training']={}
store['active_learning_steps'][3]['eval_training']['epochs']=[]
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.7880859375, 'crossentropy': 0.929939866065979})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.798828125, 'crossentropy': 0.8313398361206055})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.7919921875, 'crossentropy': 0.8094028830528259})
store['active_learning_steps'][3]['eval_training']['best_epoch']=3
store['active_learning_steps'][3]['acquisition']={'indices': [17540, 13030, 4792, 15815, 55099, 9858, 48072, 32909, 19717, 38080], 'labels': [1, 0, 3, 3, 5, 5, 9, 9, 5, 2], 'scores': [0.7153012156486511, 0.8218119144439697, 0.6565911769866943, 0.5493017435073853, 0.6050543785095215, 0.5179299116134644, 0.6015759706497192, 0.5247323513031006, 0.5197082161903381, 0.7550718784332275]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7421875, 'crossentropy': 1.5243306159973145})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7431640625, 'crossentropy': 1.6196560859680176})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7705078125, 'crossentropy': 1.5487785339355469})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.767578125, 'crossentropy': 1.8644659519195557})
store['active_learning_steps'][4]['training']['best_epoch']=1
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.7491, 'crossentropy': 1.3188982421875}
store['active_learning_steps'][4]['eval_training']={}
store['active_learning_steps'][4]['eval_training']['epochs']=[]
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.7333984375, 'crossentropy': 1.0348396301269531})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.7431640625, 'crossentropy': 0.9753530025482178})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.75, 'crossentropy': 0.9147803783416748})
store['active_learning_steps'][4]['eval_training']['best_epoch']=3
store['active_learning_steps'][4]['acquisition']={'indices': [55998, 20630, 2102, 47745, 28053, 43038, 10005, 34239, 43081, 43], 'labels': [3, 8, 7, -1, 7, 4, 0, 3, 0, 9], 'scores': [0.39152294397354126, 0.4548611640930176, 0.4849386215209961, 0.3137410879135132, 0.4218215346336365, 0.30677932500839233, 0.5644204616546631, 0.3830719590187073, 0.5028685331344604, 0.499850869178772]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.798828125, 'crossentropy': 1.029252052307129})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 1.0015002489089966})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 1.1519495248794556})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 1.4458842277526855})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 1.211017370223999})
store['active_learning_steps'][5]['training']['best_epoch']=2
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.8574, 'crossentropy': 0.97479638671875}
store['active_learning_steps'][5]['eval_training']={}
store['active_learning_steps'][5]['eval_training']['epochs']=[]
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 0.7899184823036194})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 0.6709731817245483})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 0.6495674848556519})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 0.6147555112838745})
store['active_learning_steps'][5]['eval_training']['best_epoch']=4
store['active_learning_steps'][5]['acquisition']={'indices': [42485, 77, 23863, 15328, 39971, 14043, 16073, 12377, 52753, 47535], 'labels': [-1, 1, 9, 2, 8, 2, 8, 3, 3, 1], 'scores': [0.4298529624938965, 0.5855686664581299, 0.7708682417869568, 0.5136319994926453, 0.6787880659103394, 0.6188644170761108, 0.6680946946144104, 0.7005528807640076, 0.48436325788497925, 0.45088082551956177]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.79296875, 'crossentropy': 1.0132423639297485})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 1.0170679092407227})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 1.1927365064620972})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 1.147958517074585})
store['active_learning_steps'][6]['training']['best_epoch']=1
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.8039, 'crossentropy': 0.933624609375}
store['active_learning_steps'][6]['eval_training']={}
store['active_learning_steps'][6]['eval_training']['epochs']=[]
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 0.824772298336029})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 0.7541424036026001})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 0.7531018257141113})
store['active_learning_steps'][6]['eval_training']['best_epoch']=3
store['active_learning_steps'][6]['acquisition']={'indices': [9016, 43065, 39546, 5086, 23720, 12980, 28562, 19298, 24278, 16590], 'labels': [6, 3, 1, 3, 6, 6, 7, 6, 3, 6], 'scores': [0.49592697620391846, 0.471081018447876, 0.3401305675506592, 0.47300922870635986, 0.4401620626449585, 0.5887656211853027, 0.46635711193084717, 0.6285169124603271, 0.4179072380065918, 0.4116930365562439]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 0.8445252180099487})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 0.9092769622802734})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.863025426864624})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.9374362230300903})
store['active_learning_steps'][7]['training']['best_epoch']=1
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.8388, 'crossentropy': 0.819665625}
store['active_learning_steps'][7]['eval_training']={}
store['active_learning_steps'][7]['eval_training']['epochs']=[]
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 0.8199782371520996})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 0.7543543577194214})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 0.7379591464996338})
store['active_learning_steps'][7]['eval_training']['best_epoch']=3
store['active_learning_steps'][7]['acquisition']={'indices': [34713, 4694, 2738, 47766, 13538, 39864, 41714, 37843, 47849, 59720], 'labels': [3, 3, 2, 9, 5, 8, 4, 1, 7, 2], 'scores': [0.3966793417930603, 0.6386057138442993, 0.31604892015457153, 0.26854878664016724, 0.4753403663635254, 0.43759685754776, 0.3710096478462219, 0.3704349994659424, 0.24188005924224854, 0.3525727391242981]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 0.8595046401023865})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.8756795525550842})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.8119159936904907})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.9612012505531311})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.9252275228500366})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 1.0018188953399658})
store['active_learning_steps'][8]['training']['best_epoch']=3
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.8828, 'crossentropy': 0.769673291015625}
store['active_learning_steps'][8]['eval_training']={}
store['active_learning_steps'][8]['eval_training']['epochs']=[]
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.7849042415618896})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.5969265103340149})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.5182769298553467})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.5168280005455017})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.506090521812439})
store['active_learning_steps'][8]['eval_training']['best_epoch']=5
store['active_learning_steps'][8]['acquisition']={'indices': [5247, 54510, 51362, 13902, 22609, 45482, 8479, 38038, 38185, 34916], 'labels': [2, 5, 5, 4, 6, 5, 5, 5, 6, 7], 'scores': [0.6264544129371643, 0.5008720755577087, 0.5955511331558228, 0.5642335712909698, 0.6328839063644409, 0.5447729229927063, 0.6333692669868469, 0.5457608699798584, 0.4919024705886841, 0.5022454261779785]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 0.7986537218093872})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.6687520742416382})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.7538869976997375})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.7362223863601685})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6895357370376587})
store['active_learning_steps'][9]['training']['best_epoch']=2
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.8847, 'crossentropy': 0.708715478515625}
store['active_learning_steps'][9]['eval_training']={}
store['active_learning_steps'][9]['eval_training']['epochs']=[]
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 0.7731506824493408})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.5807850956916809})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.5377013683319092})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.5467665195465088})
store['active_learning_steps'][9]['eval_training']['best_epoch']=3
store['active_learning_steps'][9]['acquisition']={'indices': [39442, 19972, 23743, 32240, 523, 31040, 55612, 32453, 29370, 26730], 'labels': [8, 9, 9, -1, -1, 6, 9, 8, 6, 9], 'scores': [0.4099694490432739, 0.5043903589248657, 0.3360181450843811, 0.33617961406707764, 0.2697070837020874, 0.6287422180175781, 0.4847906827926636, 0.5358309745788574, 0.2812782824039459, 0.5938969850540161]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.7788227200508118})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6713135838508606})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.7037408351898193})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.7610737085342407})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.7109715938568115})
store['active_learning_steps'][10]['training']['best_epoch']=2
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.8917, 'crossentropy': 0.64927890625}
store['active_learning_steps'][10]['eval_training']={}
store['active_learning_steps'][10]['eval_training']['epochs']=[]
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.7196905612945557})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.5589517951011658})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.516525149345398})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.48685407638549805})
store['active_learning_steps'][10]['eval_training']['best_epoch']=4
store['active_learning_steps'][10]['acquisition']={'indices': [20703, 7438, 29664, 41982, 4762, 14589, 57154, 50052, 56300, 32104], 'labels': [7, 7, 0, 9, 3, 0, 0, 2, 9, 7], 'scores': [0.45222562551498413, 0.5276010632514954, 0.46790021657943726, 0.38734328746795654, 0.47792166471481323, 0.34668105840682983, 0.451957643032074, 0.7889247536659241, 0.46196168661117554, 0.48212194442749023]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.7778908610343933})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.6528007984161377})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.7386538982391357})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6864968538284302})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.7658809423446655})
store['active_learning_steps'][11]['training']['best_epoch']=2
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.8931, 'crossentropy': 0.620291552734375}
store['active_learning_steps'][11]['eval_training']={}
store['active_learning_steps'][11]['eval_training']['epochs']=[]
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.7428717613220215})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.597455620765686})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.5314526557922363})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.4810032248497009})
store['active_learning_steps'][11]['eval_training']['best_epoch']=4
store['active_learning_steps'][11]['acquisition']={'indices': [28248, 10153, 22662, 14833, 9727, 3470, 37838, 10450, 24462, 31450], 'labels': [4, 4, 7, 7, 2, 2, 2, 3, 2, 3], 'scores': [0.2667863965034485, 0.38494056463241577, 0.32937657833099365, 0.38318508863449097, 0.3766632676124573, 0.4568045735359192, 0.46158844232559204, 0.3464158773422241, 0.39227187633514404, 0.31873732805252075]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.7817695140838623})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.5808590650558472})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5698980093002319})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6822736263275146})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6849555969238281})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.7376386523246765})
store['active_learning_steps'][12]['training']['best_epoch']=3
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.912, 'crossentropy': 0.576180615234375}
store['active_learning_steps'][12]['eval_training']={}
store['active_learning_steps'][12]['eval_training']['epochs']=[]
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 0.7313188314437866})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.5444806218147278})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.4568858742713928})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.4579210877418518})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.4435630142688751})
store['active_learning_steps'][12]['eval_training']['best_epoch']=5
store['active_learning_steps'][12]['acquisition']={'indices': [15099, 41018, 26879, 10211, 57403, 49563, 45334, 49438, 19350, 16834], 'labels': [-1, 6, -1, 5, 5, 8, -1, 8, 8, 5], 'scores': [0.5554488897323608, 0.5813082456588745, 0.38785064220428467, 0.5419524312019348, 0.4822610020637512, 0.6142949461936951, 0.23006772994995117, 0.5561838150024414, 0.3881477117538452, 0.48803794384002686]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.8616756200790405})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5600817203521729})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.5937525033950806})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6347638368606567})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6036987900733948})
store['active_learning_steps'][13]['training']['best_epoch']=2
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.9224, 'crossentropy': 0.513645361328125}
store['active_learning_steps'][13]['eval_training']={}
store['active_learning_steps'][13]['eval_training']['epochs']=[]
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.7213894128799438})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.5389798879623413})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.5391941666603088})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5003958940505981})
store['active_learning_steps'][13]['eval_training']['best_epoch']=4
store['active_learning_steps'][13]['acquisition']={'indices': [14042, 13273, 18669, 42826, 54932, 8887, 29669, 54592, 425, 15805], 'labels': [9, 1, -1, -1, 5, 4, 1, 9, 3, 1], 'scores': [0.4739621877670288, 0.47633397579193115, 0.3426817059516907, 0.3160727024078369, 0.41840994358062744, 0.5421196222305298, 0.34860366582870483, 0.42681360244750977, 0.24729925394058228, 0.46035993099212646]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.8105939030647278})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.5925490856170654})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.577144980430603})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5898340940475464})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6083499193191528})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6949699521064758})
store['active_learning_steps'][14]['training']['best_epoch']=3
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.9173, 'crossentropy': 0.528411181640625}
store['active_learning_steps'][14]['eval_training']={}
store['active_learning_steps'][14]['eval_training']['epochs']=[]
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.6673030853271484})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.4866562783718109})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.4589076042175293})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.433367520570755})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.42054009437561035})
store['active_learning_steps'][14]['eval_training']['best_epoch']=5
store['active_learning_steps'][14]['acquisition']={'indices': [16823, 39524, 13823, 16796, 29185, 58071, 14394, 53656, 41572, 52975], 'labels': [7, -1, -1, -1, 3, -1, 3, 2, 6, 2], 'scores': [0.5895321369171143, 0.40331190824508667, 0.35007619857788086, 0.3992237448692322, 0.5082147717475891, 0.4229806661605835, 0.6496800184249878, 0.5538972616195679, 0.48373210430145264, 0.3991738557815552]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.775221049785614})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6539119482040405})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5634287595748901})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5819570422172546})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6111449003219604})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.6468521356582642})
store['active_learning_steps'][15]['training']['best_epoch']=3
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.9186, 'crossentropy': 0.522062646484375}
store['active_learning_steps'][15]['eval_training']={}
store['active_learning_steps'][15]['eval_training']['epochs']=[]
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.7334741353988647})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.4601307213306427})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.4523865580558777})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.4469837546348572})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.40884968638420105})
store['active_learning_steps'][15]['eval_training']['best_epoch']=5
store['active_learning_steps'][15]['acquisition']={'indices': [35464, 55906, 59361, 57564, 34743, 21256, 216, 14201, 29018, 10114], 'labels': [9, 2, 8, 7, 9, 0, 0, 7, -1, 4], 'scores': [0.43520355224609375, 0.35827988386154175, 0.4757562279701233, 0.4405871033668518, 0.5259366631507874, 0.5098703503608704, 0.5519378185272217, 0.48952633142471313, 0.3421281576156616, 0.3855152726173401]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.744198203086853})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5497344136238098})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5264631509780884})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5743958353996277})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.561157763004303})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.5283981561660767})
store['active_learning_steps'][16]['training']['best_epoch']=3
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.9247, 'crossentropy': 0.492762646484375}
store['active_learning_steps'][16]['eval_training']={}
store['active_learning_steps'][16]['eval_training']['epochs']=[]
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.7084461450576782})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.524671733379364})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.4357795715332031})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.43710482120513916})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.4343827962875366})
store['active_learning_steps'][16]['eval_training']['best_epoch']=5
store['active_learning_steps'][16]['acquisition']={'indices': [44432, 45687, 24059, 10744, 4053, 17712, 43772, 5129, 34090, 35629], 'labels': [1, 3, 3, 7, 3, 3, 5, 2, 9, -1], 'scores': [0.4591587781906128, 0.558320939540863, 0.5255287289619446, 0.3954135775566101, 0.44364306330680847, 0.5277594923973083, 0.5676634311676025, 0.5950228571891785, 0.5130462646484375, 0.3583866357803345]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.7748482823371887})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.5652886629104614})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5745151042938232})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.589786171913147})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.539197564125061})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5841090083122253})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.641807496547699})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.6376410126686096})
store['active_learning_steps'][17]['training']['best_epoch']=5
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.9329, 'crossentropy': 0.474173095703125}
store['active_learning_steps'][17]['eval_training']={}
store['active_learning_steps'][17]['eval_training']['epochs']=[]
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.7387058734893799})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.4525017738342285})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.42759329080581665})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.403167724609375})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.4115273058414459})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.36597931385040283})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.3831605911254883})
store['active_learning_steps'][17]['eval_training']['best_epoch']=6
store['active_learning_steps'][17]['acquisition']={'indices': [3811, 57195, 14581, 25835, 18610, 34193, 58165, 42139, 36744, 59916], 'labels': [1, 3, 7, 8, 9, -1, -1, 4, 1, 8], 'scores': [0.34666872024536133, 0.38502779603004456, 0.48945149779319763, 0.2654663324356079, 0.3875044882297516, 0.307087779045105, 0.3453359603881836, 0.3871304988861084, 0.5352815389633179, 0.6006748676300049]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 0.8662151098251343})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.5941505432128906})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.585594654083252})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5807032585144043})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6731544733047485})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.6170523166656494})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.6446999311447144})
store['active_learning_steps'][18]['training']['best_epoch']=4
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.9116, 'crossentropy': 0.54873759765625}
store['active_learning_steps'][18]['eval_training']={}
store['active_learning_steps'][18]['eval_training']['epochs']=[]
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.7046726942062378})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5029267072677612})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.4314579367637634})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.4481981694698334})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.41107726097106934})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.40915822982788086})
store['active_learning_steps'][18]['eval_training']['best_epoch']=6
store['active_learning_steps'][18]['acquisition']={'indices': [7168, 49474, 53979, 15613, 55090, 33338, 1325, 5851, 10705, 58002], 'labels': [8, 2, 8, 4, 7, 8, 5, 7, 0, 0], 'scores': [0.6286032199859619, 0.35069701075553894, 0.5437100529670715, 0.5825343430042267, 0.4041252136230469, 0.5486001968383789, 0.6039478778839111, 0.5225510001182556, 0.6030964255332947, 0.40618300437927246]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 0.848943293094635})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5008209943771362})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.4522089958190918})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.43909603357315063})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.4617931842803955})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.48259955644607544})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.514985978603363})
store['active_learning_steps'][19]['training']['best_epoch']=4
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.9437, 'crossentropy': 0.4016652099609375}
store['active_learning_steps'][19]['eval_training']={}
store['active_learning_steps'][19]['eval_training']['epochs']=[]
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6600552797317505})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.4724678695201874})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.4275898039340973})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.3817332684993744})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.3552350103855133})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.3673115372657776})
store['active_learning_steps'][19]['eval_training']['best_epoch']=5
store['active_learning_steps'][19]['acquisition']={'indices': [23350, 1990, 39700, 38276, 9782, 28194, 36341, 51896, 11308, 14619], 'labels': [8, -1, 5, -1, 8, -1, -1, -1, -1, 3], 'scores': [0.6336162686347961, 0.5206362009048462, 0.49456310272216797, 0.5344988107681274, 0.46096718311309814, 0.5029922723770142, 0.37911033630371094, 0.3387981653213501, 0.24422907829284668, 0.43656566739082336]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.8807562589645386})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.4927859306335449})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5239693522453308})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.4524553120136261})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.4666163921356201})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5023261308670044})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5302324891090393})
store['active_learning_steps'][20]['training']['best_epoch']=4
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.9352, 'crossentropy': 0.435521337890625}
store['active_learning_steps'][20]['eval_training']={}
store['active_learning_steps'][20]['eval_training']['epochs']=[]
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.7586307525634766})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.4925016462802887})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.4407620429992676})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.39904505014419556})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.3846209645271301})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.36008092761039734})
store['active_learning_steps'][20]['eval_training']['best_epoch']=6
store['active_learning_steps'][20]['acquisition']={'indices': [35264, 32918, 29712, 59081, 51268, 30508, 53950, 33780, 48503, 5216], 'labels': [8, 2, -1, -1, -1, 1, -1, 8, 8, 2], 'scores': [0.4617924392223358, 0.4283329248428345, 0.27785634994506836, 0.24409985542297363, 0.23725485801696777, 0.4765840172767639, 0.30649662017822266, 0.41774362325668335, 0.3737650513648987, 0.6006707549095154]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 0.9074047803878784})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5049555897712708})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.4565305709838867})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.4881834089756012})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.46676626801490784})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4748219847679138})
store['active_learning_steps'][21]['training']['best_epoch']=3
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.933, 'crossentropy': 0.44114267578125}
store['active_learning_steps'][21]['eval_training']={}
store['active_learning_steps'][21]['eval_training']['epochs']=[]
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6592367887496948})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.47150322794914246})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.4212169051170349})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.38471484184265137})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.39688366651535034})
store['active_learning_steps'][21]['eval_training']['best_epoch']=4
store['active_learning_steps'][21]['acquisition']={'indices': [8579, 23208, 18227, 27453, 10823, 40316, 5052, 59307, 14657, 22903], 'labels': [-1, 4, 3, 7, -1, -1, 0, 3, 4, 3], 'scores': [0.3419687747955322, 0.3142351806163788, 0.31595003604888916, 0.3830823004245758, 0.33863794803619385, 0.4078301191329956, 0.5566632151603699, 0.2617431581020355, 0.4994596242904663, 0.432924747467041]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.9227865934371948})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5851745009422302})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5633771419525146})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.48986345529556274})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5926189422607422})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5316605567932129})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.4911530017852783})
store['active_learning_steps'][22]['training']['best_epoch']=4
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.9325, 'crossentropy': 0.439684130859375}
store['active_learning_steps'][22]['eval_training']={}
store['active_learning_steps'][22]['eval_training']['epochs']=[]
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.685940146446228})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.4559018611907959})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.4059901833534241})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.40068966150283813})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.3621059060096741})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.38613229990005493})
store['active_learning_steps'][22]['eval_training']['best_epoch']=5
store['active_learning_steps'][22]['acquisition']={'indices': [37100, 12368, 24587, 34847, 46368, 52080, 10003, 14266, 37341, 54994], 'labels': [7, 9, 8, 0, 8, 8, -1, 3, 5, 6], 'scores': [0.30390286445617676, 0.4488168954849243, 0.5515419244766235, 0.4649620056152344, 0.5281181931495667, 0.3534471392631531, 0.24197661876678467, 0.6424221992492676, 0.6867408156394958, 0.4966890811920166]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.7987793684005737})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5300806760787964})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.49085745215415955})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.4440278112888336})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.522736132144928})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.4830605387687683})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.4477774500846863})
store['active_learning_steps'][23]['training']['best_epoch']=4
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.9477, 'crossentropy': 0.3989599365234375}
store['active_learning_steps'][23]['eval_training']={}
store['active_learning_steps'][23]['eval_training']['epochs']=[]
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.793070912361145})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.4802587032318115})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.456961452960968})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.40453702211380005})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.37355828285217285})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.3686816692352295})
store['active_learning_steps'][23]['eval_training']['best_epoch']=6
store['active_learning_steps'][23]['acquisition']={'indices': [36188, 966, 21445, 34078, 10520, 2452, 6983, 40022, 13827, 53873], 'labels': [-1, 3, 9, 2, -1, -1, 5, 8, 3, 4], 'scores': [0.28009259700775146, 0.590539813041687, 0.40401947498321533, 0.5084660649299622, 0.46540701389312744, 0.3288699984550476, 0.37651437520980835, 0.5086263418197632, 0.48523932695388794, 0.47199928760528564]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.8721919059753418})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5428573489189148})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.4745331406593323})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.4699321687221527})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.44880497455596924})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5459198355674744})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.4484105706214905})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.4779422879219055})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.5066079497337341})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.5398381352424622})
store['active_learning_steps'][24]['training']['best_epoch']=7
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.95, 'crossentropy': 0.3879238037109375}
store['active_learning_steps'][24]['eval_training']={}
store['active_learning_steps'][24]['eval_training']['epochs']=[]
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.7666385173797607})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.48726069927215576})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.40384459495544434})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.3470582962036133})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.33651426434516907})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3048626184463501})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.3252498209476471})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.3185778856277466})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.297110378742218})
store['active_learning_steps'][24]['eval_training']['best_epoch']=9
store['active_learning_steps'][24]['acquisition']={'indices': [20529, 18480, 40391, 55903, 13195, 51878, 10239, 42334, 7949, 26288], 'labels': [4, 2, 9, 5, -1, -1, 1, 5, -1, 4], 'scores': [0.5937511622905731, 0.4143938422203064, 0.2598646879196167, 0.327806793153286, 0.5194516777992249, 0.42256999015808105, 0.512431263923645, 0.47131049633026123, 0.5226254463195801, 0.6024539470672607]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.9033534526824951})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5093884468078613})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.475436806678772})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.44409286975860596})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.42537909746170044})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.4208599328994751})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.4490126669406891})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.499248743057251})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.44311314821243286})
store['active_learning_steps'][25]['training']['best_epoch']=6
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.9485, 'crossentropy': 0.3773651611328125}
store['active_learning_steps'][25]['eval_training']={}
store['active_learning_steps'][25]['eval_training']['epochs']=[]
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.7129154205322266})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.44451624155044556})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.40835869312286377})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.3530862331390381})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.34459438920021057})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.3281340003013611})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.3044727146625519})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.3029937148094177})
store['active_learning_steps'][25]['eval_training']['best_epoch']=8
store['active_learning_steps'][25]['acquisition']={'indices': [53889, 38912, 26842, 51144, 17771, 14722, 22193, 39877, 55285, 47569], 'labels': [-1, -1, 5, 5, -1, 0, 5, 7, -1, -1], 'scores': [0.2981916666030884, 0.5705116987228394, 0.453593373298645, 0.5021860003471375, 0.5585801601409912, 0.47379112243652344, 0.45688194036483765, 0.5661455392837524, 0.3941202759742737, 0.36835426092147827]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 0.8823926448822021})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5190683007240295})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.4662059545516968})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.4300905466079712})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.4920058250427246})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.4345752000808716})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.429753839969635})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.4278997778892517})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.42051681876182556})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.49275413155555725})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.40302619338035583})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.4784879684448242})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.4895052909851074})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.45352432131767273})
store['active_learning_steps'][26]['training']['best_epoch']=11
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.9548, 'crossentropy': 0.3727034423828125}
store['active_learning_steps'][26]['eval_training']={}
store['active_learning_steps'][26]['eval_training']['epochs']=[]
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.7532353401184082})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.4350866675376892})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.3818151354789734})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.3437577486038208})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.35081946849823})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.3083008825778961})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.30932730436325073})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.2924374043941498})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.2932116389274597})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.30861181020736694})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.2765066623687744})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.28369152545928955})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3083873689174652})
store['active_learning_steps'][26]['eval_training']['best_epoch']=11
store['active_learning_steps'][26]['acquisition']={'indices': [30334, 50736, 55238, 22098, 41578, 28876, 475, 28333, 20065, 30927], 'labels': [9, -1, -1, -1, 8, -1, -1, -1, -1, -1], 'scores': [0.3504716157913208, 0.7534687519073486, 0.563287079334259, 0.6987455487251282, 0.5061278343200684, 0.4115186929702759, 0.5488733053207397, 0.3424638509750366, 0.5662134885787964, 0.47517484426498413]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.8733586072921753})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5151965618133545})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4359961450099945})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4794497489929199})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4203401207923889})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.4753261208534241})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.41455769538879395})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.4338802695274353})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.44709932804107666})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.4506421685218811})
store['active_learning_steps'][27]['training']['best_epoch']=7
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.956, 'crossentropy': 0.373023828125}
store['active_learning_steps'][27]['eval_training']={}
store['active_learning_steps'][27]['eval_training']['epochs']=[]
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.7500957250595093})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.4538455009460449})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.3910076916217804})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.34607505798339844})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.3336567282676697})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.3230454623699188})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.3127336800098419})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.29710352420806885})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.29164591431617737})
store['active_learning_steps'][27]['eval_training']['best_epoch']=9
store['active_learning_steps'][27]['acquisition']={'indices': [6474, 32276, 7101, 59793, 41578, 46274, 14749, 33464, 22066, 34941], 'labels': [6, 3, 8, 8, -1, 7, 0, 0, -1, -1], 'scores': [0.5607731938362122, 0.5381434559822083, 0.4623810648918152, 0.3694363236427307, 0.3387235403060913, 0.42129290103912354, 0.5092307925224304, 0.7168413400650024, 0.4027959108352661, 0.31472063064575195]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.8609625101089478})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.4994877576828003})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.3897678852081299})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.461384117603302})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.44493719935417175})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.42525243759155273})
store['active_learning_steps'][28]['training']['best_epoch']=3
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.9526, 'crossentropy': 0.3593654541015625}
store['active_learning_steps'][28]['eval_training']={}
store['active_learning_steps'][28]['eval_training']['epochs']=[]
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.7533617615699768})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.4994509816169739})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.4198083281517029})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.41289591789245605})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.3813602328300476})
store['active_learning_steps'][28]['eval_training']['best_epoch']=5
store['active_learning_steps'][28]['acquisition']={'indices': [38375, 58328, 22083, 16036, 45026, 49859, 59548, 21012, 35938, 12345], 'labels': [-1, -1, 2, 8, 8, 3, -1, 2, 7, 3], 'scores': [0.38228702545166016, 0.18237972259521484, 0.47325098514556885, 0.3556496500968933, 0.3653110861778259, 0.31663596630096436, 0.42414724826812744, 0.4353622794151306, 0.42045313119888306, 0.38475698232650757]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.90253084897995})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5085870027542114})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.4230842590332031})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.40245553851127625})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.41576361656188965})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.43767249584198})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.4298710227012634})
store['active_learning_steps'][29]['training']['best_epoch']=4
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.9542, 'crossentropy': 0.35690625}
store['active_learning_steps'][29]['eval_training']={}
store['active_learning_steps'][29]['eval_training']['epochs']=[]
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.7896003127098083})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.44051921367645264})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.408183217048645})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3803909420967102})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3889787793159485})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.34065738320350647})
store['active_learning_steps'][29]['eval_training']['best_epoch']=6
store['active_learning_steps'][29]['acquisition']={'indices': [40308, 33062, 5740, 16357, 40169, 30692, 39363, 46804, 20098, 28657], 'labels': [-1, 7, 9, 5, 4, 3, 0, -1, -1, 5], 'scores': [0.28017425537109375, 0.37179136276245117, 0.5412017703056335, 0.4074200391769409, 0.4283970594406128, 0.46128976345062256, 0.5611958503723145, 0.37103545665740967, 0.33400237560272217, 0.42555510997772217]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 0.987442672252655})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5190615057945251})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.43390437960624695})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3864403963088989})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3873264193534851})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.38916245102882385})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.39390915632247925})
store['active_learning_steps'][30]['training']['best_epoch']=4
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.9574, 'crossentropy': 0.341418896484375}
store['active_learning_steps'][30]['eval_training']={}
store['active_learning_steps'][30]['eval_training']['epochs']=[]
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.7014379501342773})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.4865412712097168})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.41804319620132446})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3690919280052185})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3429492115974426})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3211255669593811})
store['active_learning_steps'][30]['eval_training']['best_epoch']=6
store['active_learning_steps'][30]['acquisition']={'indices': [28690, 58586, 25945, 14008, 11162, 37672, 18515, 5103, 6846, 58469], 'labels': [-1, -1, 1, -1, 0, 8, 0, 2, -1, -1], 'scores': [0.4368025064468384, 0.31510138511657715, 0.31164777278900146, 0.3202660083770752, 0.48745250701904297, 0.5189513564109802, 0.544308066368103, 0.5415467619895935, 0.5102128982543945, 0.42441368103027344]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.8921158313751221})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5140623450279236})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.47067517042160034})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.42281240224838257})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.4200016260147095})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.39490318298339844})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.41063517332077026})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3831976056098938})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.40814077854156494})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.42656785249710083})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.44220298528671265})
store['active_learning_steps'][31]['training']['best_epoch']=8
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.9551, 'crossentropy': 0.349632861328125}
store['active_learning_steps'][31]['eval_training']={}
store['active_learning_steps'][31]['eval_training']['epochs']=[]
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.8958908319473267})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5275700688362122})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.40430983901023865})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3534746468067169})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3131446838378906})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.28643643856048584})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3100927174091339})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3101249635219574})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.29087093472480774})
store['active_learning_steps'][31]['eval_training']['best_epoch']=6
store['active_learning_steps'][31]['acquisition']={'indices': [50091, 28930, 17011, 1554, 31934, 59918, 11534, 26241, 6213, 7296], 'labels': [5, 7, 6, 4, 9, 0, 7, -1, 3, -1], 'scores': [0.38614165782928467, 0.4878571927547455, 0.36754173040390015, 0.5386655926704407, 0.549017608165741, 0.4857099652290344, 0.6382841467857361, 0.5361275672912598, 0.44135522842407227, 0.3567647933959961]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.8076171875, 'crossentropy': 1.0938191413879395})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5124374628067017})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.39674121141433716})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3368089497089386})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.37455254793167114})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3785627782344818})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.34363728761672974})
store['active_learning_steps'][32]['training']['best_epoch']=4
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.9601, 'crossentropy': 0.3231430908203125}
store['active_learning_steps'][32]['eval_training']={}
store['active_learning_steps'][32]['eval_training']['epochs']=[]
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.7612442970275879})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.4719807207584381})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.37063562870025635})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.3698311448097229})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.3742448091506958})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.35000282526016235})
store['active_learning_steps'][32]['eval_training']['best_epoch']=6
store['active_learning_steps'][32]['acquisition']={'indices': [12291, 19369, 39304, 37399, 44241, 23814, 48807, 52044, 48975, 54986], 'labels': [-1, -1, 4, -1, -1, -1, -1, -1, 2, 8], 'scores': [0.36890822649002075, 0.3156750202178955, 0.4299873113632202, 0.46012967824935913, 0.3920520544052124, 0.25597554445266724, 0.44185423851013184, 0.5408754348754883, 0.38948678970336914, 0.3797534704208374]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 0.997566282749176})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.5430425405502319})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.4378048777580261})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.4004298448562622})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3585329055786133})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3604573607444763})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.34719687700271606})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3708171248435974})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.39012426137924194})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3587304949760437})
store['active_learning_steps'][33]['training']['best_epoch']=7
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.9611, 'crossentropy': 0.317709130859375}
store['active_learning_steps'][33]['eval_training']={}
store['active_learning_steps'][33]['eval_training']['epochs']=[]
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.829122006893158})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.46393173933029175})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.4065926671028137})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.33514565229415894})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3321017920970917})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.33901721239089966})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.31776154041290283})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3331947922706604})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.30685603618621826})
store['active_learning_steps'][33]['eval_training']['best_epoch']=9
store['active_learning_steps'][33]['acquisition']={'indices': [12305, 30110, 3803, 50397, 3872, 56662, 39516, 41416, 26850, 55188], 'labels': [9, -1, 3, -1, -1, 0, 5, 8, 2, 2], 'scores': [0.6728139519691467, 0.40890389680862427, 0.49219977855682373, 0.37532222270965576, 0.44495177268981934, 0.5653021335601807, 0.661862313747406, 0.2592567801475525, 0.6166775822639465, 0.6208512187004089]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 1.0231328010559082})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5229594707489014})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4653943181037903})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3761149048805237})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3862663507461548})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.40152066946029663})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.41449111700057983})
store['active_learning_steps'][34]['training']['best_epoch']=4
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.9538, 'crossentropy': 0.3404448486328125}
store['active_learning_steps'][34]['eval_training']={}
store['active_learning_steps'][34]['eval_training']['epochs']=[]
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.7669020891189575})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.45650172233581543})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3612692058086395})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.36270689964294434})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3495425581932068})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3240634799003601})
store['active_learning_steps'][34]['eval_training']['best_epoch']=6
store['active_learning_steps'][34]['acquisition']={'indices': [46348, 37018, 2765, 15803, 29672, 21107, 52582, 55874, 1015, 43796], 'labels': [8, -1, 0, 1, 9, -1, 2, -1, 0, 7], 'scores': [0.48682093620300293, 0.35632383823394775, 0.5166754722595215, 0.4165226221084595, 0.38411998748779297, 0.4277452230453491, 0.5435660481452942, 0.4033864140510559, 0.35002875328063965, 0.5026285648345947]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 1.003610372543335})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5248275995254517})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.36499160528182983})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3140287399291992})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.4159459173679352})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.34487587213516235})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3503054082393646})
store['active_learning_steps'][35]['training']['best_epoch']=4
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.9591, 'crossentropy': 0.3133154541015625}
store['active_learning_steps'][35]['eval_training']={}
store['active_learning_steps'][35]['eval_training']['epochs']=[]
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.7992211580276489})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.4438418745994568})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.4056355059146881})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.34752172231674194})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.37301135063171387})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3322945237159729})
store['active_learning_steps'][35]['eval_training']['best_epoch']=6
store['active_learning_steps'][35]['acquisition']={'indices': [36055, 13812, 43135, 27540, 30308, 15893, 58273, 53999, 40973, 26686], 'labels': [-1, 8, -1, -1, 9, 5, 8, 8, -1, 0], 'scores': [0.411837100982666, 0.3997008800506592, 0.37675440311431885, 0.4245692491531372, 0.3982890844345093, 0.3815425634384155, 0.30942755937576294, 0.42148590087890625, 0.22435462474822998, 0.39338409900665283]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 1.0355777740478516})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.5577349662780762})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.41937926411628723})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.33057451248168945})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.35904037952423096})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3214636743068695})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.35676437616348267})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3598749041557312})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.37529245018959045})
store['active_learning_steps'][36]['training']['best_epoch']=6
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.9611, 'crossentropy': 0.320320556640625}
store['active_learning_steps'][36]['eval_training']={}
store['active_learning_steps'][36]['eval_training']['epochs']=[]
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.7377092838287354})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4574592709541321})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.355502188205719})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3357696831226349})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3475446105003357})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3063230514526367})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.2907087802886963})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.32872653007507324})
store['active_learning_steps'][36]['eval_training']['best_epoch']=7
store['active_learning_steps'][36]['acquisition']={'indices': [42071, 31251, 36761, 30851, 40434, 16488, 50320, 9843, 25540, 43512], 'labels': [-1, -1, -1, -1, 5, 9, 5, -1, -1, -1], 'scores': [0.23985064029693604, 0.5647060871124268, 0.7817439436912537, 0.5466727614402771, 0.35168424248695374, 0.4078853130340576, 0.5694147944450378, 0.24655437469482422, 0.40687310695648193, 0.3914310932159424]}
store['active_learning_steps'].append({})
store['active_learning_steps'][37]['training']={}
store['active_learning_steps'][37]['training']['epochs']=[]
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 1.0975505113601685})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.504266083240509})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.403076708316803})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.37199804186820984})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3287409245967865})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3545660376548767})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3340129256248474})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.33486080169677734})
store['active_learning_steps'][37]['training']['best_epoch']=5
store['active_learning_steps'][37]['evaluation_metrics']={'accuracy': 0.9628, 'crossentropy': 0.3179130126953125}
store['active_learning_steps'][37]['eval_training']={}
store['active_learning_steps'][37]['eval_training']['epochs']=[]
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.937026858329773})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.48645442724227905})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.4132087826728821})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.35760095715522766})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3405112624168396})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3043513894081116})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.30826568603515625})
store['active_learning_steps'][37]['eval_training']['best_epoch']=6
store['active_learning_steps'][37]['acquisition']={'indices': [55073, 3738, 37347, 39074, 52099, 13714, 39320, 31293, 31345, 25721], 'labels': [4, 4, 2, -1, 2, 4, 6, 8, 3, -1], 'scores': [0.46752434968948364, 0.4428521394729614, 0.6532939672470093, 0.35420525074005127, 0.547622561454773, 0.45257312059402466, 0.42244216799736023, 0.4316721558570862, 0.5090286135673523, 0.29015350341796875]}
store['active_learning_steps'].append({})
store['active_learning_steps'][38]['training']={}
store['active_learning_steps'][38]['training']['epochs']=[]
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 1.1555229425430298})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.521666407585144})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.40172484517097473})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3489382863044739})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.31064891815185547})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.326266884803772})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.29330456256866455})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3090246319770813})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3614475131034851})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.33062446117401123})
store['active_learning_steps'][38]['training']['best_epoch']=7
store['active_learning_steps'][38]['evaluation_metrics']={'accuracy': 0.966, 'crossentropy': 0.297627734375}
store['active_learning_steps'][38]['eval_training']={}
store['active_learning_steps'][38]['eval_training']['epochs']=[]
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.7688403129577637})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.4573493003845215})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3497290313243866})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.35425224900245667})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.29946884512901306})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.28238099813461304})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2681213617324829})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.26309579610824585})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.25223273038864136})
store['active_learning_steps'][38]['eval_training']['best_epoch']=9
store['active_learning_steps'][38]['acquisition']={'indices': [36562, 29996, 53872, 51900, 51764, 27393, 54296, 47002, 50477, 10690], 'labels': [0, 9, 8, -1, 5, 2, 3, -1, -1, 4], 'scores': [0.4975426197052002, 0.43853759765625, 0.5816406607627869, 0.5267672538757324, 0.693863570690155, 0.3677222728729248, 0.49104464054107666, 0.3114699125289917, 0.34788215160369873, 0.5506578683853149]}
store['active_learning_steps'].append({})
store['active_learning_steps'][39]['training']={}
store['active_learning_steps'][39]['training']['epochs']=[]
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 1.1724047660827637})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5732084512710571})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.4411364793777466})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.35540008544921875})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3442511558532715})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3934597074985504})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.35628920793533325})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3293223977088928})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3740888237953186})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.34937453269958496})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3648684620857239})
store['active_learning_steps'][39]['training']['best_epoch']=8
store['active_learning_steps'][39]['evaluation_metrics']={'accuracy': 0.9632, 'crossentropy': 0.29405625}
store['active_learning_steps'][39]['eval_training']={}
store['active_learning_steps'][39]['eval_training']['epochs']=[]
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.8355244994163513})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.44155097007751465})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.3558257222175598})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3265213966369629})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.2933143973350525})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.2986725866794586})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.27492621541023254})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.2732352018356323})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.2742273807525635})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.2867293953895569})
store['active_learning_steps'][39]['eval_training']['best_epoch']=8
store['active_learning_steps'][39]['acquisition']={'indices': [23684, 59671, 34665, 7832, 51414, 7346, 55436, 51146, 34776, 44829], 'labels': [-1, -1, 9, 3, 8, -1, -1, -1, -1, -1], 'scores': [0.6284615993499756, 0.6226308345794678, 0.39181506633758545, 0.523310661315918, 0.47569870948791504, 0.38561415672302246, 0.4432753324508667, 0.5015687942504883, 0.2358417510986328, 0.5078613758087158]}
store['active_learning_steps'].append({})
store['active_learning_steps'][40]['training']={}
store['active_learning_steps'][40]['training']['epochs']=[]
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 0.992039680480957})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5123231410980225})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3407478630542755})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3537559509277344})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.38011831045150757})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.31160223484039307})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.32499659061431885})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3364745080471039})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.33509308099746704})
store['active_learning_steps'][40]['training']['best_epoch']=6
store['active_learning_steps'][40]['evaluation_metrics']={'accuracy': 0.967, 'crossentropy': 0.282080126953125}
store['active_learning_steps'][40]['eval_training']={}
store['active_learning_steps'][40]['eval_training']['epochs']=[]
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.9372567534446716})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4984810948371887})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3366950452327728})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3206896483898163})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2878008484840393})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3125123679637909})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.28661802411079407})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2619217038154602})
store['active_learning_steps'][40]['eval_training']['best_epoch']=8
store['active_learning_steps'][40]['acquisition']={'indices': [32275, 577, 46277, 6930, 47792, 10754, 40447, 15647, 51889, 32353], 'labels': [-1, -1, -1, 6, 6, -1, -1, -1, -1, -1], 'scores': [0.48796629905700684, 0.3241395950317383, 0.349704384803772, 0.49466264247894287, 0.48985356092453003, 0.34395837783813477, 0.3724958896636963, 0.40260517597198486, 0.5011162757873535, 0.4102952480316162]}
store['active_learning_steps'].append({})
store['active_learning_steps'][41]['training']={}
store['active_learning_steps'][41]['training']['epochs']=[]
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.8892697095870972})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.4940030574798584})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.36444687843322754})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3191152811050415})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.29750919342041016})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.33210447430610657})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.32242947816848755})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3079206347465515})
store['active_learning_steps'][41]['training']['best_epoch']=5
store['active_learning_steps'][41]['evaluation_metrics']={'accuracy': 0.9674, 'crossentropy': 0.288544970703125}
store['active_learning_steps'][41]['eval_training']={}
store['active_learning_steps'][41]['eval_training']['epochs']=[]
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.7782014608383179})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5120320320129395})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3359433114528656})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3436923027038574})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3193565309047699})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.29846006631851196})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.2908969521522522})
store['active_learning_steps'][41]['eval_training']['best_epoch']=7
store['active_learning_steps'][41]['acquisition']={'indices': [47590, 44234, 22930, 19922, 56618, 44178, 43424, 37287, 18598, 54195], 'labels': [-1, 9, -1, -1, -1, -1, 6, -1, 9, -1], 'scores': [0.4229665994644165, 0.4947583079338074, 0.391060471534729, 0.27024245262145996, 0.31453120708465576, 0.35463201999664307, 0.43226897716522217, 0.362895131111145, 0.4939703941345215, 0.3605773448944092]}
store['active_learning_steps'].append({})
store['active_learning_steps'][42]['training']={}
store['active_learning_steps'][42]['training']['epochs']=[]
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 1.1123814582824707})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.4771248996257782})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3586653470993042})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.30361658334732056})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.30677586793899536})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.32181107997894287})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3002462387084961})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3253311514854431})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3397865295410156})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3291783630847931})
store['active_learning_steps'][42]['training']['best_epoch']=7
store['active_learning_steps'][42]['evaluation_metrics']={'accuracy': 0.9667, 'crossentropy': 0.2867920654296875}
store['active_learning_steps'][42]['eval_training']={}
store['active_learning_steps'][42]['eval_training']['epochs']=[]
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.8345411419868469})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4966809153556824})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3695261478424072})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.34621351957321167})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3006190061569214})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.27206775546073914})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.2621711194515228})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.25258466601371765})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2775198817253113})
store['active_learning_steps'][42]['eval_training']['best_epoch']=8
store['active_learning_steps'][42]['acquisition']={'indices': [26358, 43394, 17902, 8800, 15949, 14480, 7003, 36878, 41014, 46324], 'labels': [3, -1, -1, -1, 5, -1, -1, -1, -1, -1], 'scores': [0.7110625505447388, 0.46412181854248047, 0.4329427480697632, 0.45921748876571655, 0.6663797497749329, 0.28363990783691406, 0.3545800447463989, 0.3254600763320923, 0.25033676624298096, 0.26864945888519287]}
store['active_learning_steps'].append({})
store['active_learning_steps'][43]['training']={}
store['active_learning_steps'][43]['training']['epochs']=[]
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.9243833422660828})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.44673997163772583})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3228111267089844})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.31232577562332153})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2923505902290344})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3115929365158081})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2911849021911621})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2842750549316406})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2969662547111511})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2887404263019562})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.32083290815353394})
store['active_learning_steps'][43]['training']['best_epoch']=8
store['active_learning_steps'][43]['evaluation_metrics']={'accuracy': 0.9692, 'crossentropy': 0.2828591796875}
store['active_learning_steps'][43]['eval_training']={}
store['active_learning_steps'][43]['eval_training']['epochs']=[]
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.9106088876724243})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.5245692729949951})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3945065140724182})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3074323832988739})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.27819594740867615})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2695848345756531})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2420116364955902})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.23772546648979187})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.22795814275741577})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2360978126525879})
store['active_learning_steps'][43]['eval_training']['best_epoch']=9
store['active_learning_steps'][43]['acquisition']={'indices': [2574, 44470, 2771, 57718, 59001, 41334, 49354, 5536, 45864, 45616], 'labels': [-1, -1, -1, -1, -1, 9, 0, -1, 9, 5], 'scores': [0.5451736450195312, 0.4021871089935303, 0.4528178572654724, 0.4173710346221924, 0.5163328647613525, 0.5776047110557556, 0.4329666197299957, 0.38871443271636963, 0.5706074833869934, 0.6082854270935059]}
store['active_learning_steps'].append({})
store['active_learning_steps'][44]['training']={}
store['active_learning_steps'][44]['training']['epochs']=[]
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 1.0010230541229248})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.5656850337982178})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.4070442318916321})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.34331756830215454})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.33674395084381104})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.33609941601753235})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3288646936416626})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3185648024082184})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3333866000175476})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.34667813777923584})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3158299922943115})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.32458585500717163})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3326784372329712})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.34848305583000183})
store['active_learning_steps'][44]['training']['best_epoch']=11
store['active_learning_steps'][44]['evaluation_metrics']={'accuracy': 0.9688, 'crossentropy': 0.3082535400390625}
store['active_learning_steps'][44]['eval_training']={}
store['active_learning_steps'][44]['eval_training']['epochs']=[]
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.7770364284515381})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.44760578870773315})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.37188684940338135})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.316405326128006})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.26450592279434204})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2601654529571533})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2558482885360718})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.23935621976852417})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2655441164970398})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2701496183872223})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2433657944202423})
store['active_learning_steps'][44]['eval_training']['best_epoch']=8
store['active_learning_steps'][44]['acquisition']={'indices': [46640, 1740, 39016, 14815, 39822, 29335, 36582, 23066, 17079, 44446], 'labels': [5, 9, -1, 9, 9, -1, -1, -1, 6, 1], 'scores': [-0.3338463343679905, 0.6731500029563904, 0.3618795871734619, 0.5233069658279419, 0.4943355321884155, 0.2685493230819702, 0.46775591373443604, 0.47625958919525146, 0.6405961215496063, 0.4100785255432129]}
store['active_learning_steps'].append({})
store['active_learning_steps'][45]['training']={}
store['active_learning_steps'][45]['training']['epochs']=[]
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.9719107151031494})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.4830043911933899})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.34437036514282227})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3155755400657654})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.3016795516014099})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3073948919773102})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3214660882949829})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.31604570150375366})
store['active_learning_steps'][45]['training']['best_epoch']=5
store['active_learning_steps'][45]['evaluation_metrics']={'accuracy': 0.968, 'crossentropy': 0.2649984130859375}
store['active_learning_steps'][45]['eval_training']={}
store['active_learning_steps'][45]['eval_training']['epochs']=[]
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.7797868847846985})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.4499998986721039})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3421572744846344})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.31955161690711975})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2655424475669861})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2591192424297333})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.277468204498291})
store['active_learning_steps'][45]['eval_training']['best_epoch']=6
store['active_learning_steps'][45]['acquisition']={'indices': [45207, 57742, 51112, 6408, 36464, 11864, 1635, 25429, 25586, 37964], 'labels': [-1, 6, -1, -1, -1, 5, -1, 8, 3, -1], 'scores': [0.4285716414451599, 0.310576856136322, 0.23504328727722168, 0.35673224925994873, 0.29280364513397217, 0.39933741092681885, 0.3169233798980713, 0.3881487548351288, 0.5527983903884888, 0.41054224967956543]}
store['active_learning_steps'].append({})
store['active_learning_steps'][46]['training']={}
store['active_learning_steps'][46]['training']['epochs']=[]
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 1.17348313331604})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.5200312733650208})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.38350266218185425})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.36483460664749146})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.32636502385139465})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3224877119064331})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2854909598827362})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3129315972328186})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.3045516610145569})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.34205424785614014})
store['active_learning_steps'][46]['training']['best_epoch']=7
store['active_learning_steps'][46]['evaluation_metrics']={'accuracy': 0.9694, 'crossentropy': 0.2770063720703125}
store['active_learning_steps'][46]['eval_training']={}
store['active_learning_steps'][46]['eval_training']['epochs']=[]
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.8997691869735718})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.4768230617046356})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3631572723388672})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.29588425159454346})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2901313304901123})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2897999882698059})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2847241461277008})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.23897616565227509})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2683454751968384})
store['active_learning_steps'][46]['eval_training']['best_epoch']=8
store['active_learning_steps'][46]['acquisition']={'indices': [20869, 18294, 50910, 3536, 38347, 23226, 30778, 34442, 33320, 57507], 'labels': [3, -1, 7, -1, -1, -1, -1, -1, -1, 0], 'scores': [0.6634506583213806, 0.5445946455001831, 0.39294278621673584, 0.3943209648132324, 0.2923707962036133, 0.4343833923339844, 0.38487493991851807, 0.2906489372253418, 0.35040605068206787, 0.44006073474884033]}
store['active_learning_steps'].append({})
store['active_learning_steps'][47]['training']={}
store['active_learning_steps'][47]['training']['epochs']=[]
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 1.0251071453094482})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.49804186820983887})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3815918266773224})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.26354217529296875})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3146568536758423})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.29934990406036377})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2719385027885437})
store['active_learning_steps'][47]['training']['best_epoch']=4
store['active_learning_steps'][47]['evaluation_metrics']={'accuracy': 0.9684, 'crossentropy': 0.2841232177734375}
store['active_learning_steps'][47]['eval_training']={}
store['active_learning_steps'][47]['eval_training']['epochs']=[]
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.9578549265861511})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.5660214424133301})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.4566728472709656})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.38667792081832886})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.376151978969574})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3450397551059723})
store['active_learning_steps'][47]['eval_training']['best_epoch']=6
store['active_learning_steps'][47]['acquisition']={'indices': [51934, 39673, 14365, 14602, 31313, 5021, 28633, 49616, 48, 4544], 'labels': [3, 2, 9, 4, -1, -1, 3, 7, 9, 9], 'scores': [0.2910940647125244, 0.3473154306411743, 0.4088001251220703, 0.3206997513771057, 0.2888524532318115, 0.21237671375274658, 0.36638516187667847, 0.46077293157577515, 0.2410494089126587, 0.251064658164978]}
store['active_learning_steps'].append({})
store['active_learning_steps'][48]['training']={}
store['active_learning_steps'][48]['training']['epochs']=[]
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 1.1035661697387695})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4926662743091583})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.36511895060539246})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2818335294723511})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2914794683456421})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.28471043705940247})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2890869975090027})
store['active_learning_steps'][48]['training']['best_epoch']=4
store['active_learning_steps'][48]['evaluation_metrics']={'accuracy': 0.965, 'crossentropy': 0.288283251953125}
store['active_learning_steps'][48]['eval_training']={}
store['active_learning_steps'][48]['eval_training']['epochs']=[]
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.8489475250244141})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5116183757781982})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.37982577085494995})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3695336580276489})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.33047163486480713})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.3387431502342224})
store['active_learning_steps'][48]['eval_training']['best_epoch']=5
store['active_learning_steps'][48]['acquisition']={'indices': [58105, 50314, 18193, 20918, 1870, 20169, 747, 1792, 52201, 5974], 'labels': [4, -1, -1, 9, -1, 4, -1, -1, 8, -1], 'scores': [0.35729682445526123, 0.29136693477630615, 0.5197968482971191, 0.41091257333755493, 0.3534926772117615, 0.636650800704956, 0.3024193048477173, 0.318780779838562, 0.4641948938369751, 0.6097333431243896]}
store['active_learning_steps'].append({})
store['active_learning_steps'][49]['training']={}
store['active_learning_steps'][49]['training']['epochs']=[]
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 1.0624949932098389})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.49186185002326965})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.35057199001312256})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.291037917137146})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.29543304443359375})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.29104214906692505})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.29770445823669434})
store['active_learning_steps'][49]['training']['best_epoch']=4
store['active_learning_steps'][49]['evaluation_metrics']={'accuracy': 0.9639, 'crossentropy': 0.29969228515625}
store['active_learning_steps'][49]['eval_training']={}
store['active_learning_steps'][49]['eval_training']['epochs']=[]
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.7836538553237915})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.4751431345939636})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.3765944242477417})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.37178337574005127})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.368069589138031})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.36184197664260864})
store['active_learning_steps'][49]['eval_training']['best_epoch']=6
store['active_learning_steps'][49]['acquisition']={'indices': [28284, 48973, 43212, 38082, 49537, 52854, 29037, 34528, 43042, 59663], 'labels': [-1, 8, 5, -1, 2, 1, -1, -1, 8, 8], 'scores': [0.18612539768218994, 0.4817206859588623, 0.3973461985588074, 0.3098287582397461, 0.4522460103034973, 0.24315404891967773, 0.22391867637634277, 0.23265016078948975, 0.5360845327377319, 0.4014413356781006]}
store['active_learning_steps'].append({})
store['active_learning_steps'][50]['training']={}
store['active_learning_steps'][50]['training']['epochs']=[]
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 1.0889549255371094})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.5552577972412109})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.3706660866737366})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3691212832927704})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.320949912071228})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2844699025154114})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.30739331245422363})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2769765853881836})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2825695872306824})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.30170106887817383})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.26621922850608826})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2880478799343109})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.3312520980834961})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.28911441564559937})
store['active_learning_steps'][50]['training']['best_epoch']=11
store['active_learning_steps'][50]['evaluation_metrics']={'accuracy': 0.9718, 'crossentropy': 0.2553644775390625}
store['active_learning_steps'][50]['eval_training']={}
store['active_learning_steps'][50]['eval_training']['epochs']=[]
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.8307509422302246})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.41471153497695923})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.3453822433948517})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.30040329694747925})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.26583343744277954})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.25139471888542175})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.2243850827217102})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.24202972650527954})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.2382548749446869})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.9755859375, 'crossentropy': 0.2319013476371765})
store['active_learning_steps'][50]['eval_training']['best_epoch']=7
store['active_learning_steps'][50]['acquisition']={'indices': [10756, 19971, 6005, 4369, 50370, 10520, 48356, 52456, 26293, 4815], 'labels': [3, -1, -1, -1, 7, -1, 2, 2, 4, -1], 'scores': [0.6429557204246521, 0.3663281202316284, 0.33306705951690674, 0.5588086843490601, 0.3717012405395508, 0.6625455021858215, 0.28048717975616455, 0.6086221933364868, 0.5140617191791534, 0.35976099967956543]}
store['active_learning_steps'].append({})
store['active_learning_steps'][51]['training']={}
store['active_learning_steps'][51]['training']['epochs']=[]
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 1.1451469659805298})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.5947361588478088})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.43421459197998047})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.36931777000427246})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2999512851238251})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2991348206996918})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.28886353969573975})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2719441056251526})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3119066059589386})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.30620139837265015})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2820501923561096})
store['active_learning_steps'][51]['training']['best_epoch']=8
store['active_learning_steps'][51]['evaluation_metrics']={'accuracy': 0.9697, 'crossentropy': 0.270148046875}
store['active_learning_steps'][51]['eval_training']={}
store['active_learning_steps'][51]['eval_training']['epochs']=[]
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.8606369495391846})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.5350570678710938})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3526759743690491})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.30120599269866943})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.315523236989975})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.27797436714172363})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.27501824498176575})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.25526002049446106})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.974609375, 'crossentropy': 0.24426297843456268})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.23085293173789978})
store['active_learning_steps'][51]['eval_training']['best_epoch']=10
store['active_learning_steps'][51]['acquisition']={'indices': [38985, 10126, 57624, 25920, 58049, 37161, 18027, 23187, 52931, 22621], 'labels': [-1, -1, -1, -1, -1, 3, -1, -1, 3, -1], 'scores': [0.3713027238845825, 0.6171045303344727, 0.4883701205253601, 0.4101855754852295, 0.5148898959159851, 0.46755117177963257, 0.48377561569213867, 0.4951082468032837, 0.23560300469398499, 0.3885636329650879]}
store['active_learning_steps'].append({})
store['active_learning_steps'][52]['training']={}
store['active_learning_steps'][52]['training']['epochs']=[]
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 1.1124818325042725})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.5627708435058594})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.4097375273704529})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3583592176437378})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3370778560638428})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.3024081587791443})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.28852394223213196})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2883661389350891})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.28671130537986755})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.33453941345214844})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.28964123129844666})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3168366253376007})
store['active_learning_steps'][52]['training']['best_epoch']=9
store['active_learning_steps'][52]['evaluation_metrics']={'accuracy': 0.9693, 'crossentropy': 0.28287578125}
store['active_learning_steps'][52]['eval_training']={}
store['active_learning_steps'][52]['eval_training']['epochs']=[]
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.8401612639427185})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.47848132252693176})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.3662030100822449})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.31280267238616943})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.2676059603691101})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2645420730113983})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.23805144429206848})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2529536485671997})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.243318572640419})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.238765150308609})
store['active_learning_steps'][52]['eval_training']['best_epoch']=7
store['active_learning_steps'][52]['acquisition']={'indices': [22607, 42122, 55905, 22040, 42472, 12360, 14376, 47597, 12197, 37089], 'labels': [4, -1, -1, -1, 2, -1, 5, 8, -1, -1], 'scores': [0.6230620741844177, 0.4617488384246826, 0.43550097942352295, 0.46617746353149414, 0.4045397639274597, 0.44604289531707764, 0.5306707620620728, 0.566291093826294, 0.5881487131118774, 0.5793448090553284]}
store['active_learning_steps'].append({})
store['active_learning_steps'][53]['training']={}
store['active_learning_steps'][53]['training']['epochs']=[]
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 1.2401838302612305})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.6387523412704468})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3611050844192505})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3193231225013733})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.330988347530365})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.30273836851119995})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.30113208293914795})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.30589139461517334})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.28804200887680054})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.30019909143447876})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.32079848647117615})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2711748778820038})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.28546297550201416})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.3049877882003784})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.31459176540374756})
store['active_learning_steps'][53]['training']['best_epoch']=12
store['active_learning_steps'][53]['evaluation_metrics']={'accuracy': 0.9714, 'crossentropy': 0.2725156494140625}
store['active_learning_steps'][53]['eval_training']={}
store['active_learning_steps'][53]['eval_training']['epochs']=[]
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.8892843723297119})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.5204122066497803})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.329082190990448})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.28812259435653687})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.27251237630844116})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.2624681293964386})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.248382568359375})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.24149321019649506})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.23243404924869537})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.23959897458553314})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.9755859375, 'crossentropy': 0.22610515356063843})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.23106133937835693})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.21009714901447296})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.9755859375, 'crossentropy': 0.23028555512428284})
store['active_learning_steps'][53]['eval_training']['best_epoch']=13
store['active_learning_steps'][53]['acquisition']={'indices': [6005, 34800, 10486, 46760, 40016, 27999, 14342, 20177, 32776, 15523], 'labels': [-1, 5, -1, -1, -1, -1, -1, -1, 4, -1], 'scores': [0.6418038010597229, 0.42949551343917847, 0.39173424243927, 0.46182847023010254, 0.735626757144928, 0.42757439613342285, 0.6719214916229248, 0.4109032154083252, 0.6445044875144958, 0.6301305890083313]}
store['active_learning_steps'].append({})
store['active_learning_steps'][54]['training']={}
store['active_learning_steps'][54]['training']['epochs']=[]
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 1.051259994506836})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.4733528196811676})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.37805360555648804})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3114655613899231})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.26222914457321167})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2594292163848877})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.2426108419895172})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.263808012008667})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.9765625, 'crossentropy': 0.2431359440088272})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.23676344752311707})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.28843507170677185})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.27226361632347107})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.2568588852882385})
store['active_learning_steps'][54]['training']['best_epoch']=10
store['active_learning_steps'][54]['evaluation_metrics']={'accuracy': 0.9732, 'crossentropy': 0.25204677734375}
store['active_learning_steps'][54]['eval_training']={}
store['active_learning_steps'][54]['eval_training']['epochs']=[]
store['active_learning_steps'][54]['eval_training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.8461747169494629})
store['active_learning_steps'][54]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.45499730110168457})
store['active_learning_steps'][54]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.34915468096733093})
store['active_learning_steps'][54]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2709895074367523})
store['active_learning_steps'][54]['eval_training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.2686368227005005})
store['active_learning_steps'][54]['eval_training']['epochs'].append({'accuracy': 0.9755859375, 'crossentropy': 0.2574063539505005})
store['active_learning_steps'][54]['eval_training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.2368752658367157})
store['active_learning_steps'][54]['eval_training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.22283965349197388})
store['active_learning_steps'][54]['eval_training']['epochs'].append({'accuracy': 0.974609375, 'crossentropy': 0.2132246047258377})
store['active_learning_steps'][54]['eval_training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.22411412000656128})
store['active_learning_steps'][54]['eval_training']['epochs'].append({'accuracy': 0.9765625, 'crossentropy': 0.2009967714548111})
store['active_learning_steps'][54]['eval_training']['epochs'].append({'accuracy': 0.9765625, 'crossentropy': 0.22304043173789978})
store['active_learning_steps'][54]['eval_training']['best_epoch']=11
store['active_learning_steps'][54]['acquisition']={'indices': [33376, 26990, 14726, 24967, 24740, 49488, 17570, 53881, 22592, 5820], 'labels': [-1, 0, 9, 9, 8, 1, 9, -1, -1, -1], 'scores': [0.33357763290405273, 0.4321388304233551, 0.5416463017463684, 0.197398841381073, 0.6585054397583008, 0.4594791531562805, 0.45618346333503723, 0.26722168922424316, 0.31746184825897217, 0.20436733961105347]}
store['active_learning_steps'].append({})
store['active_learning_steps'][55]['training']={}
store['active_learning_steps'][55]['training']['epochs']=[]
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 1.2609847784042358})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5623524188995361})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.35625940561294556})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3289630711078644})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.27898889780044556})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.26193833351135254})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.27471300959587097})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.3012225031852722})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.27492639422416687})
store['active_learning_steps'][55]['training']['best_epoch']=6
store['active_learning_steps'][55]['evaluation_metrics']={'accuracy': 0.9677, 'crossentropy': 0.2767773681640625}
store['active_learning_steps'][55]['eval_training']={}
store['active_learning_steps'][55]['eval_training']['epochs']=[]
store['active_learning_steps'][55]['eval_training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 0.9963195323944092})
store['active_learning_steps'][55]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5068140029907227})
store['active_learning_steps'][55]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.41771429777145386})
store['active_learning_steps'][55]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3463197350502014})
store['active_learning_steps'][55]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.34872469305992126})
store['active_learning_steps'][55]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2815195322036743})
store['active_learning_steps'][55]['eval_training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.27440229058265686})
store['active_learning_steps'][55]['eval_training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2814710736274719})
store['active_learning_steps'][55]['eval_training']['best_epoch']=7
store['active_learning_steps'][55]['acquisition']={'indices': [18186, 24188, 45216, 43206, 38469, 59492, 22299, 48354, 1323, 55043], 'labels': [-1, -1, -1, 5, -1, -1, -1, 2, -1, -1], 'scores': [0.45547330379486084, 0.33179450035095215, 0.4402940273284912, 0.5036295056343079, 0.48087573051452637, 0.4518876075744629, 0.5273642539978027, 0.24533462524414062, 0.4157898426055908, 0.5697965621948242]}
store['active_learning_steps'].append({})
store['active_learning_steps'][56]['training']={}
store['active_learning_steps'][56]['training']['epochs']=[]
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.798828125, 'crossentropy': 1.2450635433197021})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.554695188999176})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.412712037563324})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.36993277072906494})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3669660687446594})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.30381396412849426})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.3056952655315399})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.9765625, 'crossentropy': 0.28317129611968994})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.3247225880622864})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.32957470417022705})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.3064560294151306})
store['active_learning_steps'][56]['training']['best_epoch']=8
store['active_learning_steps'][56]['evaluation_metrics']={'accuracy': 0.9691, 'crossentropy': 0.2772826416015625}
store['active_learning_steps'][56]['eval_training']={}
store['active_learning_steps'][56]['eval_training']['epochs']=[]
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.9645836353302002})
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.5168799161911011})
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.39096924662590027})
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3332843482494354})
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.28093522787094116})
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.29588210582733154})
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2623181939125061})
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.273017555475235})
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.2617555260658264})
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.24104516208171844})
store['active_learning_steps'][56]['eval_training']['best_epoch']=10
store['active_learning_steps'][56]['acquisition']={'indices': [46120, 22929, 20448, 3693, 53931, 43971, 47891, 53585, 34920, 27885], 'labels': [-1, -1, -1, -1, -1, -1, -1, 2, 9, -1], 'scores': [0.5352166891098022, 0.2915644645690918, 0.32297706604003906, 0.43200981616973877, 0.529674768447876, 0.41721415519714355, 0.4256688952445984, 0.6088946461677551, 0.5845946073532104, 0.552934467792511]}
store['active_learning_steps'].append({})
store['active_learning_steps'][57]['training']={}
store['active_learning_steps'][57]['training']['epochs']=[]
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 1.3617686033248901})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.5990559458732605})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.427276611328125})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.35921338200569153})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.30901122093200684})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.28897809982299805})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.31061792373657227})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.3202407956123352})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.278577983379364})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.3030030131340027})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.2788233160972595})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2688242793083191})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2773513197898865})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.3151962161064148})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3152730464935303})
store['active_learning_steps'][57]['training']['best_epoch']=12
store['active_learning_steps'][57]['evaluation_metrics']={'accuracy': 0.9702, 'crossentropy': 0.264436376953125}
store['active_learning_steps'][57]['eval_training']={}
store['active_learning_steps'][57]['eval_training']['epochs']=[]
store['active_learning_steps'][57]['eval_training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.9435117840766907})
store['active_learning_steps'][57]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.5041621923446655})
store['active_learning_steps'][57]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.34136348962783813})
store['active_learning_steps'][57]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.32305359840393066})
store['active_learning_steps'][57]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2822982668876648})
store['active_learning_steps'][57]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2660624384880066})
store['active_learning_steps'][57]['eval_training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.2484608292579651})
store['active_learning_steps'][57]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.25296682119369507})
store['active_learning_steps'][57]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2204054892063141})
store['active_learning_steps'][57]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2418563961982727})
store['active_learning_steps'][57]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.22382941842079163})
store['active_learning_steps'][57]['eval_training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.20520548522472382})
store['active_learning_steps'][57]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.22815760970115662})
store['active_learning_steps'][57]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2229595184326172})
store['active_learning_steps'][57]['eval_training']['best_epoch']=12
store['active_learning_steps'][57]['acquisition']={'indices': [53603, 47034, 27203, 32999, 3316, 56566, 49899, 6968, 323, 491], 'labels': [-1, -1, -1, -1, -1, 5, -1, -1, -1, -1], 'scores': [0.5395439863204956, 0.7237377166748047, 0.5631632804870605, 0.5498169660568237, 0.39926648139953613, 0.6785642504692078, 0.5744174718856812, 0.4065643548965454, 0.5691980123519897, 0.5209559202194214]}
store['active_learning_steps'].append({})
store['active_learning_steps'][58]['training']={}
store['active_learning_steps'][58]['training']['epochs']=[]
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.9835449457168579})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.4837666451931})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3801409602165222})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.31632736325263977})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.29700911045074463})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.26835304498672485})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2679552733898163})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2891523241996765})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2988699674606323})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.9765625, 'crossentropy': 0.2335071861743927})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2869621217250824})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3133908808231354})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2518761157989502})
store['active_learning_steps'][58]['training']['best_epoch']=10
store['active_learning_steps'][58]['evaluation_metrics']={'accuracy': 0.972, 'crossentropy': 0.2486039306640625}
store['active_learning_steps'][58]['eval_training']={}
store['active_learning_steps'][58]['eval_training']['epochs']=[]
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.911067008972168})
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.5116696357727051})
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3436143696308136})
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.28519442677497864})
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.28162604570388794})
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.2318633496761322})
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.24929773807525635})
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.24369966983795166})
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.2216985523700714})
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.22284993529319763})
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.22218874096870422})
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.21703007817268372})
store['active_learning_steps'][58]['eval_training']['best_epoch']=12
store['active_learning_steps'][58]['acquisition']={'indices': [40566, 16739, 15933, 22315, 21190, 25184, 4055, 18044, 58001, 36704], 'labels': [2, -1, -1, -1, -1, -1, -1, -1, -1, 2], 'scores': [0.3507845401763916, 0.4316064119338989, 0.4936039447784424, 0.5816963911056519, 0.5520321130752563, 0.4590972661972046, 0.5720740556716919, 0.4605097770690918, 0.48232197761535645, 0.5505619645118713]}
store['active_learning_steps'].append({})
store['active_learning_steps'][59]['training']={}
store['active_learning_steps'][59]['training']['epochs']=[]
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 1.1213735342025757})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.5956604480743408})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.38964375853538513})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.31755661964416504})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.28845107555389404})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2735525369644165})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3316752314567566})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.3549227714538574})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.30428367853164673})
store['active_learning_steps'][59]['training']['best_epoch']=6
store['active_learning_steps'][59]['evaluation_metrics']={'accuracy': 0.9635, 'crossentropy': 0.2871446044921875}
store['active_learning_steps'][59]['eval_training']={}
store['active_learning_steps'][59]['eval_training']['epochs']=[]
store['active_learning_steps'][59]['eval_training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 0.9419905543327332})
store['active_learning_steps'][59]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5180447101593018})
store['active_learning_steps'][59]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.38065946102142334})
store['active_learning_steps'][59]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3313584327697754})
store['active_learning_steps'][59]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.346302330493927})
store['active_learning_steps'][59]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.31251755356788635})
store['active_learning_steps'][59]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2987034320831299})
store['active_learning_steps'][59]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.29579710960388184})
store['active_learning_steps'][59]['eval_training']['best_epoch']=8
store['active_learning_steps'][59]['acquisition']={'indices': [11195, 17039, 33086, 8505, 1075, 10283, 30053, 3676, 40539, 21185], 'labels': [-1, -1, -1, -1, 7, 0, -1, 2, -1, -1], 'scores': [0.4449501037597656, 0.5389903783798218, 0.5252977609634399, 0.42413604259490967, 0.5721802711486816, 0.32559406757354736, 0.3620760440826416, 0.500076413154602, 0.31915104389190674, 0.3965088129043579]}
store['active_learning_steps'].append({})
store['active_learning_steps'][60]['training']={}
store['active_learning_steps'][60]['training']['epochs']=[]
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 1.0190311670303345})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.5695492029190063})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.39915919303894043})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.28231698274612427})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.3120768666267395})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2896888852119446})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2844705879688263})
store['active_learning_steps'][60]['training']['best_epoch']=4
store['active_learning_steps'][60]['evaluation_metrics']={'accuracy': 0.9654, 'crossentropy': 0.2970414794921875}
store['active_learning_steps'][60]['eval_training']={}
store['active_learning_steps'][60]['eval_training']['epochs']=[]
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.8097919821739197})
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.5219963788986206})
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3855893015861511})
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.377094566822052})
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3603411316871643})
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.301655113697052})
store['active_learning_steps'][60]['eval_training']['best_epoch']=6
store['active_learning_steps'][60]['acquisition']={'indices': [57972, 37898, 24488, 25873, 52169, 40208, 53919, 12840, 50909, 16787], 'labels': [4, -1, -1, 8, 2, 0, -1, 9, -1, -1], 'scores': [0.5206032991409302, 0.2336103916168213, 0.2777111530303955, 0.422680139541626, 0.5087774991989136, 0.3653038740158081, 0.39669764041900635, 0.5505976676940918, 0.24821698665618896, 0.19721925258636475]}
store['active_learning_steps'].append({})
store['active_learning_steps'][61]['training']={}
store['active_learning_steps'][61]['training']['epochs']=[]
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 1.096096158027649})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.4810895621776581})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.36956003308296204})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3015252649784088})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2993210554122925})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.28607913851737976})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2763254642486572})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.27277442812919617})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2885274291038513})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2744850814342499})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.28334739804267883})
store['active_learning_steps'][61]['training']['best_epoch']=8
store['active_learning_steps'][61]['evaluation_metrics']={'accuracy': 0.9637, 'crossentropy': 0.288533251953125}
store['active_learning_steps'][61]['eval_training']={}
store['active_learning_steps'][61]['eval_training']['epochs']=[]
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 0.9723502993583679})
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5484857559204102})
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3757804036140442})
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3573618531227112})
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.32644104957580566})
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2709413170814514})
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.27924782037734985})
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2523886263370514})
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.24831900000572205})
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.26086366176605225})
store['active_learning_steps'][61]['eval_training']['best_epoch']=9
store['active_learning_steps'][61]['acquisition']={'indices': [59308, 10822, 24736, 11366, 49500, 26926, 8395, 3185, 56072, 41868], 'labels': [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1], 'scores': [0.4481927156448364, 0.3598625659942627, 0.3002411127090454, 0.346574068069458, 0.33363962173461914, 0.3630187511444092, 0.37335407733917236, 0.35515785217285156, 0.357663094997406, 0.38092637062072754]}
store['active_learning_steps'].append({})
store['active_learning_steps'][62]['training']={}
store['active_learning_steps'][62]['training']['epochs']=[]
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 1.1308200359344482})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.5588375329971313})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3521580696105957})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.28927671909332275})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2801586389541626})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.974609375, 'crossentropy': 0.252208411693573})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2760269045829773})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2638646364212036})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.25664451718330383})
store['active_learning_steps'][62]['training']['best_epoch']=6
store['active_learning_steps'][62]['evaluation_metrics']={'accuracy': 0.9711, 'crossentropy': 0.2475951904296875}
store['active_learning_steps'][62]['eval_training']={}
store['active_learning_steps'][62]['eval_training']['epochs']=[]
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 1.027659296989441})
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.5098975300788879})
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.41720935702323914})
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.3392100930213928})
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.3279837369918823})
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.33007922768592834})
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.276769757270813})
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2695810794830322})
store['active_learning_steps'][62]['eval_training']['best_epoch']=8
store['active_learning_steps'][62]['acquisition']={'indices': [21910, 29839, 23351, 47430, 54042, 22614, 7833, 46936, 15405, 12692], 'labels': [-1, -1, -1, -1, -1, -1, 5, -1, -1, 5], 'scores': [0.607039213180542, 0.3687632083892822, 0.4054715633392334, 0.37461209297180176, 0.2522517442703247, 0.47234201431274414, 0.5257418751716614, 0.4217519760131836, 0.21064722537994385, 0.34283506870269775]}
store['active_learning_steps'].append({})
store['active_learning_steps'][63]['training']={}
store['active_learning_steps'][63]['training']['epochs']=[]
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 1.1001574993133545})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5162290334701538})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3871474862098694})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.27070188522338867})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.27271556854248047})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.27798229455947876})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2724875807762146})
store['active_learning_steps'][63]['training']['best_epoch']=4
store['active_learning_steps'][63]['evaluation_metrics']={'accuracy': 0.9674, 'crossentropy': 0.282741748046875}
store['active_learning_steps'][63]['eval_training']={}
store['active_learning_steps'][63]['eval_training']['epochs']=[]
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.8865127563476562})
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.49660080671310425})
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.4366059899330139})
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3465864062309265})
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.35554027557373047})
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3703746497631073})
store['active_learning_steps'][63]['eval_training']['best_epoch']=4
store['active_learning_steps'][63]['acquisition']={'indices': [21102, 19942, 24004, 57169, 6254, 14690, 43060, 28194, 3106, 393], 'labels': [3, 5, 5, -1, 1, 8, -1, -1, 0, -1], 'scores': [0.355460524559021, 0.5049353241920471, 0.2976931929588318, 0.3134843111038208, 0.26553767919540405, 0.3706203103065491, 0.2501870393753052, 0.28794169425964355, 0.33756041526794434, 0.34217405319213867]}
store['active_learning_steps'].append({})
store['active_learning_steps'][64]['training']={}
store['active_learning_steps'][64]['training']['epochs']=[]
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 1.058659553527832})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5206741094589233})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3457449674606323})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.31211310625076294})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.2986658811569214})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.28366321325302124})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2619495391845703})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.26237067580223083})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.28624075651168823})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2846919298171997})
store['active_learning_steps'][64]['training']['best_epoch']=7
store['active_learning_steps'][64]['evaluation_metrics']={'accuracy': 0.9676, 'crossentropy': 0.265001025390625}
store['active_learning_steps'][64]['eval_training']={}
store['active_learning_steps'][64]['eval_training']['epochs']=[]
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.9046393036842346})
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.4882315397262573})
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.36380910873413086})
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.3570343255996704})
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.3098093271255493})
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.280668169260025})
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.25031548738479614})
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.23366817831993103})
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.25088798999786377})
store['active_learning_steps'][64]['eval_training']['best_epoch']=8
store['active_learning_steps'][64]['acquisition']={'indices': [25564, 3061, 33892, 52738, 53386, 21264, 57470, 17509, 42428, 19665], 'labels': [-1, -1, -1, -1, -1, -1, -1, -1, 5, -1], 'scores': [0.3826037645339966, 0.3060039281845093, 0.5014019012451172, 0.515929102897644, 0.3776487112045288, 0.4749845266342163, 0.31326282024383545, 0.5616832971572876, 0.6272181868553162, 0.4004477262496948]}
store['active_learning_steps'].append({})
store['active_learning_steps'][65]['training']={}
store['active_learning_steps'][65]['training']['epochs']=[]
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 1.1708974838256836})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.601932168006897})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.36303621530532837})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.30455270409584045})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3315064311027527})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3171985149383545})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.2779111862182617})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2920815348625183})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3068045377731323})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3124677538871765})
store['active_learning_steps'][65]['training']['best_epoch']=7
store['active_learning_steps'][65]['evaluation_metrics']={'accuracy': 0.9681, 'crossentropy': 0.27887744140625}
store['active_learning_steps'][65]['eval_training']={}
store['active_learning_steps'][65]['eval_training']['epochs']=[]
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.9681175947189331})
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.5183643102645874})
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.4042302966117859})
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.34144121408462524})
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.30055397748947144})
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.29667049646377563})
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2886847257614136})
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2902032732963562})
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2772502303123474})
store['active_learning_steps'][65]['eval_training']['best_epoch']=9
store['active_learning_steps'][65]['acquisition']={'indices': [11605, 26475, 44267, 37583, 20612, 59726, 29467, 6249, 30374, 32429], 'labels': [-1, -1, -1, -1, -1, 5, -1, -1, 8, -1], 'scores': [0.49362289905548096, 0.4417020082473755, 0.4506744146347046, 0.5662075281143188, 0.4722224473953247, 0.6628241539001465, 0.5408614873886108, 0.4253981113433838, 0.36498016119003296, 0.4184134006500244]}
store['active_learning_steps'].append({})
store['active_learning_steps'][66]['training']={}
store['active_learning_steps'][66]['training']['epochs']=[]
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 1.0608220100402832})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.6013299226760864})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.36055222153663635})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.33282530307769775})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.28197866678237915})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2720367908477783})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.29115286469459534})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3141571283340454})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.30964356660842896})
store['active_learning_steps'][66]['training']['best_epoch']=6
store['active_learning_steps'][66]['evaluation_metrics']={'accuracy': 0.9668, 'crossentropy': 0.2840054443359375}
store['active_learning_steps'][66]['eval_training']={}
store['active_learning_steps'][66]['eval_training']['epochs']=[]
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.8680890798568726})
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.4750552773475647})
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.394733190536499})
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3509024679660797})
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2829345464706421})
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.28826653957366943})
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2913759648799896})
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.29682695865631104})
store['active_learning_steps'][66]['eval_training']['best_epoch']=5
store['active_learning_steps'][66]['acquisition']={'indices': [26153, 55814, 22633, 40512, 6291, 43107, 47870, 14588, 6428, 160], 'labels': [-1, -1, 6, 7, 3, -1, 9, 3, -1, 8], 'scores': [0.3367053270339966, 0.3667696714401245, 0.40550100803375244, 0.41960805654525757, 0.4385210871696472, 0.173240065574646, 0.31414687633514404, 0.4508473873138428, 0.4121204614639282, 0.3316328525543213]}
store['active_learning_steps'].append({})
store['active_learning_steps'][67]['training']={}
store['active_learning_steps'][67]['training']['epochs']=[]
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 1.2743489742279053})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.5614678859710693})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.4198007583618164})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3444087505340576})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3285333812236786})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2758331298828125})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2885786294937134})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2894855737686157})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2881987690925598})
store['active_learning_steps'][67]['training']['best_epoch']=6
store['active_learning_steps'][67]['evaluation_metrics']={'accuracy': 0.9679, 'crossentropy': 0.2653887939453125}
store['active_learning_steps'][67]['eval_training']={}
store['active_learning_steps'][67]['eval_training']['epochs']=[]
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.8654110431671143})
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5510938167572021})
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.385093629360199})
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.35857000946998596})
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.32386720180511475})
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.31532514095306396})
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3015420734882355})
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.32604703307151794})
store['active_learning_steps'][67]['eval_training']['best_epoch']=7
store['active_learning_steps'][67]['acquisition']={'indices': [26515, 5938, 8111, 47101, 13581, 50149, 34771, 28454, 50556, 35627], 'labels': [-1, -1, -1, -1, -1, 4, 0, -1, 6, -1], 'scores': [0.37718749046325684, 0.5283045768737793, 0.4868201017379761, 0.5025852918624878, 0.3262934684753418, 0.5015157461166382, 0.4115891456604004, 0.3924596309661865, 0.3809950053691864, 0.46344107389450073]}
store['active_learning_steps'].append({})
store['active_learning_steps'][68]['training']={}
store['active_learning_steps'][68]['training']['epochs']=[]
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 1.2099535465240479})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.5283678770065308})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.41351088881492615})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.31341859698295593})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3253380060195923})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2882080674171448})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3162095844745636})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.28501367568969727})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.27814769744873047})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.26655423641204834})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.974609375, 'crossentropy': 0.2730078101158142})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.27079951763153076})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.3057076036930084})
store['active_learning_steps'][68]['training']['best_epoch']=10
store['active_learning_steps'][68]['evaluation_metrics']={'accuracy': 0.9663, 'crossentropy': 0.2839373779296875}
store['active_learning_steps'][68]['eval_training']={}
store['active_learning_steps'][68]['eval_training']['epochs']=[]
store['active_learning_steps'][68]['eval_training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.8157370686531067})
store['active_learning_steps'][68]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.47409364581108093})
store['active_learning_steps'][68]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3829135596752167})
store['active_learning_steps'][68]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3026394844055176})
store['active_learning_steps'][68]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.31519800424575806})
store['active_learning_steps'][68]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.26846975088119507})
store['active_learning_steps'][68]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2312314510345459})
store['active_learning_steps'][68]['eval_training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.24034351110458374})
store['active_learning_steps'][68]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.24048686027526855})
store['active_learning_steps'][68]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.25946587324142456})
store['active_learning_steps'][68]['eval_training']['best_epoch']=7
store['active_learning_steps'][68]['acquisition']={'indices': [28762, 42041, 59015, 56588, 40654, 6680, 22098, 41196, 2432, 52358], 'labels': [5, -1, -1, 7, -1, -1, -1, 9, -1, 2], 'scores': [0.5218042433261871, 0.45457231998443604, 0.3977161645889282, 0.4503327012062073, 0.4269164800643921, 0.427260160446167, 0.6234744191169739, 0.6289329528808594, 0.2439253330230713, 0.6803672313690186]}
store['active_learning_steps'].append({})
store['active_learning_steps'][69]['training']={}
store['active_learning_steps'][69]['training']['epochs']=[]
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.9690314531326294})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.49648892879486084})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3394659161567688})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.30868667364120483})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.29188215732574463})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2929058074951172})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2736953794956207})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2822756767272949})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.25856733322143555})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9775390625, 'crossentropy': 0.2524435818195343})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.26514628529548645})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.26031994819641113})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2902776300907135})
store['active_learning_steps'][69]['training']['best_epoch']=10
store['active_learning_steps'][69]['evaluation_metrics']={'accuracy': 0.9702, 'crossentropy': 0.244927294921875}
store['active_learning_steps'][69]['eval_training']={}
store['active_learning_steps'][69]['eval_training']['epochs']=[]
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.8371356725692749})
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.48000937700271606})
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3791571259498596})
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.28958433866500854})
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.25659191608428955})
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.9755859375, 'crossentropy': 0.2897859215736389})
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.24062886834144592})
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.9755859375, 'crossentropy': 0.20484361052513123})
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.2543696463108063})
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.20854127407073975})
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.974609375, 'crossentropy': 0.22604861855506897})
store['active_learning_steps'][69]['eval_training']['best_epoch']=8
store['active_learning_steps'][69]['acquisition']={'indices': [36984, 19896, 19328, 18487, 7484, 10957, 38926, 39114, 23927, 15424], 'labels': [-1, 6, 5, 4, -1, -1, -1, -1, 5, -1], 'scores': [0.30051127076148987, 0.36877185106277466, 0.6396678686141968, 0.5043699145317078, 0.3051055669784546, 0.39162564277648926, 0.30913305282592773, 0.3957712650299072, 0.46743500232696533, 0.3446403741836548]}
store['active_learning_steps'].append({})
store['active_learning_steps'][70]['training']={}
store['active_learning_steps'][70]['training']['epochs']=[]
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 1.1611747741699219})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.5542968511581421})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.36488574743270874})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.28476232290267944})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.974609375, 'crossentropy': 0.27529817819595337})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2430260181427002})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.25860774517059326})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.974609375, 'crossentropy': 0.2629395127296448})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.9775390625, 'crossentropy': 0.22573217749595642})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.9775390625, 'crossentropy': 0.22758358716964722})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.24848194420337677})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.9765625, 'crossentropy': 0.23209911584854126})
store['active_learning_steps'][70]['training']['best_epoch']=9
store['active_learning_steps'][70]['evaluation_metrics']={'accuracy': 0.9726, 'crossentropy': 0.2438835693359375}
store['active_learning_steps'][70]['eval_training']={}
store['active_learning_steps'][70]['eval_training']['epochs']=[]
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.9147520065307617})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.486183762550354})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.302634060382843})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.28449252247810364})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.26975393295288086})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2407388687133789})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2332681119441986})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.2424495816230774})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.237038254737854})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.20877042412757874})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.230876624584198})
store['active_learning_steps'][70]['eval_training']['best_epoch']=10
store['active_learning_steps'][70]['acquisition']={'indices': [1916, 49822, 17971, 47486, 26380, 37372, 7296, 24970, 36127, 14341], 'labels': [0, -1, -1, -1, -1, -1, -1, -1, -1, -1], 'scores': [0.18354597687721252, 0.41440892219543457, 0.4800419807434082, 0.29524219036102295, 0.5198748111724854, 0.42946839332580566, 0.44598257541656494, 0.45261430740356445, 0.3734828233718872, 0.4172629117965698]}
store['active_learning_steps'].append({})
store['active_learning_steps'][71]['training']={}
store['active_learning_steps'][71]['training']['epochs']=[]
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.791015625, 'crossentropy': 1.231900691986084})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.6775354146957397})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.4163138270378113})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3088292181491852})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2764679193496704})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.26308712363243103})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.27173423767089844})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.974609375, 'crossentropy': 0.26438409090042114})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.27506253123283386})
store['active_learning_steps'][71]['training']['best_epoch']=6
store['active_learning_steps'][71]['evaluation_metrics']={'accuracy': 0.9683, 'crossentropy': 0.25921376953125}
store['active_learning_steps'][71]['eval_training']={}
store['active_learning_steps'][71]['eval_training']['epochs']=[]
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.826291561126709})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.42670097947120667})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.38069015741348267})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.32336458563804626})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.29720550775527954})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.314147412776947})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.27919596433639526})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2833302915096283})
store['active_learning_steps'][71]['eval_training']['best_epoch']=7
store['active_learning_steps'][71]['acquisition']={'indices': [33669, 37122, 38990, 12748, 24800, 21436, 31383, 49768, 57054, 44123], 'labels': [-1, -1, 3, -1, -1, 2, -1, -1, -1, 8], 'scores': [0.5339702367782593, 0.49412405490875244, 0.3348384499549866, 0.39172887802124023, 0.4048278331756592, 0.5433279275894165, 0.3700171113014221, 0.3764522075653076, 0.39210784435272217, 0.5947357416152954]}
store['active_learning_steps'].append({})
store['active_learning_steps'][72]['training']={}
store['active_learning_steps'][72]['training']['epochs']=[]
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 1.0676748752593994})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.48752743005752563})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3494281768798828})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.32471466064453125})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2568969428539276})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2712796628475189})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2607871890068054})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.2293526530265808})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.2639580965042114})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2640882432460785})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9765625, 'crossentropy': 0.22690685093402863})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.2768637537956238})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2599904239177704})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.25945067405700684})
store['active_learning_steps'][72]['training']['best_epoch']=11
store['active_learning_steps'][72]['evaluation_metrics']={'accuracy': 0.974, 'crossentropy': 0.237210986328125}
store['active_learning_steps'][72]['eval_training']={}
store['active_learning_steps'][72]['eval_training']['epochs']=[]
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 1.0341906547546387})
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.4968011975288391})
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3591674566268921})
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3380763530731201})
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.28162041306495667})
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.25825372338294983})
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.25015518069267273})
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.23927056789398193})
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2118016928434372})
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.9755859375, 'crossentropy': 0.22608041763305664})
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.23228417336940765})
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.23514053225517273})
store['active_learning_steps'][72]['eval_training']['best_epoch']=9
store['active_learning_steps'][72]['acquisition']={'indices': [42991, 30632, 49981, 16556, 51988, 49231, 30587, 56235, 41149, 39032], 'labels': [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1], 'scores': [0.46302127838134766, 0.5501008033752441, 0.36591076850891113, 0.5746138095855713, 0.48195308446884155, 0.5142632722854614, 0.45555734634399414, 0.59269779920578, 0.43098020553588867, 0.503281831741333]}
store['active_learning_steps'].append({})
store['active_learning_steps'][73]['training']={}
store['active_learning_steps'][73]['training']['epochs']=[]
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 1.2803966999053955})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5968758463859558})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.38469791412353516})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.37244921922683716})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.32035309076309204})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2956511974334717})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2915900945663452})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.27786189317703247})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2662569284439087})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.29691413044929504})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.28058743476867676})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.32077354192733765})
store['active_learning_steps'][73]['training']['best_epoch']=9
store['active_learning_steps'][73]['evaluation_metrics']={'accuracy': 0.9706, 'crossentropy': 0.2532163818359375}
store['active_learning_steps'][73]['eval_training']={}
store['active_learning_steps'][73]['eval_training']['epochs']=[]
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 1.0590646266937256})
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.5287523865699768})
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3884371817111969})
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.31619465351104736})
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2926174998283386})
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2638551592826843})
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2741287648677826})
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.26342764496803284})
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.24107208847999573})
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.25214526057243347})
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.24904824793338776})
store['active_learning_steps'][73]['eval_training']['best_epoch']=9
store['active_learning_steps'][73]['acquisition']={'indices': [15286, 36196, 34488, 42124, 43068, 31714, 53587, 59747, 18729, 12760], 'labels': [8, -1, -1, -1, -1, -1, -1, 5, -1, -1], 'scores': [0.31555771827697754, 0.4383796453475952, 0.4044332504272461, 0.4997875690460205, 0.3908576965332031, 0.36760592460632324, 0.43370723724365234, 0.38629937171936035, 0.4382706880569458, 0.4108010530471802]}
store['active_learning_steps'].append({})
store['active_learning_steps'][74]['training']={}
store['active_learning_steps'][74]['training']['epochs']=[]
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.7880859375, 'crossentropy': 1.2917497158050537})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.5337020754814148})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.4231996536254883})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.31938743591308594})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.32426172494888306})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2644346058368683})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2632412612438202})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.28688448667526245})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.289335161447525})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3007951080799103})
store['active_learning_steps'][74]['training']['best_epoch']=7
store['active_learning_steps'][74]['evaluation_metrics']={'accuracy': 0.9682, 'crossentropy': 0.25996904296875}
store['active_learning_steps'][74]['eval_training']={}
store['active_learning_steps'][74]['eval_training']['epochs']=[]
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 1.005805253982544})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.5650993585586548})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.46692705154418945})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.35584622621536255})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.322018027305603})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3416571617126465})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.28342336416244507})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2810625731945038})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.29404929280281067})
store['active_learning_steps'][74]['eval_training']['best_epoch']=8
store['active_learning_steps'][74]['acquisition']={'indices': [51805, 21512, 24738, 59139, 18093, 40850, 43745, 38165, 43864, 58392], 'labels': [-1, -1, 1, -1, -1, -1, 8, 5, -1, -1], 'scores': [0.5099869966506958, 0.45277857780456543, 0.3883941173553467, 0.5167088508605957, 0.3964744806289673, 0.407412588596344, 0.5303139686584473, 0.36095112562179565, 0.42960965633392334, 0.5200375318527222]}
store['active_learning_steps'].append({})
store['active_learning_steps'][75]['training']={}
store['active_learning_steps'][75]['training']['epochs']=[]
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.787109375, 'crossentropy': 1.3077634572982788})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.6599489450454712})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.42503467202186584})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.334621399641037})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.28812867403030396})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.27583739161491394})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.273924320936203})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2718328535556793})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.29838594794273376})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2751425504684448})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.27902916073799133})
store['active_learning_steps'][75]['training']['best_epoch']=8
store['active_learning_steps'][75]['evaluation_metrics']={'accuracy': 0.9695, 'crossentropy': 0.271299609375}
store['active_learning_steps'][75]['eval_training']={}
store['active_learning_steps'][75]['eval_training']['epochs']=[]
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 1.138991355895996})
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6028883457183838})
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.45253926515579224})
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.33268672227859497})
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.26833051443099976})
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.3029208183288574})
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2894338369369507})
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2720072567462921})
store['active_learning_steps'][75]['eval_training']['best_epoch']=5
store['active_learning_steps'][75]['acquisition']={'indices': [19873, 28150, 7281, 19356, 4039, 46133, 28895, 47387, 53537, 14072], 'labels': [-1, 6, -1, 6, 6, -1, -1, 8, -1, 6], 'scores': [0.3343013525009155, 0.41131436824798584, 0.4171870946884155, 0.5624316930770874, 0.6106123328208923, 0.3638263940811157, 0.37941139936447144, 0.43967336416244507, 0.34435510635375977, 0.5591089725494385]}
store['active_learning_steps'].append({})
store['active_learning_steps'][76]['training']={}
store['active_learning_steps'][76]['training']['epochs']=[]
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.76171875, 'crossentropy': 1.3207101821899414})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.6188517808914185})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.4368370771408081})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.33929941058158875})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.2783014178276062})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2809068560600281})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.27095460891723633})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.271921843290329})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.28111031651496887})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.28640395402908325})
store['active_learning_steps'][76]['training']['best_epoch']=7
store['active_learning_steps'][76]['evaluation_metrics']={'accuracy': 0.9692, 'crossentropy': 0.2491045654296875}
store['active_learning_steps'][76]['eval_training']={}
store['active_learning_steps'][76]['eval_training']['epochs']=[]
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.8978333473205566})
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.4724627435207367})
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.35862380266189575})
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3496973514556885})
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2872110605239868})
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2992476522922516})
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.28225231170654297})
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.27364683151245117})
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2634158730506897})
store['active_learning_steps'][76]['eval_training']['best_epoch']=9
store['active_learning_steps'][76]['acquisition']={'indices': [3411, 10123, 58316, 17736, 16984, 33198, 20720, 31658, 2030, 5112], 'labels': [-1, -1, 0, -1, -1, 8, 7, -1, -1, -1], 'scores': [0.32579708099365234, 0.39286506175994873, 0.5406390428543091, 0.354386568069458, 0.29523932933807373, 0.3190416693687439, 0.450886070728302, 0.3406715393066406, 0.4543195962905884, 0.4436125159263611]}
store['active_learning_steps'].append({})
store['active_learning_steps'][77]['training']={}
store['active_learning_steps'][77]['training']['epochs']=[]
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 1.1501412391662598})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5157087445259094})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.36057209968566895})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.327309787273407})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.30415111780166626})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.2931237816810608})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.26985496282577515})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.25893211364746094})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2620229721069336})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.25474053621292114})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2679809331893921})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.25474271178245544})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.26239264011383057})
store['active_learning_steps'][77]['training']['best_epoch']=10
store['active_learning_steps'][77]['evaluation_metrics']={'accuracy': 0.97, 'crossentropy': 0.2605218505859375}
store['active_learning_steps'][77]['eval_training']={}
store['active_learning_steps'][77]['eval_training']['epochs']=[]
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.9292514324188232})
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.5186139345169067})
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3366478979587555})
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.31804943084716797})
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3089415431022644})
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.26989084482192993})
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2569119334220886})
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.22258205711841583})
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.23727163672447205})
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.9765625, 'crossentropy': 0.23504288494586945})
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.25155162811279297})
store['active_learning_steps'][77]['eval_training']['best_epoch']=8
store['active_learning_steps'][77]['acquisition']={'indices': [12302, 26133, 33685, 58111, 2371, 40770, 9384, 51595, 51674, 7195], 'labels': [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1], 'scores': [0.5138521194458008, 0.3724769353866577, 0.681893527507782, 0.3849189281463623, 0.43351197242736816, 0.4484298825263977, 0.4755142331123352, 0.36624693870544434, 0.5673494338989258, 0.4408760666847229]}
store['active_learning_steps'].append({})
store['active_learning_steps'][78]['training']={}
store['active_learning_steps'][78]['training']['epochs']=[]
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 1.2014813423156738})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.5848463177680969})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.4284777045249939})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3401442766189575})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.303433895111084})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3142317235469818})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2603774666786194})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2585148811340332})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.28661391139030457})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.9794921875, 'crossentropy': 0.23478826880455017})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.26951032876968384})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.974609375, 'crossentropy': 0.255296528339386})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.9775390625, 'crossentropy': 0.23669461905956268})
store['active_learning_steps'][78]['training']['best_epoch']=10
store['active_learning_steps'][78]['evaluation_metrics']={'accuracy': 0.9727, 'crossentropy': 0.244592138671875}
store['active_learning_steps'][78]['eval_training']={}
store['active_learning_steps'][78]['eval_training']['epochs']=[]
store['active_learning_steps'][78]['eval_training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 1.0308189392089844})
store['active_learning_steps'][78]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.5048336982727051})
store['active_learning_steps'][78]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3486546277999878})
store['active_learning_steps'][78]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.29083025455474854})
store['active_learning_steps'][78]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.260001540184021})
store['active_learning_steps'][78]['eval_training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.23289139568805695})
store['active_learning_steps'][78]['eval_training']['epochs'].append({'accuracy': 0.974609375, 'crossentropy': 0.2552492618560791})
store['active_learning_steps'][78]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2483161985874176})
store['active_learning_steps'][78]['eval_training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.2170943170785904})
store['active_learning_steps'][78]['eval_training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.21380744874477386})
store['active_learning_steps'][78]['eval_training']['epochs'].append({'accuracy': 0.9775390625, 'crossentropy': 0.21246832609176636})
store['active_learning_steps'][78]['eval_training']['epochs'].append({'accuracy': 0.9765625, 'crossentropy': 0.2097880244255066})
store['active_learning_steps'][78]['eval_training']['best_epoch']=12
store['active_learning_steps'][78]['acquisition']={'indices': [42337, 29320, 26882, 54240, 9138, 37449, 5062, 30480, 19507, 22824], 'labels': [5, 1, -1, 2, -1, -1, 9, -1, 1, 9], 'scores': [0.5689830183982849, 0.5634854435920715, 0.44179344177246094, 0.4675883948802948, 0.3791462182998657, 0.3639901280403137, 0.431893527507782, 0.3631173372268677, 0.5572460293769836, 0.49755024909973145]}
store['active_learning_steps'].append({})
store['active_learning_steps'][79]['training']={}
store['active_learning_steps'][79]['training']['epochs']=[]
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 1.1434625387191772})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5748008489608765})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3733331561088562})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.27417850494384766})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.28273266553878784})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.28790920972824097})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.24942395091056824})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.26527705788612366})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2552722990512848})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2673532962799072})
store['active_learning_steps'][79]['training']['best_epoch']=7
store['active_learning_steps'][79]['evaluation_metrics']={'accuracy': 0.9738, 'crossentropy': 0.2378213623046875}
store['active_learning_steps'][79]['eval_training']={}
store['active_learning_steps'][79]['eval_training']['epochs']=[]
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.8805524110794067})
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.4611414074897766})
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.37122589349746704})
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.32093724608421326})
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.28384384512901306})
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.28738129138946533})
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2550179362297058})
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.24778597056865692})
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.28054454922676086})
store['active_learning_steps'][79]['eval_training']['best_epoch']=8
store['active_learning_steps'][79]['acquisition']={'indices': [33966, 29002, 51693, 33882, 17865, 3486, 31250, 47195, 56171, 91], 'labels': [-1, 7, -1, -1, -1, -1, -1, -1, -1, -1], 'scores': [0.5281295776367188, 0.35000503063201904, 0.35228729248046875, 0.45061129331588745, 0.49457037448883057, 0.45089036226272583, 0.26371121406555176, 0.457542359828949, 0.2672315835952759, 0.26576805114746094]}
store['active_learning_steps'].append({})
store['active_learning_steps'][80]['training']={}
store['active_learning_steps'][80]['training']['epochs']=[]
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 1.1997361183166504})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5706042647361755})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.4088231921195984})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3811521530151367})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3516808748245239})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.30455920100212097})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2474367320537567})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.27962177991867065})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.26447153091430664})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2544783651828766})
store['active_learning_steps'][80]['training']['best_epoch']=7
store['active_learning_steps'][80]['evaluation_metrics']={'accuracy': 0.9694, 'crossentropy': 0.251442626953125}
store['active_learning_steps'][80]['eval_training']={}
store['active_learning_steps'][80]['eval_training']['epochs']=[]
store['active_learning_steps'][80]['eval_training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.9533932209014893})
store['active_learning_steps'][80]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.5785660147666931})
store['active_learning_steps'][80]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.39894407987594604})
store['active_learning_steps'][80]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.3364565968513489})
store['active_learning_steps'][80]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.3204619586467743})
store['active_learning_steps'][80]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3195594549179077})
store['active_learning_steps'][80]['eval_training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.26498669385910034})
store['active_learning_steps'][80]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.28384047746658325})
store['active_learning_steps'][80]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.26067012548446655})
store['active_learning_steps'][80]['eval_training']['best_epoch']=9
store['active_learning_steps'][80]['acquisition']={'indices': [11263, 11720, 10516, 14501, 54042, 37622, 35239, 901, 9528, 48880], 'labels': [-1, -1, -1, -1, -1, -1, -1, -1, 8, -1], 'scores': [0.42229974269866943, 0.3725751042366028, 0.45785653591156006, 0.47139978408813477, 0.2859330177307129, 0.4199092388153076, 0.3727477788925171, 0.3952662944793701, 0.3678497076034546, 0.3099103569984436]}
store['active_learning_steps'].append({})
store['active_learning_steps'][81]['training']={}
store['active_learning_steps'][81]['training']['epochs']=[]
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 1.2500910758972168})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.6198031902313232})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.43925851583480835})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.3437998294830322})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3055684566497803})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2854505777359009})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.27593499422073364})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.29796579480171204})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.28300029039382935})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.974609375, 'crossentropy': 0.28887027502059937})
store['active_learning_steps'][81]['training']['best_epoch']=7
store['active_learning_steps'][81]['evaluation_metrics']={'accuracy': 0.9727, 'crossentropy': 0.2488621826171875}
store['active_learning_steps'][81]['eval_training']={}
store['active_learning_steps'][81]['eval_training']['epochs']=[]
store['active_learning_steps'][81]['eval_training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 1.1361939907073975})
store['active_learning_steps'][81]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.5162665843963623})
store['active_learning_steps'][81]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.37727153301239014})
store['active_learning_steps'][81]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.31380409002304077})
store['active_learning_steps'][81]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.30998316407203674})
store['active_learning_steps'][81]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.28039276599884033})
store['active_learning_steps'][81]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2700401544570923})
store['active_learning_steps'][81]['eval_training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.26465222239494324})
store['active_learning_steps'][81]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.26506590843200684})
store['active_learning_steps'][81]['eval_training']['best_epoch']=8
store['active_learning_steps'][81]['acquisition']={'indices': [13942, 42315, 552, 15072, 47124, 30992, 2917, 56935, 15366, 22342], 'labels': [4, -1, -1, -1, -1, -1, -1, -1, 8, -1], 'scores': [0.49948859214782715, 0.5168375968933105, 0.4445995092391968, 0.3340733051300049, 0.3536607027053833, 0.32220375537872314, 0.419289231300354, 0.3808939456939697, 0.2424442172050476, 0.3066396713256836]}
store['active_learning_steps'].append({})
store['active_learning_steps'][82]['training']={}
store['active_learning_steps'][82]['training']['epochs']=[]
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.7900390625, 'crossentropy': 1.2484049797058105})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.5403164625167847})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3638436794281006})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3082558512687683})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2841906249523163})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.2711203992366791})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2616400122642517})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.2508203387260437})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2526057958602905})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.24433104693889618})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9755859375, 'crossentropy': 0.2790810465812683})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.2645273208618164})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.27012205123901367})
store['active_learning_steps'][82]['training']['best_epoch']=10
store['active_learning_steps'][82]['evaluation_metrics']={'accuracy': 0.9742, 'crossentropy': 0.237910546875}
store['active_learning_steps'][82]['eval_training']={}
store['active_learning_steps'][82]['eval_training']['epochs']=[]
store['active_learning_steps'][82]['eval_training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 1.0404489040374756})
store['active_learning_steps'][82]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.551457405090332})
store['active_learning_steps'][82]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.43100646138191223})
store['active_learning_steps'][82]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.30976682901382446})
store['active_learning_steps'][82]['eval_training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.27506470680236816})
store['active_learning_steps'][82]['eval_training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.296500027179718})
store['active_learning_steps'][82]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2714288532733917})
store['active_learning_steps'][82]['eval_training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.25681057572364807})
store['active_learning_steps'][82]['eval_training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.24594765901565552})
store['active_learning_steps'][82]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.23685503005981445})
store['active_learning_steps'][82]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.24401527643203735})
store['active_learning_steps'][82]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2312849909067154})
store['active_learning_steps'][82]['eval_training']['best_epoch']=12
store['active_learning_steps'][82]['acquisition']={'indices': [13873, 22676, 28781, 39136, 20069, 36034, 47086, 37865, 26615, 15238], 'labels': [-1, -1, 7, -1, -1, -1, -1, -1, -1, -1], 'scores': [0.4585895538330078, 0.3217824697494507, 0.5341007709503174, 0.31089913845062256, 0.5425562262535095, 0.3181021213531494, 0.5022243857383728, 0.4022785425186157, 0.3422877788543701, 0.41725486516952515]}
store['active_learning_steps'].append({})
store['active_learning_steps'][83]['training']={}
store['active_learning_steps'][83]['training']['epochs']=[]
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 1.2098459005355835})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.6076187491416931})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.4158586859703064})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3393194079399109})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2866600751876831})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.28131571412086487})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2960933446884155})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.257511705160141})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2639678120613098})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3291752338409424})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.2500542998313904})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.28005555272102356})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2894870340824127})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2613743543624878})
store['active_learning_steps'][83]['training']['best_epoch']=11
store['active_learning_steps'][83]['evaluation_metrics']={'accuracy': 0.972, 'crossentropy': 0.239475439453125}
store['active_learning_steps'][83]['eval_training']={}
store['active_learning_steps'][83]['eval_training']['epochs']=[]
store['active_learning_steps'][83]['eval_training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.8824044466018677})
store['active_learning_steps'][83]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.5332886576652527})
store['active_learning_steps'][83]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.36699312925338745})
store['active_learning_steps'][83]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3349940776824951})
store['active_learning_steps'][83]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.29132387042045593})
store['active_learning_steps'][83]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.28301921486854553})
store['active_learning_steps'][83]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.29351121187210083})
store['active_learning_steps'][83]['eval_training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2501915693283081})
store['active_learning_steps'][83]['eval_training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.28578442335128784})
store['active_learning_steps'][83]['eval_training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.25162380933761597})
store['active_learning_steps'][83]['eval_training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2337135672569275})
store['active_learning_steps'][83]['eval_training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.24789534509181976})
store['active_learning_steps'][83]['eval_training']['epochs'].append({'accuracy': 0.9755859375, 'crossentropy': 0.23009029030799866})
store['active_learning_steps'][83]['eval_training']['best_epoch']=13
store['active_learning_steps'][83]['acquisition']={'indices': [24036, 33347, 45140, 44267, 6715, 20266, 21935, 26565, 45536, 31451], 'labels': [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1], 'scores': [0.35517430305480957, 0.3702167272567749, 0.4820622205734253, 0.4646265506744385, 0.5390361547470093, 0.5015274286270142, 0.514614999294281, 0.5197192430496216, 0.4147685766220093, 0.4988841414451599]}
store['active_learning_steps'].append({})
store['active_learning_steps'][84]['training']={}
store['active_learning_steps'][84]['training']['epochs']=[]
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.763671875, 'crossentropy': 1.2884023189544678})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.6008166074752808})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.4311501383781433})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3464584946632385})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.30830997228622437})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.974609375, 'crossentropy': 0.2737267017364502})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.9755859375, 'crossentropy': 0.24884222447872162})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.98046875, 'crossentropy': 0.25115522742271423})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.2960366904735565})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.9755859375, 'crossentropy': 0.2585827708244324})
store['active_learning_steps'][84]['training']['best_epoch']=7
store['active_learning_steps'][84]['evaluation_metrics']={'accuracy': 0.9726, 'crossentropy': 0.247923876953125}
store['active_learning_steps'][84]['eval_training']={}
store['active_learning_steps'][84]['eval_training']['epochs']=[]
store['active_learning_steps'][84]['eval_training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.9291112422943115})
store['active_learning_steps'][84]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.4874669909477234})
store['active_learning_steps'][84]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3693302273750305})
store['active_learning_steps'][84]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.35233062505722046})
store['active_learning_steps'][84]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.26006197929382324})
store['active_learning_steps'][84]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2698398232460022})
store['active_learning_steps'][84]['eval_training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.2507335841655731})
store['active_learning_steps'][84]['eval_training']['epochs'].append({'accuracy': 0.978515625, 'crossentropy': 0.258369117975235})
store['active_learning_steps'][84]['eval_training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.2425808310508728})
store['active_learning_steps'][84]['eval_training']['best_epoch']=9
store['active_learning_steps'][84]['acquisition']={'indices': [21387, 11572, 22344, 31027, 146, 47614, 53242, 19663, 38448, 46738], 'labels': [-1, 5, -1, -1, -1, -1, 7, -1, 6, -1], 'scores': [0.5280840992927551, 0.6006245613098145, 0.2521715760231018, 0.3124490976333618, 0.3051358461380005, 0.38994550704956055, 0.4147524833679199, 0.5101341009140015, 0.2507534623146057, 0.3487361669540405]}
store['active_learning_steps'].append({})
store['active_learning_steps'][85]['training']={}
store['active_learning_steps'][85]['training']['epochs']=[]
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.76953125, 'crossentropy': 1.2344796657562256})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.5090959072113037})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.38316550850868225})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.28426915407180786})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2534262537956238})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.26312172412872314})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.25523871183395386})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.24606385827064514})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.23450277745723724})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.26286643743515015})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.9765625, 'crossentropy': 0.25353753566741943})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.24718433618545532})
store['active_learning_steps'][85]['training']['best_epoch']=9
store['active_learning_steps'][85]['evaluation_metrics']={'accuracy': 0.9721, 'crossentropy': 0.228336083984375}
