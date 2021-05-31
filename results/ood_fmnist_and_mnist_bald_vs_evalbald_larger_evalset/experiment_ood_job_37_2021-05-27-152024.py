store = {}
store['timestamp']=1622125224
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/experiment_ood.py', '--id=37']
store['commit']='687a8dd5b631132403a94f206eb0a7ba2c3b7a98'
store['github_url']='687a8dd5b631132403a94f206eb0a7ba2c3b7a98'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/experiment_ood.py'
store['job_id']=37
store['worker_id']=37
store['num_workers']=80
store['config']={'seed': 1273, 'uniform_ood': True, 'id_dataset_type': 'batchbald_redux.fast_mnist.FastFashionMNIST', 'ood_dataset_type': 'batchbald_redux.fast_mnist.FastMNIST', 'initial_training_set_size': 20, 'validation_set_size': 1024, 'evaluation_set_size': 256, 'id_repetitions': 1, 'ood_repetitions': 1, 'add_dataset_noise': False, 'validation_split_random_state': 0, 'acquisition_size': 5, 'max_training_set': 200, 'num_pool_samples': 100, 'num_validation_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'min_samples_per_epoch': 5056, 'acquisition_function': 'batchbald_redux.acquisition_functions.BatchEvalBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationEvalModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 8}
store['log']={}
store['dataset_info']={'training': "(FastFashionMNIST (train; 58976 samples) | one_hot_targets{'num_classes': 10}) + ('FastMNIST Train (60000 samples)' | uniform_targets{'num_classes': 10})", 'test': "'FastFashionMNIST Test (10000 samples)'"}
store['initial_training_set_indices']=[55573, 380, 12640, 44119, 30392, 58226, 43812, 52440, 3091, 29974, 49512, 46037, 53434, 22015, 37915, 52296, 8533, 58125, 22304, 35472]
store['evaluation_set_indices']=[42890, 40646, 10110, 32775, 33736, 27254, 306, 37354, 19689, 57811, 34482, 15494, 19215, 18819, 11554, 8108, 29048, 30362, 48953, 5588, 8719, 48602, 33140, 46397, 56710, 14640, 39579, 5573, 5715, 47420, 27135, 26129, 16927, 39050, 42295, 51555, 51600, 43234, 33891, 20917, 38856, 17032, 13036, 11228, 46700, 50498, 40741, 9834, 24971, 17759, 45567, 2728, 1774, 33486, 43252, 43803, 50036, 46861, 53831, 54003, 53362, 229, 767, 36270, 10432, 23451, 6612, 8710, 41077, 48498, 46683, 45260, 37098, 55148, 49775, 52801, 15969, 57520, 36797, 34198, 27145, 3029, 37047, 31965, 26501, 48519, 5803, 43415, 35794, 33581, 5897, 27573, 30980, 29614, 35237, 51755, 57690, 26516, 5380, 25589, 53689, 31444, 29950, 44803, 396, 56990, 24052, 12108, 54426, 42320, 35072, 21536, 49304, 49595, 44428, 72, 57175, 52679, 41082, 30184, 54017, 10232, 17968, 31935, 43587, 801, 48031, 2206, 2404, 58741, 29079, 49986, 46464, 17659, 30072, 39879, 29556, 52389, 13092, 37129, 11773, 15822, 37625, 7382, 7121, 17195, 32625, 43141, 28181, 50055, 55187, 34588, 38725, 50466, 40018, 37115, 20801, 23496, 4321, 42102, 12075, 54012, 28833, 18880, 26520, 27580, 14637, 40466, 54800, 24110, 13859, 51027, 45005, 57541, 34361, 26479, 43321, 44048, 45974, 15675, 10508, 49549, 28991, 13074, 9574, 44454, 36688, 8821, 12610, 54422, 34121, 27019, 21800, 44138, 36367, 44100, 33464, 51760, 15917, 495, 50997, 48032, 40334, 21423, 46870, 18137, 4701, 18693, 17506, 6968, 13359, 35372, 7356, 2289, 55733, 5481, 37157, 56054, 2400, 56137, 1005, 56096, 53538, 55783, 37709, 3792, 10664, 5616, 32972, 30013, 19757, 49169, 47417, 38430, 41512, 14035, 35714, 16068, 20076, 26853, 26428, 48521, 11261, 12917, 257, 43981, 8705, 27383, 10113, 7896]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.5888671875, 'crossentropy': 2.432244062423706})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.595703125, 'crossentropy': 3.689999580383301})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.587890625, 'crossentropy': 3.517054319381714})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.591796875, 'crossentropy': 4.013506889343262})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.59765625, 'crossentropy': 3.871218681335449})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.599609375, 'crossentropy': 3.9788312911987305})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 4.223658561706543})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.58984375, 'crossentropy': 5.060093879699707})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.5869140625, 'crossentropy': 4.440949440002441})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.58203125, 'crossentropy': 4.288861274719238})
store['active_learning_steps'][0]['training']['best_epoch']=7
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.5928, 'crossentropy': 4.22281015625}
store['active_learning_steps'][0]['eval_training']={}
store['active_learning_steps'][0]['eval_training']['epochs']=[]
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 1.5383652448654175})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 1.4704458713531494})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.603515625, 'crossentropy': 1.5122703313827515})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 1.5992342233657837})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 1.5975682735443115})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 1.5607008934020996})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 1.48274564743042})
store['active_learning_steps'][0]['eval_training']['best_epoch']=4
store['active_learning_steps'][0]['acquisition']={'indices': [['ood', 20005], ['ood', 49896], ['id', 50827], ['id', 54591], ['id', 42451]], 'labels': [[0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.0496042753307588, 1.8879520235802785, 2.4870734536264223, 2.836905990976504, 3.024217940810008]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 1.7985165119171143})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 2.430321455001831})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 2.8867228031158447})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 2.7927441596984863})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 3.155442714691162})
store['active_learning_steps'][1]['training']['best_epoch']=2
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.599, 'crossentropy': 2.6500873046875}
store['active_learning_steps'][1]['eval_training']={}
store['active_learning_steps'][1]['eval_training']['epochs']=[]
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 1.423388957977295})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 1.4928267002105713})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 1.459384560585022})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 1.4824819564819336})
store['active_learning_steps'][1]['eval_training']['best_epoch']=3
store['active_learning_steps'][1]['acquisition']={'indices': [['id', 48030], ['id', 35776], ['ood', 15686], ['ood', 49185], ['id', 53914]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.8535638966367194, 1.4985356733806068, 2.0132310671821614, 2.315203194640569, 2.5156022113427383]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.58984375, 'crossentropy': 1.9539778232574463})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.5888671875, 'crossentropy': 3.0054478645324707})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.59375, 'crossentropy': 3.226987361907959})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 3.6622416973114014})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.5908203125, 'crossentropy': 3.654247283935547})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.595703125, 'crossentropy': 3.937793731689453})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.5986328125, 'crossentropy': 3.631814479827881})
store['active_learning_steps'][2]['training']['best_epoch']=4
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.5939, 'crossentropy': 3.677143359375}
store['active_learning_steps'][2]['eval_training']={}
store['active_learning_steps'][2]['eval_training']['epochs']=[]
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 1.4708271026611328})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.599609375, 'crossentropy': 1.6868324279785156})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 1.5798664093017578})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 1.7785301208496094})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 1.9499058723449707})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 1.7488266229629517})
store['active_learning_steps'][2]['eval_training']['best_epoch']=3
store['active_learning_steps'][2]['acquisition']={'indices': [['id', 51890], ['id', 25988], ['id', 2762], ['id', 55019], ['id', 20760]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [0.6717846702143202, 1.2489550252439656, 1.7354852698704137, 2.1124172695921963, 2.3659010850107327]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 1.6438922882080078})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.5966796875, 'crossentropy': 2.3248777389526367})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 2.6138992309570312})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 2.8169803619384766})
store['active_learning_steps'][3]['training']['best_epoch']=1
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.603, 'crossentropy': 1.7679119140625}
store['active_learning_steps'][3]['eval_training']={}
store['active_learning_steps'][3]['eval_training']['epochs']=[]
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 1.388479471206665})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 1.3043479919433594})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 1.3519002199172974})
store['active_learning_steps'][3]['eval_training']['best_epoch']=3
store['active_learning_steps'][3]['acquisition']={'indices': [['ood', 31020], ['id', 907], ['id', 14932], ['id', 16361], ['id', 33942]], 'labels': [[0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.5134805261321693, 0.9474053571345755, 1.2816653111737244, 1.574850915473645, 1.8150923656989892]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.583984375, 'crossentropy': 1.5607308149337769})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 2.0030276775360107})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 2.5020337104797363})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 2.7428905963897705})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 2.7732908725738525})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 2.6333017349243164})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 3.1454949378967285})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 2.8630776405334473})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 3.1331210136413574})
store['active_learning_steps'][4]['training']['best_epoch']=6
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.6316, 'crossentropy': 2.7629224609375}
store['active_learning_steps'][4]['eval_training']={}
store['active_learning_steps'][4]['eval_training']['epochs']=[]
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 1.3258284330368042})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 1.3529603481292725})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 1.2999050617218018})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 1.4044840335845947})
store['active_learning_steps'][4]['eval_training']['best_epoch']=1
store['active_learning_steps'][4]['acquisition']={'indices': [['id', 44606], ['id', 30552], ['id', 13195], ['id', 39620], ['id', 44619]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.8223438664999903, 1.4450945268716344, 1.9533495386571804, 2.351633471830927, 2.603186995243713]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.580078125, 'crossentropy': 1.5002741813659668})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 1.9130580425262451})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 2.1903040409088135})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 3.029181957244873})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 2.3587586879730225})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 2.7753710746765137})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 3.0377273559570312})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 2.873413324356079})
store['active_learning_steps'][5]['training']['best_epoch']=5
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.6144, 'crossentropy': 2.914346875}
store['active_learning_steps'][5]['eval_training']={}
store['active_learning_steps'][5]['eval_training']['epochs']=[]
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 1.3020551204681396})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 1.3812048435211182})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 1.4343986511230469})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 1.3893346786499023})
store['active_learning_steps'][5]['eval_training']['best_epoch']=1
store['active_learning_steps'][5]['acquisition']={'indices': [['id', 49472], ['id', 23560], ['ood', 11084], ['id', 56138], ['id', 2535]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.7644415189003739, 1.3951304802011184, 1.8584746758856303, 2.2120242804238153, 2.4546228047097216]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.578125, 'crossentropy': 1.546069622039795})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 1.9429028034210205})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 2.2668232917785645})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 2.445218563079834})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 2.545289993286133})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 3.114192485809326})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 3.1183300018310547})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 3.0889198780059814})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 2.9344310760498047})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 2.9583053588867188})
store['active_learning_steps'][6]['training']['best_epoch']=7
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.619, 'crossentropy': 3.103609375}
store['active_learning_steps'][6]['eval_training']={}
store['active_learning_steps'][6]['eval_training']['epochs']=[]
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 1.3466202020645142})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 1.2722705602645874})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 1.3116317987442017})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 1.394914150238037})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 1.3506462574005127})
store['active_learning_steps'][6]['eval_training']['best_epoch']=2
store['active_learning_steps'][6]['acquisition']={'indices': [['id', 17500], ['id', 57069], ['id', 42198], ['ood', 49026], ['id', 4641]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.7784681661465727, 1.4282313353912741, 1.9634700568383643, 2.3393861648695866, 2.5804211336505976]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 1.328749179840088})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 1.9957265853881836})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 2.1735267639160156})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 2.388563394546509})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 3.089322566986084})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 3.0088586807250977})
store['active_learning_steps'][7]['training']['best_epoch']=3
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.6221, 'crossentropy': 2.2256390625}
store['active_learning_steps'][7]['eval_training']={}
store['active_learning_steps'][7]['eval_training']['epochs']=[]
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 1.1763466596603394})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 1.1669063568115234})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 1.2005832195281982})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 1.2283728122711182})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 1.1910300254821777})
store['active_learning_steps'][7]['eval_training']['best_epoch']=5
store['active_learning_steps'][7]['acquisition']={'indices': [['id', 57018], ['id', 45933], ['id', 38595], ['id', 37005], ['id', 6844]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5938899518616956, 1.1191730756919185, 1.5821646395173108, 1.9575058622369985, 2.24407031498317]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 1.241701602935791})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 1.762014627456665})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 2.168253183364868})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 2.119399070739746})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 2.350327491760254})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 2.8187575340270996})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 2.6842997074127197})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 2.9779763221740723})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 2.814767360687256})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 2.8326215744018555})
store['active_learning_steps'][8]['training']['best_epoch']=7
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.6403, 'crossentropy': 2.72891171875}
store['active_learning_steps'][8]['eval_training']={}
store['active_learning_steps'][8]['eval_training']['epochs']=[]
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 1.2662577629089355})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 1.2464497089385986})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 1.2552765607833862})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 1.2541038990020752})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 1.2632101774215698})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 1.2484385967254639})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 1.2761852741241455})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 1.2587138414382935})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 1.27767014503479})
store['active_learning_steps'][8]['eval_training']['best_epoch']=9
store['active_learning_steps'][8]['acquisition']={'indices': [['id', 32462], ['id', 499], ['id', 14065], ['id', 43275], ['id', 39489]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.7450169594826428, 1.3760580227578654, 1.9184662190994493, 2.353723133798977, 2.649288990578242]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 1.309924840927124})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 1.7370902299880981})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 1.8981786966323853})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 2.1065673828125})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 2.251720428466797})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 2.2327003479003906})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 2.6381235122680664})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 2.405834674835205})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 2.607865333557129})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 2.8193347454071045})
store['active_learning_steps'][9]['training']['best_epoch']=7
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.6323, 'crossentropy': 2.622185546875}
store['active_learning_steps'][9]['eval_training']={}
store['active_learning_steps'][9]['eval_training']['epochs']=[]
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 1.180255651473999})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 1.115095853805542})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 1.1461260318756104})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 1.1792635917663574})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 1.168357253074646})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 1.1683621406555176})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 1.1698997020721436})
store['active_learning_steps'][9]['eval_training']['best_epoch']=4
store['active_learning_steps'][9]['acquisition']={'indices': [['id', 58860], ['id', 40979], ['id', 6943], ['id', 11444], ['id', 36646]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6650050413337418, 1.246862108448561, 1.742672231261265, 2.149894586815691, 2.4243158853736997]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.568359375, 'crossentropy': 1.315382480621338})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 1.5864160060882568})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 1.9201617240905762})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 2.063924551010132})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 2.2170300483703613})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 2.3043570518493652})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 2.5104198455810547})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 2.7043890953063965})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 2.8693032264709473})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 2.8809823989868164})
store['active_learning_steps'][10]['training']['best_epoch']=7
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.6289, 'crossentropy': 2.7555947265625}
store['active_learning_steps'][10]['eval_training']={}
store['active_learning_steps'][10]['eval_training']['epochs']=[]
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 1.117606282234192})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 1.1565382480621338})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 1.116508960723877})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 1.2617534399032593})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 1.1877098083496094})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 1.2267436981201172})
store['active_learning_steps'][10]['eval_training']['best_epoch']=3
store['active_learning_steps'][10]['acquisition']={'indices': [['id', 52961], ['id', 14763], ['id', 54103], ['id', 41558], ['id', 39750]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.7339282778815053, 1.350119169718238, 1.8628525161447107, 2.245243249231537, 2.5256279928824785]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.552734375, 'crossentropy': 1.3765627145767212})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 1.5031476020812988})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 1.8129301071166992})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 2.076528549194336})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 2.5713131427764893})
store['active_learning_steps'][11]['training']['best_epoch']=2
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.6092, 'crossentropy': 1.60182333984375}
store['active_learning_steps'][11]['eval_training']={}
store['active_learning_steps'][11]['eval_training']['epochs']=[]
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 1.1658293008804321})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 1.1461124420166016})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 1.0926049947738647})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 1.0740935802459717})
store['active_learning_steps'][11]['eval_training']['best_epoch']=4
store['active_learning_steps'][11]['acquisition']={'indices': [['id', 57944], ['ood', 30782], ['id', 53054], ['id', 36592], ['id', 59033]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5647455220808026, 1.0952857894698385, 1.5353093635547337, 1.8739469692478083, 2.141193435485457]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.5439453125, 'crossentropy': 1.3322689533233643})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 1.4407204389572144})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 1.5829885005950928})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 1.8925111293792725})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 2.1398699283599854})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 2.0894200801849365})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 2.3247005939483643})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 2.2959940433502197})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 2.1885390281677246})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 2.368072986602783})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 2.442668914794922})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 2.605973243713379})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 2.3578524589538574})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 3.0494775772094727})
store['active_learning_steps'][12]['training']['best_epoch']=11
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.6555, 'crossentropy': 2.525583984375}
store['active_learning_steps'][12]['eval_training']={}
store['active_learning_steps'][12]['eval_training']['epochs']=[]
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 1.0704858303070068})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 1.1281516551971436})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 1.1230319738388062})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 1.1567535400390625})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 1.0930042266845703})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 1.1370929479599})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 1.1826105117797852})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 1.131016731262207})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 1.092250108718872})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 1.1905083656311035})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 1.1483440399169922})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 1.1168179512023926})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 1.130631923675537})
store['active_learning_steps'][12]['eval_training']['best_epoch']=13
store['active_learning_steps'][12]['acquisition']={'indices': [['id', 47482], ['id', 25397], ['id', 35583], ['id', 5134], ['id', 1128]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.7675842205813441, 1.4146900682581123, 1.9874749156916494, 2.4192241089942375, 2.6940795720389623]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.55078125, 'crossentropy': 1.3612719774246216})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 1.449627161026001})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 1.67354416847229})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 2.04386568069458})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 1.9608358144760132})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 2.4511771202087402})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 2.5555481910705566})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 2.6307554244995117})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 2.339250087738037})
store['active_learning_steps'][13]['training']['best_epoch']=6
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.6312, 'crossentropy': 2.429990234375}
store['active_learning_steps'][13]['eval_training']={}
store['active_learning_steps'][13]['eval_training']['epochs']=[]
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 1.1326605081558228})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 1.1229512691497803})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 1.11002779006958})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 1.1700003147125244})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 1.1209207773208618})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 1.1260173320770264})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 1.123090147972107})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 1.205410122871399})
store['active_learning_steps'][13]['eval_training']['best_epoch']=6
store['active_learning_steps'][13]['acquisition']={'indices': [['id', 58915], ['id', 1254], ['id', 43543], ['id', 30767], ['id', 58095]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6231580044404299, 1.166709402334046, 1.6192483184465587, 1.9850159628104649, 2.259023760331427]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.5947265625, 'crossentropy': 1.2881699800491333})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 1.4154576063156128})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 1.6589369773864746})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 1.9097820520401})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 2.1517691612243652})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 2.2073497772216797})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 2.1278581619262695})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 2.2842793464660645})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 2.419262409210205})
store['active_learning_steps'][14]['training']['best_epoch']=6
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.6453, 'crossentropy': 2.1964173828125}
store['active_learning_steps'][14]['eval_training']={}
store['active_learning_steps'][14]['eval_training']['epochs']=[]
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 1.1320524215698242})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 1.0496251583099365})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 1.1702680587768555})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 1.121336579322815})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 1.1558136940002441})
store['active_learning_steps'][14]['eval_training']['best_epoch']=2
store['active_learning_steps'][14]['acquisition']={'indices': [['id', 8919], ['id', 24172], ['id', 20348], ['id', 14436], ['id', 18293]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.7322319377492246, 1.366714348398221, 1.8918605884477637, 2.3085218761015707, 2.577858005343465]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 1.2905464172363281})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 1.323742151260376})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 1.4201130867004395})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 1.6879148483276367})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 2.131746768951416})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 2.224339485168457})
store['active_learning_steps'][15]['training']['best_epoch']=3
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.6414, 'crossentropy': 1.658217578125}
store['active_learning_steps'][15]['eval_training']={}
store['active_learning_steps'][15]['eval_training']['epochs']=[]
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 1.1063454151153564})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 1.060140609741211})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 1.022405982017517})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 1.0360701084136963})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 1.0153958797454834})
store['active_learning_steps'][15]['eval_training']['best_epoch']=5
store['active_learning_steps'][15]['acquisition']={'indices': [['id', 35231], ['id', 7867], ['id', 10700], ['id', 5355], ['id', 13237]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.49689969173273996, 0.9709043613760788, 1.3977582666186263, 1.7363611146185196, 2.0094058188037884]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 1.1474281549453735})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 1.2612335681915283})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 1.4109535217285156})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 1.661197304725647})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 1.7685192823410034})
store['active_learning_steps'][16]['training']['best_epoch']=2
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.6575, 'crossentropy': 1.2409841796875}
store['active_learning_steps'][16]['eval_training']={}
store['active_learning_steps'][16]['eval_training']['epochs']=[]
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 1.086759328842163})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 0.9851088523864746})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 0.9563331604003906})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 0.9506929516792297})
store['active_learning_steps'][16]['eval_training']['best_epoch']=3
store['active_learning_steps'][16]['acquisition']={'indices': [['id', 45785], ['id', 11033], ['id', 55812], ['ood', 38716], ['id', 47462]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.48590720388236575, 0.9197854318106669, 1.2792687514807657, 1.5818954650440826, 1.8194899971832932]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 1.299370288848877})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 1.1533797979354858})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 1.4222662448883057})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 1.7619211673736572})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 2.0613889694213867})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 1.9335122108459473})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 2.0012221336364746})
store['active_learning_steps'][17]['training']['best_epoch']=4
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.666, 'crossentropy': 1.71014921875}
store['active_learning_steps'][17]['eval_training']={}
store['active_learning_steps'][17]['eval_training']['epochs']=[]
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 1.1213992834091187})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 1.0490467548370361})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 1.0239784717559814})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 1.010352611541748})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 0.9877479076385498})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 0.9850210547447205})
store['active_learning_steps'][17]['eval_training']['best_epoch']=6
store['active_learning_steps'][17]['acquisition']={'indices': [['id', 40453], ['id', 16154], ['id', 12860], ['id', 16460], ['id', 12943]], 'labels': [[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6075913337436567, 1.1561626482004717, 1.5897534992966316, 1.9376890164053666, 2.2095246996612428]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.587890625, 'crossentropy': 1.2973978519439697})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 1.1190571784973145})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 1.3072049617767334})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 1.399817943572998})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 1.6846940517425537})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 1.8092663288116455})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 2.06605863571167})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 1.9194101095199585})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 2.066415309906006})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 2.033658504486084})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 2.1358485221862793})
store['active_learning_steps'][18]['training']['best_epoch']=8
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.6873, 'crossentropy': 1.9252708984375}
store['active_learning_steps'][18]['eval_training']={}
store['active_learning_steps'][18]['eval_training']['epochs']=[]
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 1.0562371015548706})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 0.9737697839736938})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 1.0186660289764404})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 0.9645809531211853})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 1.0103604793548584})
store['active_learning_steps'][18]['eval_training']['best_epoch']=2
store['active_learning_steps'][18]['acquisition']={'indices': [['ood', 56543], ['id', 36715], ['id', 47161], ['id', 13179], ['id', 48160]], 'labels': [[0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6817142923187403, 1.3179646155494602, 1.8769326894360958, 2.3080830187196906, 2.617963535913729]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 1.2253057956695557})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 1.0958271026611328})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 1.338507056236267})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.3856027126312256})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 1.4745385646820068})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 1.5409865379333496})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 1.8147540092468262})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 1.807354211807251})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 1.8217365741729736})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 1.7741215229034424})
store['active_learning_steps'][19]['training']['best_epoch']=7
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.6878, 'crossentropy': 1.8248951171875}
store['active_learning_steps'][19]['eval_training']={}
store['active_learning_steps'][19]['eval_training']['epochs']=[]
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 1.0498565435409546})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 0.9471386671066284})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 0.9666000604629517})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 0.9684425592422485})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 0.9406536817550659})
store['active_learning_steps'][19]['eval_training']['best_epoch']=2
store['active_learning_steps'][19]['acquisition']={'indices': [['id', 18557], ['id', 29728], ['id', 14697], ['id', 44447], ['id', 22875]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.7127027937140045, 1.3697103875821628, 1.9280480791105532, 2.315487861005135, 2.597803315176148]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.5927734375, 'crossentropy': 1.2704375982284546})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 1.132825255393982})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 1.2057480812072754})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 1.401253342628479})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 1.6462609767913818})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 1.4743518829345703})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 1.9102630615234375})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.803180456161499})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 1.8349255323410034})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 1.6943516731262207})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 1.9899659156799316})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 1.9633219242095947})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 2.07405424118042})
store['active_learning_steps'][20]['training']['best_epoch']=10
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.6991, 'crossentropy': 1.9175462890625}
store['active_learning_steps'][20]['eval_training']={}
store['active_learning_steps'][20]['eval_training']['epochs']=[]
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 1.0814762115478516})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 0.9730756878852844})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 0.9520801305770874})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 0.9504275321960449})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 0.9343324303627014})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 0.9383025765419006})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.712890625, 'crossentropy': 0.9295128583908081})
store['active_learning_steps'][20]['eval_training']['best_epoch']=4
store['active_learning_steps'][20]['acquisition']={'indices': [['id', 50582], ['id', 19018], ['id', 22507], ['id', 21887], ['id', 29885]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [0.6999039903005404, 1.3379803080562773, 1.8493665650699054, 2.2330357915990033, 2.501104861693893]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.5634765625, 'crossentropy': 1.3599083423614502})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 1.0671465396881104})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 1.1750938892364502})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 1.5222198963165283})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 1.596339225769043})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 1.7077579498291016})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 1.6415326595306396})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 1.8337794542312622})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 1.8692879676818848})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 1.9727342128753662})
store['active_learning_steps'][21]['training']['best_epoch']=7
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.6975, 'crossentropy': 1.76417890625}
store['active_learning_steps'][21]['eval_training']={}
store['active_learning_steps'][21]['eval_training']['epochs']=[]
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 1.069334864616394})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 0.9746049642562866})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 1.033447504043579})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 0.989905595779419})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 1.0192373991012573})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 1.0353777408599854})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 1.0177096128463745})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 1.0712960958480835})
store['active_learning_steps'][21]['eval_training']['best_epoch']=5
store['active_learning_steps'][21]['acquisition']={'indices': [['ood', 13650], ['ood', 53746], ['id', 27593], ['id', 24269], ['id', 34452]], 'labels': [[0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.6061575002045736, 1.1738731879132667, 1.6621239738258593, 2.025500315820808, 2.278012760354149]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.57421875, 'crossentropy': 1.3364548683166504})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 1.1456732749938965})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 1.1489357948303223})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 1.467667579650879})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.728515625, 'crossentropy': 1.4059768915176392})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 1.7291245460510254})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 1.8205609321594238})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 1.632755994796753})
store['active_learning_steps'][22]['training']['best_epoch']=5
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.7115, 'crossentropy': 1.465883203125}
store['active_learning_steps'][22]['eval_training']={}
store['active_learning_steps'][22]['eval_training']['epochs']=[]
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 1.098515272140503})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 1.0373369455337524})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 0.92201167345047})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.716796875, 'crossentropy': 0.9355029463768005})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 0.9297527074813843})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.724609375, 'crossentropy': 0.8986015319824219})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.7255859375, 'crossentropy': 0.9228901863098145})
store['active_learning_steps'][22]['eval_training']['best_epoch']=7
store['active_learning_steps'][22]['acquisition']={'indices': [['id', 48954], ['id', 42265], ['id', 10882], ['id', 13318], ['id', 59855]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6614782021864163, 1.19959637774627, 1.6250577095501244, 1.9561549095780117, 2.2180181194909308]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.5654296875, 'crossentropy': 1.3309659957885742})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 1.1464624404907227})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 1.1373395919799805})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 1.343196153640747})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 1.5207840204238892})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 1.486208438873291})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 1.6614034175872803})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 1.7672638893127441})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.712890625, 'crossentropy': 1.7787353992462158})
store['active_learning_steps'][23]['training']['best_epoch']=6
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.7011, 'crossentropy': 1.5586123046875}
store['active_learning_steps'][23]['eval_training']={}
store['active_learning_steps'][23]['eval_training']['epochs']=[]
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 1.1223413944244385})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 0.9626951217651367})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 0.9589900374412537})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 0.958000898361206})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 0.9628776907920837})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 0.9862438440322876})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 0.9662264585494995})
store['active_learning_steps'][23]['eval_training']['best_epoch']=4
store['active_learning_steps'][23]['acquisition']={'indices': [['id', 46619], ['id', 49410], ['id', 27074], ['id', 45156], ['id', 29550]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.5677030029719976, 1.0858352457392746, 1.5239605805948466, 1.873637222075672, 2.1134179237734187]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.572265625, 'crossentropy': 1.30381441116333})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 1.1666433811187744})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.1818407773971558})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 1.4355758428573608})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 1.4552035331726074})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 1.5354444980621338})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 1.7014434337615967})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 1.7941162586212158})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 1.67081880569458})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 1.741369605064392})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 1.9292569160461426})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.712890625, 'crossentropy': 1.9680885076522827})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 2.097336769104004})
store['active_learning_steps'][24]['training']['best_epoch']=10
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.7021, 'crossentropy': 1.91195078125}
store['active_learning_steps'][24]['eval_training']={}
store['active_learning_steps'][24]['eval_training']['epochs']=[]
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 1.116011142730713})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 0.980828583240509})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 0.990554690361023})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 0.9834282398223877})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 0.9709492325782776})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 0.9848780035972595})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 1.0315728187561035})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 0.970036506652832})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 1.006682276725769})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 0.9990777969360352})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 1.017447590827942})
store['active_learning_steps'][24]['eval_training']['best_epoch']=8
store['active_learning_steps'][24]['acquisition']={'indices': [['id', 20638], ['id', 10960], ['id', 15290], ['id', 8397], ['id', 56287]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.7371700892164239, 1.3315293099736714, 1.8105763437591182, 2.196055646469893, 2.4464345920414754]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 1.280111312866211})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 1.0985941886901855})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 1.1414157152175903})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 1.3318586349487305})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 1.5621976852416992})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.7275390625, 'crossentropy': 1.4539623260498047})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 1.7199937105178833})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 1.8902949094772339})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.716796875, 'crossentropy': 1.654357671737671})
store['active_learning_steps'][25]['training']['best_epoch']=6
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.698, 'crossentropy': 1.54629375}
store['active_learning_steps'][25]['eval_training']={}
store['active_learning_steps'][25]['eval_training']['epochs']=[]
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 1.0713779926300049})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 0.9739748239517212})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 0.9067661762237549})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 0.9216675758361816})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 0.8918857574462891})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 0.8970605134963989})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 0.8971735239028931})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 0.914095938205719})
store['active_learning_steps'][25]['eval_training']['best_epoch']=7
store['active_learning_steps'][25]['acquisition']={'indices': [['id', 14770], ['id', 4752], ['id', 16797], ['id', 53668], ['id', 2644]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6693602618014991, 1.2197299795319223, 1.7009347129922547, 2.071959117188409, 2.3420389502014887]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.5703125, 'crossentropy': 1.2921996116638184})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 1.044372320175171})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 1.2138237953186035})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 1.2513138055801392})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 1.4402751922607422})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 1.6269962787628174})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 1.7207417488098145})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 1.582693338394165})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 1.9727399349212646})
store['active_learning_steps'][26]['training']['best_epoch']=6
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.6906, 'crossentropy': 1.60453037109375}
store['active_learning_steps'][26]['eval_training']={}
store['active_learning_steps'][26]['eval_training']['epochs']=[]
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 1.068356990814209})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 0.9740894436836243})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 0.9126420021057129})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 0.9445284605026245})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 0.9156926274299622})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 0.9648056030273438})
store['active_learning_steps'][26]['eval_training']['best_epoch']=3
store['active_learning_steps'][26]['acquisition']={'indices': [['id', 23980], ['id', 36107], ['id', 5374], ['id', 19842], ['id', 1014]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.5551673446137821, 1.0737461071489305, 1.5329487510992221, 1.910627930358177, 2.18480851941427]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.58203125, 'crossentropy': 1.2688968181610107})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 1.1123690605163574})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 1.0988366603851318})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 1.2278289794921875})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 1.4548392295837402})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.5590381622314453})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 1.7605738639831543})
store['active_learning_steps'][27]['training']['best_epoch']=4
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.6804, 'crossentropy': 1.28185673828125}
store['active_learning_steps'][27]['eval_training']={}
store['active_learning_steps'][27]['eval_training']['epochs']=[]
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 1.0988601446151733})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 0.9546315670013428})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 0.9736331105232239})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 0.9123526811599731})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 0.9031249284744263})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 0.8851160407066345})
store['active_learning_steps'][27]['eval_training']['best_epoch']=6
store['active_learning_steps'][27]['acquisition']={'indices': [['id', 57000], ['id', 33964], ['id', 52509], ['id', 45148], ['id', 27699]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6225481101426475, 1.1143211439677931, 1.5078676540649747, 1.840960245501842, 2.0954813826070477]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.5908203125, 'crossentropy': 1.3432023525238037})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 1.0217311382293701})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 1.0321699380874634})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 1.1098567247390747})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 1.3249932527542114})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 1.4201040267944336})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 1.4064278602600098})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.716796875, 'crossentropy': 1.5071228742599487})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.728515625, 'crossentropy': 1.7566230297088623})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.7255859375, 'crossentropy': 1.8674819469451904})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 1.8247175216674805})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.728515625, 'crossentropy': 1.7011523246765137})
store['active_learning_steps'][28]['training']['best_epoch']=9
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.7086, 'crossentropy': 1.7687583984375}
store['active_learning_steps'][28]['eval_training']={}
store['active_learning_steps'][28]['eval_training']['epochs']=[]
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 1.068084955215454})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 0.9453364610671997})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.71484375, 'crossentropy': 0.9115549325942993})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 0.9361882209777832})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 0.9073870182037354})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.724609375, 'crossentropy': 0.9229837656021118})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.7236328125, 'crossentropy': 0.8825383186340332})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.7275390625, 'crossentropy': 0.9474219679832458})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.724609375, 'crossentropy': 0.9395097494125366})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 0.9694758653640747})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.73046875, 'crossentropy': 0.9326897859573364})
store['active_learning_steps'][28]['eval_training']['best_epoch']=11
store['active_learning_steps'][28]['acquisition']={'indices': [['id', 43592], ['id', 20144], ['id', 49921], ['id', 27829], ['ood', 14753]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.6180279670645694, 1.195347988542375, 1.6891414892807406, 2.062498037466886, 2.341244135242559]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.5498046875, 'crossentropy': 1.327933669090271})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 1.113417387008667})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 1.0783052444458008})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 1.1094627380371094})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 1.177740216255188})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 1.3460561037063599})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 1.4847910404205322})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 1.5873286724090576})
store['active_learning_steps'][29]['training']['best_epoch']=5
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.6984, 'crossentropy': 1.28104482421875}
store['active_learning_steps'][29]['eval_training']={}
store['active_learning_steps'][29]['eval_training']['epochs']=[]
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 1.0617034435272217})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 0.9646199941635132})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 0.8840551376342773})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.712890625, 'crossentropy': 0.8757514953613281})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 0.8671562075614929})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 0.8788087368011475})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.716796875, 'crossentropy': 0.8303248882293701})
store['active_learning_steps'][29]['eval_training']['best_epoch']=5
store['active_learning_steps'][29]['acquisition']={'indices': [['id', 20606], ['id', 27800], ['id', 4821], ['id', 34753], ['id', 31256]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5468092189326146, 1.0445978316704432, 1.4635922845096618, 1.8270804701510217, 2.1245638668719247]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 1.2710726261138916})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 1.0578820705413818})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 1.0782737731933594})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 1.222116231918335})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 1.198958158493042})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 1.4293217658996582})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 1.493730068206787})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 1.7285618782043457})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.71484375, 'crossentropy': 1.719419002532959})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 1.9423959255218506})
store['active_learning_steps'][30]['training']['best_epoch']=7
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.6986, 'crossentropy': 1.57580595703125}
store['active_learning_steps'][30]['eval_training']={}
store['active_learning_steps'][30]['eval_training']['epochs']=[]
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 1.0514378547668457})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 0.9764502644538879})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.712890625, 'crossentropy': 0.9095439910888672})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 0.9259597063064575})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.7216796875, 'crossentropy': 0.9102845788002014})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 0.9196462631225586})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.71484375, 'crossentropy': 0.9466686844825745})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.7255859375, 'crossentropy': 0.9048187732696533})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 0.9196918606758118})
store['active_learning_steps'][30]['eval_training']['best_epoch']=8
store['active_learning_steps'][30]['acquisition']={'indices': [['id', 15738], ['id', 44011], ['id', 50770], ['id', 34338], ['id', 49919]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5656417654359451, 1.062312270395858, 1.4727256073788242, 1.816419983225524, 2.0802761067651314]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.5888671875, 'crossentropy': 1.2719882726669312})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 1.0480830669403076})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.72265625, 'crossentropy': 1.021425485610962})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 1.1156586408615112})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.7294921875, 'crossentropy': 1.2529218196868896})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.712890625, 'crossentropy': 1.3440972566604614})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 1.5211749076843262})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.7255859375, 'crossentropy': 1.5341260433197021})
store['active_learning_steps'][31]['training']['best_epoch']=5
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.7199, 'crossentropy': 1.26537705078125}
store['active_learning_steps'][31]['eval_training']={}
store['active_learning_steps'][31]['eval_training']['epochs']=[]
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 1.0129809379577637})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 0.9568183422088623})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 0.8863755464553833})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 0.8896933794021606})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.71484375, 'crossentropy': 0.8638759851455688})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.72265625, 'crossentropy': 0.8511857986450195})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 0.862553596496582})
store['active_learning_steps'][31]['eval_training']['best_epoch']=6
store['active_learning_steps'][31]['acquisition']={'indices': [['id', 41355], ['id', 59860], ['id', 13191], ['id', 20946], ['id', 15678]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5602836741598507, 1.029121732817075, 1.4371943555112434, 1.7650990745635013, 2.0122663882908896]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.5830078125, 'crossentropy': 1.3229591846466064})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 1.0644445419311523})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 1.0473320484161377})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.7265625, 'crossentropy': 1.1209030151367188})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 1.2164130210876465})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.7275390625, 'crossentropy': 1.2830495834350586})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.7265625, 'crossentropy': 1.430971384048462})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.7275390625, 'crossentropy': 1.5135905742645264})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.7255859375, 'crossentropy': 1.7461861371994019})
store['active_learning_steps'][32]['training']['best_epoch']=6
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.7159, 'crossentropy': 1.38253095703125}
store['active_learning_steps'][32]['eval_training']={}
store['active_learning_steps'][32]['eval_training']['epochs']=[]
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 0.9889529943466187})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 0.958690881729126})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.72265625, 'crossentropy': 0.9211215972900391})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 0.8870353102684021})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.7294921875, 'crossentropy': 0.8706763386726379})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.7314453125, 'crossentropy': 0.8540101051330566})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.734375, 'crossentropy': 0.859616756439209})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.728515625, 'crossentropy': 0.854144811630249})
store['active_learning_steps'][32]['eval_training']['best_epoch']=7
store['active_learning_steps'][32]['acquisition']={'indices': [['id', 34851], ['id', 16076], ['id', 38156], ['ood', 12747], ['id', 23149]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5818322452364846, 1.1122065907960883, 1.5846091077054103, 1.9822550475410399, 2.2558550330096114]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.5830078125, 'crossentropy': 1.3442120552062988})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 1.0191662311553955})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 1.0911216735839844})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.1253198385238647})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 1.175339937210083})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 1.2599214315414429})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 1.3758630752563477})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 1.4472157955169678})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.724609375, 'crossentropy': 1.4208964109420776})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 1.599583625793457})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 1.6913254261016846})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.72265625, 'crossentropy': 1.6353811025619507})
store['active_learning_steps'][33]['training']['best_epoch']=9
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.714, 'crossentropy': 1.55943984375}
store['active_learning_steps'][33]['eval_training']={}
store['active_learning_steps'][33]['eval_training']['epochs']=[]
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 1.1217069625854492})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 0.9328851699829102})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 0.9347552061080933})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 0.8828756809234619})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 0.9031012058258057})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.716796875, 'crossentropy': 0.9068920016288757})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.7236328125, 'crossentropy': 0.8852359056472778})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.716796875, 'crossentropy': 0.9213681221008301})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 0.9068330526351929})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.716796875, 'crossentropy': 0.9340299963951111})
store['active_learning_steps'][33]['eval_training']['best_epoch']=7
store['active_learning_steps'][33]['acquisition']={'indices': [['id', 9692], ['id', 8900], ['id', 50367], ['id', 25321], ['id', 29882]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.6237215487357819, 1.2028212345933524, 1.6717139142531403, 2.0086225943680365, 2.2421009847768394]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 1.1826545000076294})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 1.0067431926727295})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 1.1086055040359497})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.736328125, 'crossentropy': 1.045973777770996})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.7255859375, 'crossentropy': 1.179787039756775})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.736328125, 'crossentropy': 1.2319283485412598})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 1.586935043334961})
store['active_learning_steps'][34]['training']['best_epoch']=4
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.7144, 'crossentropy': 1.108025390625}
store['active_learning_steps'][34]['eval_training']={}
store['active_learning_steps'][34]['eval_training']['epochs']=[]
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 1.0674653053283691})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 0.8783408999443054})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 0.9222920536994934})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.716796875, 'crossentropy': 0.8913289308547974})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 0.8527912497520447})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.7294921875, 'crossentropy': 0.8462866544723511})
store['active_learning_steps'][34]['eval_training']['best_epoch']=6
store['active_learning_steps'][34]['acquisition']={'indices': [['id', 50815], ['id', 34620], ['id', 38782], ['id', 35309], ['id', 16490]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.4817766193350006, 0.9100062599997214, 1.3068828783533255, 1.645219812311593, 1.9084845975292613]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.568359375, 'crossentropy': 1.381908655166626})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.0101531744003296})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 1.067732572555542})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 1.1109058856964111})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 1.18310546875})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 1.2632107734680176})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.716796875, 'crossentropy': 1.4140408039093018})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 1.409993052482605})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 1.6089001893997192})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.7275390625, 'crossentropy': 1.4477572441101074})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.72265625, 'crossentropy': 1.7499849796295166})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.728515625, 'crossentropy': 1.7536776065826416})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.7216796875, 'crossentropy': 1.7315406799316406})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.728515625, 'crossentropy': 1.8740110397338867})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.72265625, 'crossentropy': 1.9029150009155273})
store['active_learning_steps'][35]['training']['best_epoch']=12
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.7179, 'crossentropy': 1.8581388671875}
store['active_learning_steps'][35]['eval_training']={}
store['active_learning_steps'][35]['eval_training']['epochs']=[]
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 1.0327298641204834})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 0.9558051824569702})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 0.9007983803749084})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.7255859375, 'crossentropy': 0.9497365951538086})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.7265625, 'crossentropy': 0.9632789492607117})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 0.9739133715629578})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.7275390625, 'crossentropy': 0.9970608949661255})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.7255859375, 'crossentropy': 1.013726830482483})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.7333984375, 'crossentropy': 0.9917001724243164})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.7314453125, 'crossentropy': 0.958914041519165})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.7392578125, 'crossentropy': 0.9691777229309082})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.732421875, 'crossentropy': 0.9926842451095581})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.740234375, 'crossentropy': 1.0008790493011475})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.7314453125, 'crossentropy': 1.0410947799682617})
store['active_learning_steps'][35]['eval_training']['best_epoch']=13
store['active_learning_steps'][35]['acquisition']={'indices': [['id', 43780], ['ood', 58391], ['id', 5990], ['id', 35271], ['id', 36245]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.622796943537582, 1.1931764035306447, 1.6965027887768231, 2.134954173729791, 2.453009449363619]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 1.2126379013061523})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 1.0065314769744873})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 1.0065019130706787})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 1.1488535404205322})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 1.3059167861938477})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 1.393986701965332})
store['active_learning_steps'][36]['training']['best_epoch']=3
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.7113, 'crossentropy': 1.0186884765625}
