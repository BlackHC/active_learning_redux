store = {}
store['timestamp']=1621483878
store['cmdline']=['/home/kell4989/git/active_learning_redux/batchbald_redux/ood_experiment.py', '--id=79']
store['commit']='8a2cf4fb40ce306533b4e439b08268c53f009a3b'
store['github_url']='8a2cf4fb40ce306533b4e439b08268c53f009a3b'
store['experiment']='/home/kell4989/git/active_learning_redux/batchbald_redux/ood_experiment.py'
store['job_id']=79
store['worker_id']=79
store['num_workers']=80
store['config']={'seed': 1317, 'uniform_ood': False, 'id_dataset_type': 'batchbald_redux.fast_mnist.FastFashionMNIST', 'ood_dataset_type': 'batchbald_redux.fast_mnist.FastMNIST', 'initial_training_set_size': 20, 'validation_set_size': 1024, 'evaluation_set_size': 256, 'id_repetitions': 1, 'ood_repetitions': 1, 'add_dataset_noise': False, 'validation_split_random_state': 0, 'acquisition_size': 5, 'max_training_set': 200, 'num_pool_samples': 100, 'num_validation_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'min_samples_per_epoch': 5056, 'acquisition_function': 'batchbald_redux.acquisition_functions.BatchBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationEvalModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 8}
store['log']={}
store['dataset_info']={'training': "(FastFashionMNIST (train; 58976 samples)) + ('FastMNIST Train (60000 samples)' | constant_target{'target': tensor(-1, device='cuda:0'), 'num_classes': 10})", 'test': "'FastFashionMNIST Test (10000 samples)'"}
store['initial_training_set_indices']=[55573, 380, 12640, 44119, 30392, 58226, 43812, 52440, 3091, 29974, 49512, 46037, 53434, 22015, 37915, 52296, 8533, 58125, 22304, 35472]
store['evaluation_set_indices']=[42890, 40646, 10110, 32775, 33736, 27254, 306, 37354, 19689, 57811, 34482, 15494, 19215, 18819, 11554, 8108, 29048, 30362, 48953, 5588, 8719, 48602, 33140, 46397, 56710, 14640, 39579, 5573, 5715, 47420, 27135, 26129, 16927, 39050, 42295, 51555, 51600, 43234, 33891, 20917, 38856, 17032, 13036, 11228, 46700, 50498, 40741, 9834, 24971, 17759, 45567, 2728, 1774, 33486, 43252, 43803, 50036, 46861, 53831, 54003, 53362, 229, 767, 36270, 10432, 23451, 6612, 8710, 41077, 48498, 46683, 45260, 37098, 55148, 49775, 52801, 15969, 57520, 36797, 34198, 27145, 3029, 37047, 31965, 26501, 48519, 5803, 43415, 35794, 33581, 5897, 27573, 30980, 29614, 35237, 51755, 57690, 26516, 5380, 25589, 53689, 31444, 29950, 44803, 396, 56990, 24052, 12108, 54426, 42320, 35072, 21536, 49304, 49595, 44428, 72, 57175, 52679, 41082, 30184, 54017, 10232, 17968, 31935, 43587, 801, 48031, 2206, 2404, 58741, 29079, 49986, 46464, 17659, 30072, 39879, 29556, 52389, 13092, 37129, 11773, 15822, 37625, 7382, 7121, 17195, 32625, 43141, 28181, 50055, 55187, 34588, 38725, 50466, 40018, 37115, 20801, 23496, 4321, 42102, 12075, 54012, 28833, 18880, 26520, 27580, 14637, 40466, 54800, 24110, 13859, 51027, 45005, 57541, 34361, 26479, 43321, 44048, 45974, 15675, 10508, 49549, 28991, 13074, 9574, 44454, 36688, 8821, 12610, 54422, 34121, 27019, 21800, 44138, 36367, 44100, 33464, 51760, 15917, 495, 50997, 48032, 40334, 21423, 46870, 18137, 4701, 18693, 17506, 6968, 13359, 35372, 7356, 2289, 55733, 5481, 37157, 56054, 2400, 56137, 1005, 56096, 53538, 55783, 37709, 3792, 10664, 5616, 32972, 30013, 19757, 49169, 47417, 38430, 41512, 14035, 35714, 16068, 20076, 26853, 26428, 48521, 11261, 12917, 257, 43981, 8705, 27383, 10113, 7896]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 2.974461078643799})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 3.5078396797180176})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.59375, 'crossentropy': 3.6128201484680176})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 3.969672679901123})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.5986328125, 'crossentropy': 3.9387943744659424})
store['active_learning_steps'][0]['training']['best_epoch']=2
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.5811, 'crossentropy': 3.55248984375}
store['active_learning_steps'][0]['acquisition']={'indices': [['id', 28501], ['id', 4827], ['id', 10620], ['id', 10860], ['id', 4863]], 'labels': [-1, -1, -1, 8, -1], 'scores': [1.4386621162607973, 2.5222297463571746, 3.3428468017132085, 3.890235683635411, 4.217761928822756]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 2.1165108680725098})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 3.04705810546875})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 2.9522688388824463})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 3.1875786781311035})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 3.2497870922088623})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 3.1498351097106934})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 3.3280563354492188})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 3.389923572540283})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 3.4228248596191406})
store['active_learning_steps'][1]['training']['best_epoch']=6
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.6217, 'crossentropy': 3.56911796875}
store['active_learning_steps'][1]['acquisition']={'indices': [['id', 17408], ['id', 25210], ['id', 34438], ['id', 37326], ['id', 45978]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5732188149836772, 2.852892993363083, 3.7054717985033196, 4.1778475222300635, 4.401627547701549]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 2.4583349227905273})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 3.2469143867492676})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 3.9381277561187744})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 3.414628267288208})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 3.6161794662475586})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 4.1640520095825195})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 4.5926642417907715})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 3.9101836681365967})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 3.969736099243164})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 3.551391124725342})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.5966796875, 'crossentropy': 4.937994003295898})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 3.8133277893066406})
store['active_learning_steps'][2]['training']['best_epoch']=9
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.6155, 'crossentropy': 4.22051171875}
store['active_learning_steps'][2]['acquisition']={'indices': [['id', 41744], ['id', 12972], ['id', 11600], ['id', 24172], ['id', 54805]], 'labels': [-1, -1, -1, 4, -1], 'scores': [1.5370264886697866, 2.7630165833481595, 3.650577011385229, 4.199501651565402, 4.432748936599793]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 2.175640821456909})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 2.8827457427978516})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 3.2435097694396973})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 3.331322193145752})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 3.451188087463379})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.59765625, 'crossentropy': 3.6627326011657715})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 3.430825710296631})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 3.6955020427703857})
store['active_learning_steps'][3]['training']['best_epoch']=5
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.5917, 'crossentropy': 3.622497265625}
store['active_learning_steps'][3]['acquisition']={'indices': [['id', 37888], ['id', 25907], ['id', 34438], ['id', 42343], ['id', 43513]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4720833967453177, 2.694135867190893, 3.5801251141073127, 4.084499491858292, 4.335945453617196]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.5947265625, 'crossentropy': 2.1644492149353027})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 3.0628223419189453})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.58984375, 'crossentropy': 3.4377284049987793})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.591796875, 'crossentropy': 3.3607687950134277})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.5966796875, 'crossentropy': 3.616039991378784})
store['active_learning_steps'][4]['training']['best_epoch']=2
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.5906, 'crossentropy': 3.079489453125}
store['active_learning_steps'][4]['acquisition']={'indices': [['id', 14716], ['id', 25051], ['id', 43809], ['id', 27738], ['id', 54805]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4524568765291423, 2.6075619201027056, 3.4362481037712183, 3.9464868717308876, 4.240285949667848]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 2.208815813064575})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 2.831507682800293})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 2.615540027618408})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 3.248739242553711})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 3.2884268760681152})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 3.377108573913574})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 3.662661075592041})
store['active_learning_steps'][5]['training']['best_epoch']=4
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.6124, 'crossentropy': 3.28199296875}
store['active_learning_steps'][5]['acquisition']={'indices': [['id', 11591], ['id', 53479], ['id', 59599], ['id', 41738], ['id', 43294]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.533561350224077, 2.7042331416801475, 3.5370959242202744, 4.047650736874223, 4.328067973676342]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6005859375, 'crossentropy': 2.4989938735961914})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 2.9444146156311035})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 3.1040427684783936})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 3.6150248050689697})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 3.5616774559020996})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 3.59625244140625})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.599609375, 'crossentropy': 4.288789749145508})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 3.534926414489746})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 3.777190685272217})
store['active_learning_steps'][6]['training']['best_epoch']=6
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.6032, 'crossentropy': 3.62934921875}
store['active_learning_steps'][6]['acquisition']={'indices': [['id', 3617], ['id', 10630], ['id', 44732], ['id', 29681], ['id', 59101]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5238109432320317, 2.788571269653982, 3.6526704273169495, 4.145673605494473, 4.4044688445776305]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.587890625, 'crossentropy': 2.3279995918273926})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.5869140625, 'crossentropy': 3.2039263248443604})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 3.444650650024414})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 3.9078149795532227})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 3.590970516204834})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.5966796875, 'crossentropy': 3.8668417930603027})
store['active_learning_steps'][7]['training']['best_epoch']=3
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.6, 'crossentropy': 3.5074390625}
store['active_learning_steps'][7]['acquisition']={'indices': [['id', 14716], ['id', 30150], ['id', 14073], ['id', 58172], ['id', 37341]], 'labels': [-1, -1, -1, -1, 5], 'scores': [1.4545237093439258, 2.5890451775667183, 3.4058446619179996, 3.980120043295207, 4.273272159413592]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 2.277350902557373})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 2.681771993637085})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 2.6773924827575684})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 2.901872158050537})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 3.2993836402893066})
store['active_learning_steps'][8]['training']['best_epoch']=2
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.6159, 'crossentropy': 2.7498658203125}
store['active_learning_steps'][8]['acquisition']={'indices': [['id', 35870], ['id', 37751], ['id', 17985], ['id', 53956], ['id', 48926]], 'labels': [-1, -1, 5, -1, -1], 'scores': [1.4218592341813734, 2.5795232424036083, 3.3920454640505984, 3.913948886298236, 4.21953524195488]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 1.9987976551055908})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 2.4627914428710938})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 2.971148729324341})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 3.3025453090667725})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 3.1706643104553223})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 3.288538932800293})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 3.431849956512451})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 3.7792434692382812})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 3.525956630706787})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 3.6555817127227783})
store['active_learning_steps'][9]['training']['best_epoch']=7
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.6047, 'crossentropy': 3.579353125}
store['active_learning_steps'][9]['acquisition']={'indices': [['id', 28395], ['id', 41197], ['id', 36471], ['id', 34988], ['id', 22807]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4599526222297134, 2.5870274330791956, 3.397556919798282, 3.9448247206849842, 4.250345850938377]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 2.1939001083374023})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 2.9302101135253906})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.5986328125, 'crossentropy': 3.2901177406311035})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.58984375, 'crossentropy': 3.5867271423339844})
store['active_learning_steps'][10]['training']['best_epoch']=1
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.586, 'crossentropy': 2.2991591796875}
store['active_learning_steps'][10]['acquisition']={'indices': [['id', 45048], ['id', 10383], ['id', 4618], ['id', 23564], ['id', 45152]], 'labels': [-1, -1, 2, -1, 0], 'scores': [1.139243483096888, 2.1211523005027453, 2.86340898795952, 3.4587682822021044, 3.8404694307058467]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 2.069037914276123})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 2.9913458824157715})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6005859375, 'crossentropy': 3.5620906352996826})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.5908203125, 'crossentropy': 4.206165790557861})
store['active_learning_steps'][11]['training']['best_epoch']=1
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.5998, 'crossentropy': 2.1655302734375}
store['active_learning_steps'][11]['acquisition']={'indices': [['id', 34616], ['id', 20240], ['id', 50827], ['id', 45122], ['id', 33665]], 'labels': [-1, -1, 9, -1, -1], 'scores': [1.0660662056828183, 1.9617879333822916, 2.6970239869609944, 3.2788024274114544, 3.6872419053347043]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.5869140625, 'crossentropy': 2.1776649951934814})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.57421875, 'crossentropy': 2.8672828674316406})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 2.892812967300415})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 3.0080204010009766})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 3.21189022064209})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.59375, 'crossentropy': 3.6289124488830566})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 3.918975353240967})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 3.4864001274108887})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 3.9584317207336426})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.591796875, 'crossentropy': 4.145013332366943})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 3.727200984954834})
store['active_learning_steps'][12]['training']['best_epoch']=8
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.606, 'crossentropy': 3.4188921875}
store['active_learning_steps'][12]['acquisition']={'indices': [['id', 29766], ['id', 59389], ['id', 6063], ['id', 45422], ['id', 35336]], 'labels': [-1, -1, -1, -1, 8], 'scores': [1.4837148604123802, 2.7882663351656136, 3.7052635026288208, 4.199846849192422, 4.426614213943678]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.578125, 'crossentropy': 2.478825569152832})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 2.6674623489379883})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.5947265625, 'crossentropy': 2.986298084259033})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 3.30977201461792})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.58203125, 'crossentropy': 3.7186026573181152})
store['active_learning_steps'][13]['training']['best_epoch']=2
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.5964, 'crossentropy': 2.7826517578125}
store['active_learning_steps'][13]['acquisition']={'indices': [['id', 40268], ['id', 42583], ['id', 13525], ['id', 36751], ['id', 16909]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.2393168922068802, 2.33096614600667, 3.1560788954811834, 3.765887116976737, 4.121506763463133]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.5927734375, 'crossentropy': 2.0941529273986816})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 2.525693416595459})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 2.966674566268921})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.591796875, 'crossentropy': 3.4537248611450195})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 3.046938419342041})
store['active_learning_steps'][14]['training']['best_epoch']=2
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.5941, 'crossentropy': 2.7832169921875}
store['active_learning_steps'][14]['acquisition']={'indices': [['id', 39662], ['id', 50294], ['id', 33246], ['id', 11111], ['id', 22729]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.2688710271452202, 2.3621718320927076, 3.22890619878914, 3.8140872086467166, 4.147318930232332]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 1.9816685914993286})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6005859375, 'crossentropy': 2.9639675617218018})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.591796875, 'crossentropy': 3.048978567123413})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 3.0242488384246826})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.5986328125, 'crossentropy': 3.5439183712005615})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.5927734375, 'crossentropy': 3.4489307403564453})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.5966796875, 'crossentropy': 3.744577169418335})
store['active_learning_steps'][15]['training']['best_epoch']=4
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.6035, 'crossentropy': 3.2568328125}
store['active_learning_steps'][15]['acquisition']={'indices': [['id', 5967], ['id', 4743], ['id', 47663], ['id', 59669], ['id', 13523]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.389184328035368, 2.451130974575527, 3.3056633294564763, 3.8447705296513446, 4.194651926231731]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.5830078125, 'crossentropy': 2.0723419189453125})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.5849609375, 'crossentropy': 3.005117416381836})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.5869140625, 'crossentropy': 3.1311678886413574})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 3.383007526397705})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.5791015625, 'crossentropy': 3.4586524963378906})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 3.3747034072875977})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.599609375, 'crossentropy': 3.203033447265625})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.59375, 'crossentropy': 3.31793212890625})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6005859375, 'crossentropy': 3.4292759895324707})
store['active_learning_steps'][16]['training']['best_epoch']=6
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.5875, 'crossentropy': 3.58762734375}
store['active_learning_steps'][16]['acquisition']={'indices': [['id', 59278], ['id', 38861], ['id', 42595], ['id', 36834], ['id', 33933]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4166712883046455, 2.6155590141796443, 3.529645295864035, 4.051082197054276, 4.331448553003737]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 2.0072743892669678})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 2.3694543838500977})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 2.7903873920440674})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.5947265625, 'crossentropy': 3.3376078605651855})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 3.2841796875})
store['active_learning_steps'][17]['training']['best_epoch']=2
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.6015, 'crossentropy': 2.5570365234375}
store['active_learning_steps'][17]['acquisition']={'indices': [['id', 14715], ['id', 57728], ['id', 21366], ['id', 8523], ['id', 50294]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.383636930209708, 2.506792547006281, 3.3070608035166584, 3.8687041488429763, 4.188141920175413]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.583984375, 'crossentropy': 2.1777520179748535})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 2.6414804458618164})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 2.800449848175049})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 3.135140895843506})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 3.5638608932495117})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 3.576444149017334})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 3.6000521183013916})
store['active_learning_steps'][18]['training']['best_epoch']=4
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.6092, 'crossentropy': 3.140748828125}
store['active_learning_steps'][18]['acquisition']={'indices': [['id', 42595], ['id', 37665], ['id', 38861], ['id', 36875], ['id', 46826]], 'labels': [-1, -1, -1, -1, 8], 'scores': [1.5310777050560658, 2.7565269454675794, 3.6709588485441955, 4.133925219773838, 4.391687667189135]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.564453125, 'crossentropy': 2.0302391052246094})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.599609375, 'crossentropy': 2.714219093322754})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 2.9723663330078125})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 3.0721817016601562})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 3.166433095932007})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.595703125, 'crossentropy': 3.309769630432129})
store['active_learning_steps'][19]['training']['best_epoch']=3
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.6122, 'crossentropy': 3.0270185546875}
store['active_learning_steps'][19]['acquisition']={'indices': [['id', 12223], ['id', 41188], ['id', 59389], ['id', 29376], ['id', 26740]], 'labels': [-1, -1, -1, 5, -1], 'scores': [1.443568209497358, 2.6439310630389112, 3.47323293736714, 3.984611793830526, 4.282124408749183]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 1.8735023736953735})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 2.493159770965576})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 2.584674596786499})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 2.9386582374572754})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 3.104334831237793})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 2.9240026473999023})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 3.121891975402832})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 3.379748821258545})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 3.250549793243408})
store['active_learning_steps'][20]['training']['best_epoch']=6
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.6321, 'crossentropy': 3.1865203125}
store['active_learning_steps'][20]['acquisition']={'indices': [['id', 30970], ['id', 39663], ['id', 45616], ['id', 5332], ['id', 15296]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4629823250925509, 2.6627108396984607, 3.530889583319418, 4.063223345484869, 4.342127291931796]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 2.092278242111206})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.59375, 'crossentropy': 2.6543962955474854})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 2.791196823120117})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 3.030552625656128})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 2.8809823989868164})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 3.4654650688171387})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 3.3441829681396484})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 3.239658832550049})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 3.180013656616211})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.5927734375, 'crossentropy': 3.3851118087768555})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 3.2631421089172363})
store['active_learning_steps'][21]['training']['best_epoch']=8
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.6173, 'crossentropy': 3.29297890625}
store['active_learning_steps'][21]['acquisition']={'indices': [['id', 25072], ['id', 39627], ['id', 31835], ['id', 33484], ['id', 22062]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5021764022764976, 2.7750000179888517, 3.6824561119393717, 4.165466776131185, 4.410702196022872]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 1.9119815826416016})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 2.2972259521484375})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 2.2530009746551514})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 2.7224409580230713})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 2.9185729026794434})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 2.507234573364258})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 2.7288408279418945})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 2.7622690200805664})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 2.776757001876831})
store['active_learning_steps'][22]['training']['best_epoch']=6
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.6205, 'crossentropy': 2.8871513671875}
store['active_learning_steps'][22]['acquisition']={'indices': [['id', 27238], ['id', 9527], ['id', 18324], ['id', 20142], ['id', 36169]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4970003529674236, 2.7985914192849872, 3.693669553600161, 4.196779643909629, 4.4177970029015]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.5849609375, 'crossentropy': 1.9309595823287964})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 2.146174907684326})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.603515625, 'crossentropy': 2.8926398754119873})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 3.193526268005371})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 3.30820894241333})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6005859375, 'crossentropy': 3.3570244312286377})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.583984375, 'crossentropy': 3.792492389678955})
store['active_learning_steps'][23]['training']['best_epoch']=4
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.5946, 'crossentropy': 3.4559390625}
store['active_learning_steps'][23]['acquisition']={'indices': [['id', 30255], ['id', 28001], ['id', 50294], ['id', 23866], ['id', 44924]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4223708833203552, 2.6951824682579457, 3.5605355980227777, 4.072580986844377, 4.351869440248213]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.595703125, 'crossentropy': 1.9488892555236816})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 2.6861934661865234})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 2.8832955360412598})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.599609375, 'crossentropy': 3.2153401374816895})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 3.2518224716186523})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 3.5345635414123535})
store['active_learning_steps'][24]['training']['best_epoch']=3
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.6039, 'crossentropy': 2.9904181640625}
store['active_learning_steps'][24]['acquisition']={'indices': [['id', 54271], ['id', 25467], ['id', 45942], ['id', 29505], ['id', 756]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4404895002491696, 2.669364047998495, 3.603291212958842, 4.07261149137203, 4.333820108379712]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.58984375, 'crossentropy': 2.287113904953003})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 2.659895181655884})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 2.4841136932373047})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 3.0142641067504883})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.5986328125, 'crossentropy': 3.0056161880493164})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 3.1638035774230957})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 3.4728450775146484})
store['active_learning_steps'][25]['training']['best_epoch']=4
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.613, 'crossentropy': 3.0978013671875}
store['active_learning_steps'][25]['acquisition']={'indices': [['id', 45942], ['id', 48109], ['id', 21525], ['id', 6163], ['id', 16909]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4414356918266849, 2.645269492747061, 3.49972079758973, 4.025545145967933, 4.326803245743679]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 1.8328944444656372})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 2.4425840377807617})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 2.3745031356811523})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.599609375, 'crossentropy': 2.97139310836792})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 3.1099064350128174})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 3.192466974258423})
store['active_learning_steps'][26]['training']['best_epoch']=3
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.6134, 'crossentropy': 2.4312568359375}
store['active_learning_steps'][26]['acquisition']={'indices': [['id', 37148], ['id', 59389], ['id', 25088], ['id', 21864], ['id', 51163]], 'labels': [-1, -1, -1, 2, 0], 'scores': [1.4297805404289996, 2.5281240083625782, 3.419304980754002, 3.9683736744782863, 4.272714263084868]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 1.7650659084320068})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 2.2431540489196777})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 2.60540771484375})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 3.137101650238037})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 2.6987154483795166})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 3.0598020553588867})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 3.370983839035034})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 3.0639567375183105})
store['active_learning_steps'][27]['training']['best_epoch']=5
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.6178, 'crossentropy': 3.0613400390625}
store['active_learning_steps'][27]['acquisition']={'indices': [['id', 12514], ['id', 29766], ['id', 51968], ['id', 30376], ['id', 4899]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.44236732478774, 2.7190554383743253, 3.5886370113302215, 4.071341838487031, 4.337768778898871]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.599609375, 'crossentropy': 1.926761507987976})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 2.525043249130249})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 2.6908373832702637})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 2.9105641841888428})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 3.094261646270752})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 3.418560028076172})
store['active_learning_steps'][28]['training']['best_epoch']=3
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.6152, 'crossentropy': 2.938726953125}
store['active_learning_steps'][28]['acquisition']={'indices': [['id', 42583], ['id', 51764], ['id', 22634], ['id', 4850], ['id', 7206]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4210879609199876, 2.6227736901181533, 3.5115517816771895, 4.028216071935203, 4.308441069041614]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 1.8135242462158203})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 2.8164615631103516})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 2.7829337120056152})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 2.9219608306884766})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.5986328125, 'crossentropy': 3.1932260990142822})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 3.1249423027038574})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 3.310157299041748})
store['active_learning_steps'][29]['training']['best_epoch']=4
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.6072, 'crossentropy': 3.0075001953125}
store['active_learning_steps'][29]['acquisition']={'indices': [['id', 28189], ['id', 12146], ['id', 47634], ['id', 14158], ['id', 8523]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.432522049795748, 2.594480551817771, 3.4645670506741117, 3.9587913248016573, 4.262695427182436]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 1.8805766105651855})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 2.371432304382324})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 2.7809391021728516})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 2.9461779594421387})
store['active_learning_steps'][30]['training']['best_epoch']=1
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.6105, 'crossentropy': 2.02119296875}
store['active_learning_steps'][30]['acquisition']={'indices': [['id', 28395], ['id', 51216], ['id', 3694], ['id', 1254], ['id', 1480]], 'labels': [-1, -1, 2, 0, -1], 'scores': [1.1883899331867922, 2.087972575977247, 2.7994867959695773, 3.374895647633749, 3.78069626346819]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 1.7803056240081787})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 2.112302303314209})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 2.3812789916992188})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 2.781498432159424})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 2.74710750579834})
store['active_learning_steps'][31]['training']['best_epoch']=2
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.6369, 'crossentropy': 2.29123359375}
store['active_learning_steps'][31]['acquisition']={'indices': [['id', 42583], ['id', 44551], ['id', 32776], ['id', 28744], ['id', 25377]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.47907197139401, 2.4926587732639547, 3.286139512339348, 3.8457876477777964, 4.186597118737081]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.599609375, 'crossentropy': 1.8474276065826416})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 2.5902597904205322})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 2.342150926589966})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 2.6845309734344482})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 2.9741079807281494})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 3.3836510181427})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 3.6230382919311523})
store['active_learning_steps'][32]['training']['best_epoch']=4
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.6349, 'crossentropy': 2.8244630859375}
store['active_learning_steps'][32]['acquisition']={'indices': [['id', 17009], ['id', 48420], ['id', 1377], ['id', 24896], ['id', 4899]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4643924876963013, 2.61088169714582, 3.4650521892950277, 4.006653920463064, 4.289631456465461]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 1.7845499515533447})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 2.3804173469543457})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 2.5933642387390137})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 3.159008502960205})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 3.1975927352905273})
store['active_learning_steps'][33]['training']['best_epoch']=2
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.6159, 'crossentropy': 2.5323375}
store['active_learning_steps'][33]['acquisition']={'indices': [['id', 42340], ['id', 16772], ['id', 7113], ['id', 330], ['id', 48046]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.2802781923226467, 2.2568124908563076, 3.095470403494435, 3.6731531265691073, 4.0529024348427365]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 1.6736061573028564})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 2.22666072845459})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 2.567413806915283})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 2.9440395832061768})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 3.2097740173339844})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 3.144829750061035})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 3.456943988800049})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 3.3384904861450195})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 3.382563352584839})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 3.4418888092041016})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 3.475475311279297})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 3.4111175537109375})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 3.533736228942871})
store['active_learning_steps'][34]['training']['best_epoch']=10
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.6438, 'crossentropy': 3.520981640625}
store['active_learning_steps'][34]['acquisition']={'indices': [['id', 25884], ['id', 18324], ['id', 48463], ['id', 9277], ['id', 41008]], 'labels': [-1, -1, -1, 1, -1], 'scores': [1.4376896771919236, 2.674356895432305, 3.512384370202364, 4.026611277429984, 4.295646632621367]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 1.7899909019470215})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 2.100443124771118})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 2.3263137340545654})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 2.5686593055725098})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 2.654984951019287})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 3.0503201484680176})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 2.6075873374938965})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 3.035572052001953})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 2.788886547088623})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 2.9598867893218994})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 2.677093744277954})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 2.9662203788757324})
store['active_learning_steps'][35]['training']['best_epoch']=9
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.6413, 'crossentropy': 3.085573046875}
store['active_learning_steps'][35]['acquisition']={'indices': [['id', 46056], ['id', 56823], ['id', 36283], ['id', 8453], ['id', 34374]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5453367255776072, 2.79761572496199, 3.683610256765636, 4.182491170458637, 4.404545104730868]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.599609375, 'crossentropy': 1.853529930114746})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 2.5968055725097656})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 2.399808883666992})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 2.9655611515045166})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 3.119647741317749})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 3.1508188247680664})
store['active_learning_steps'][36]['training']['best_epoch']=3
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.6267, 'crossentropy': 2.6120263671875}
store['active_learning_steps'][36]['acquisition']={'indices': [['id', 42012], ['id', 30646], ['id', 47584], ['id', 18324], ['id', 55070]], 'labels': [-1, -1, -1, -1, 3], 'scores': [1.499408191258118, 2.6488021229818814, 3.434806889041326, 3.9585066019473096, 4.270948893431838]}
store['active_learning_steps'].append({})
store['active_learning_steps'][37]['training']={}
store['active_learning_steps'][37]['training']['epochs']=[]
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 1.9735325574874878})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 2.710045576095581})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 2.9184651374816895})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 2.9144084453582764})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 3.2783360481262207})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 3.6923084259033203})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 3.4356558322906494})
store['active_learning_steps'][37]['training']['best_epoch']=4
store['active_learning_steps'][37]['evaluation_metrics']={'accuracy': 0.6159, 'crossentropy': 3.3491546875}
store['active_learning_steps'][37]['acquisition']={'indices': [['id', 42741], ['id', 29766], ['id', 36197], ['id', 36323], ['id', 18324]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5094374616691866, 2.7196820059148514, 3.612170981444992, 4.089070710232436, 4.352677020776019]}
store['active_learning_steps'].append({})
store['active_learning_steps'][38]['training']={}
store['active_learning_steps'][38]['training']['epochs']=[]
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 2.010863780975342})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 2.3361778259277344})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 2.6216840744018555})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 2.972433090209961})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 3.0977835655212402})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 3.1750712394714355})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 3.2362608909606934})
store['active_learning_steps'][38]['training']['best_epoch']=4
store['active_learning_steps'][38]['evaluation_metrics']={'accuracy': 0.6232, 'crossentropy': 3.067800390625}
store['active_learning_steps'][38]['acquisition']={'indices': [['id', 9682], ['id', 2268], ['id', 7974], ['id', 35855], ['id', 20142]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.3984266280356215, 2.54040395403379, 3.4077792139841687, 3.93450681044093, 4.241066234991786]}
store['active_learning_steps'].append({})
store['active_learning_steps'][39]['training']={}
store['active_learning_steps'][39]['training']['epochs']=[]
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 1.9022027254104614})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 2.527355670928955})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.603515625, 'crossentropy': 2.7832956314086914})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 3.0598397254943848})
store['active_learning_steps'][39]['training']['best_epoch']=1
store['active_learning_steps'][39]['evaluation_metrics']={'accuracy': 0.6055, 'crossentropy': 1.9047943359375}
store['active_learning_steps'][39]['acquisition']={'indices': [['id', 42340], ['id', 57991], ['id', 49889], ['id', 10785], ['id', 50123]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.2065622752831024, 2.082574356692059, 2.8175096540661704, 3.3563739733608102, 3.7521906139495576]}
store['active_learning_steps'].append({})
store['active_learning_steps'][40]['training']={}
store['active_learning_steps'][40]['training']['epochs']=[]
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 1.821542501449585})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 2.450242519378662})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 2.4240453243255615})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 2.6223196983337402})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 2.885443687438965})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 2.95013427734375})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 3.5422403812408447})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 3.139678478240967})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 3.275743007659912})
store['active_learning_steps'][40]['training']['best_epoch']=6
store['active_learning_steps'][40]['evaluation_metrics']={'accuracy': 0.6162, 'crossentropy': 3.2435498046875}
store['active_learning_steps'][40]['acquisition']={'indices': [['id', 9682], ['id', 21858], ['id', 59389], ['id', 58973], ['id', 15036]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5128001240429887, 2.7506895651093286, 3.6285295908210884, 4.121482602147561, 4.366657924030012]}
store['active_learning_steps'].append({})
store['active_learning_steps'][41]['training']={}
store['active_learning_steps'][41]['training']['epochs']=[]
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 1.681631088256836})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 2.158465623855591})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 2.460012197494507})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 2.7401344776153564})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 2.8451991081237793})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 3.091905117034912})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 3.4777073860168457})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 3.1614019870758057})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 2.842930793762207})
store['active_learning_steps'][41]['training']['best_epoch']=6
store['active_learning_steps'][41]['evaluation_metrics']={'accuracy': 0.6354, 'crossentropy': 3.303612890625}
store['active_learning_steps'][41]['acquisition']={'indices': [['id', 16794], ['id', 59474], ['id', 34262], ['id', 40899], ['id', 10736]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4747979313013042, 2.6363534810772897, 3.5045641680991757, 4.020321984055283, 4.318185997202763]}
store['active_learning_steps'].append({})
store['active_learning_steps'][42]['training']={}
store['active_learning_steps'][42]['training']['epochs']=[]
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 1.9520211219787598})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 2.148982524871826})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 2.6256637573242188})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 2.581500291824341})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 2.824500799179077})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 2.9427928924560547})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 3.227745532989502})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 3.454707622528076})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 3.098367691040039})
store['active_learning_steps'][42]['training']['best_epoch']=6
store['active_learning_steps'][42]['evaluation_metrics']={'accuracy': 0.6202, 'crossentropy': 3.0522201171875}
store['active_learning_steps'][42]['acquisition']={'indices': [['id', 15036], ['id', 23738], ['id', 50410], ['id', 10736], ['id', 38288]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5768940101947, 2.8041565924991594, 3.637470556429137, 4.108452898703245, 4.370511098842657]}
store['active_learning_steps'].append({})
store['active_learning_steps'][43]['training']={}
store['active_learning_steps'][43]['training']['epochs']=[]
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 1.927168369293213})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 2.272721767425537})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 2.4136393070220947})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 2.3488965034484863})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 2.512648105621338})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 2.9828739166259766})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 2.7664856910705566})
store['active_learning_steps'][43]['training']['best_epoch']=4
store['active_learning_steps'][43]['evaluation_metrics']={'accuracy': 0.6426, 'crossentropy': 2.7814794921875}
store['active_learning_steps'][43]['acquisition']={'indices': [['id', 5357], ['id', 21873], ['id', 19042], ['id', 37183], ['id', 8551]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5052724413816103, 2.6281873411681476, 3.466697500948306, 3.9836574685778157, 4.280180976816262]}
store['active_learning_steps'].append({})
store['active_learning_steps'][44]['training']={}
store['active_learning_steps'][44]['training']['epochs']=[]
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 1.9630510807037354})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 2.4411468505859375})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 2.5893659591674805})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 2.6760306358337402})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 3.0014901161193848})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 3.1091060638427734})
store['active_learning_steps'][44]['training']['best_epoch']=3
store['active_learning_steps'][44]['evaluation_metrics']={'accuracy': 0.6252, 'crossentropy': 2.7077541015625}
store['active_learning_steps'][44]['acquisition']={'indices': [['id', 8665], ['id', 25337], ['id', 9689], ['id', 10736], ['id', 10044]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4448485779278886, 2.644265150467965, 3.4429454938972954, 3.9650814316938927, 4.2598934761809915]}
store['active_learning_steps'].append({})
store['active_learning_steps'][45]['training']={}
store['active_learning_steps'][45]['training']['epochs']=[]
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 2.026003837585449})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 2.2413530349731445})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 2.7611353397369385})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 2.808603286743164})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 3.055281162261963})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 3.120574474334717})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 2.9669930934906006})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 3.204150438308716})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 3.1483206748962402})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 3.182785987854004})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 4.284773826599121})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 3.786346912384033})
store['active_learning_steps'][45]['training']['best_epoch']=9
store['active_learning_steps'][45]['evaluation_metrics']={'accuracy': 0.6227, 'crossentropy': 3.547995703125}
store['active_learning_steps'][45]['acquisition']={'indices': [['id', 50666], ['id', 2268], ['id', 1306], ['id', 14506], ['id', 30905]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.6138421325831622, 2.7985004848469925, 3.7077294155530396, 4.192174790590216, 4.418245982851584]}
store['active_learning_steps'].append({})
store['active_learning_steps'][46]['training']={}
store['active_learning_steps'][46]['training']['epochs']=[]
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 1.6988561153411865})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 2.3866424560546875})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 2.531388282775879})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 2.6269302368164062})
store['active_learning_steps'][46]['training']['best_epoch']=1
store['active_learning_steps'][46]['evaluation_metrics']={'accuracy': 0.6216, 'crossentropy': 1.884729296875}
store['active_learning_steps'][46]['acquisition']={'indices': [['id', 42795], ['id', 25349], ['id', 47260], ['id', 12396], ['id', 58316]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.1093389123074577, 2.0062784921212335, 2.7499181916228217, 3.330617145407375, 3.7393732203839605]}
store['active_learning_steps'].append({})
store['active_learning_steps'][47]['training']={}
store['active_learning_steps'][47]['training']['epochs']=[]
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 1.8371272087097168})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.6005859375, 'crossentropy': 2.3907203674316406})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 2.7397913932800293})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 3.137275218963623})
store['active_learning_steps'][47]['training']['best_epoch']=1
store['active_learning_steps'][47]['evaluation_metrics']={'accuracy': 0.6085, 'crossentropy': 1.852203515625}
store['active_learning_steps'][47]['acquisition']={'indices': [['id', 19473], ['id', 39673], ['id', 22679], ['id', 21668], ['id', 31046]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.148577997924881, 2.138772627172864, 2.8719915310192654, 3.4250489950979937, 3.8058666335813953]}
store['active_learning_steps'].append({})
store['active_learning_steps'][48]['training']={}
store['active_learning_steps'][48]['training']['epochs']=[]
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.5966796875, 'crossentropy': 2.018239736557007})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 2.5591847896575928})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.5986328125, 'crossentropy': 2.8806915283203125})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 3.0755598545074463})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 3.4030094146728516})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 3.656486988067627})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 3.2664411067962646})
store['active_learning_steps'][48]['training']['best_epoch']=4
store['active_learning_steps'][48]['evaluation_metrics']={'accuracy': 0.6091, 'crossentropy': 3.37830703125}
store['active_learning_steps'][48]['acquisition']={'indices': [['id', 45462], ['id', 38796], ['id', 6088], ['id', 47156], ['id', 33007]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5266032573757222, 2.703696056001098, 3.567076099880534, 4.089497534743622, 4.3627623007758825]}
store['active_learning_steps'].append({})
store['active_learning_steps'][49]['training']={}
store['active_learning_steps'][49]['training']['epochs']=[]
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.5751953125, 'crossentropy': 2.21701717376709})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.587890625, 'crossentropy': 2.4659271240234375})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 3.084184408187866})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.5966796875, 'crossentropy': 3.029860258102417})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 3.4144644737243652})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 3.4653327465057373})
store['active_learning_steps'][49]['training']['best_epoch']=3
store['active_learning_steps'][49]['evaluation_metrics']={'accuracy': 0.5924, 'crossentropy': 3.21715625}
store['active_learning_steps'][49]['acquisition']={'indices': [['id', 38796], ['id', 28395], ['id', 50294], ['id', 7974], ['id', 45422]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4451181938533584, 2.5751497938062524, 3.4525470461463996, 3.989244398604554, 4.2896682075910295]}
store['active_learning_steps'].append({})
store['active_learning_steps'][50]['training']={}
store['active_learning_steps'][50]['training']['epochs']=[]
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 1.8726856708526611})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 2.297304391860962})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 2.5323243141174316})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 2.8301072120666504})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 2.8999929428100586})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 2.6271004676818848})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 2.918405532836914})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 3.2411274909973145})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 3.335123062133789})
store['active_learning_steps'][50]['training']['best_epoch']=6
store['active_learning_steps'][50]['evaluation_metrics']={'accuracy': 0.6355, 'crossentropy': 2.8469875}
store['active_learning_steps'][50]['acquisition']={'indices': [['id', 4954], ['id', 42832], ['id', 1742], ['id', 3362], ['id', 36157]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5392331548266425, 2.6609024569378414, 3.510135449403913, 4.050453863827434, 4.326715853982979]}
store['active_learning_steps'].append({})
store['active_learning_steps'][51]['training']={}
store['active_learning_steps'][51]['training']['epochs']=[]
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 1.9051593542099})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 2.3170270919799805})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 2.618349075317383})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 2.94905424118042})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 3.1517410278320312})
store['active_learning_steps'][51]['training']['best_epoch']=2
store['active_learning_steps'][51]['evaluation_metrics']={'accuracy': 0.625, 'crossentropy': 2.38499765625}
store['active_learning_steps'][51]['acquisition']={'indices': [['id', 53019], ['id', 4725], ['id', 10317], ['id', 16909], ['id', 42583]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.3836542304932014, 2.4207866271024887, 3.2446266000945645, 3.788297730013687, 4.131201047396216]}
store['active_learning_steps'].append({})
store['active_learning_steps'][52]['training']={}
store['active_learning_steps'][52]['training']['epochs']=[]
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 1.7063050270080566})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 2.3817920684814453})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 2.8066179752349854})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 3.154125213623047})
store['active_learning_steps'][52]['training']['best_epoch']=1
store['active_learning_steps'][52]['evaluation_metrics']={'accuracy': 0.6213, 'crossentropy': 1.75524765625}
store['active_learning_steps'][52]['acquisition']={'indices': [['id', 49389], ['id', 18729], ['id', 12972], ['id', 50619], ['id', 31046]], 'labels': [-1, 3, -1, -1, -1], 'scores': [1.1568080446118292, 2.0573603677540913, 2.7960249088648226, 3.3288808461351778, 3.7171634452144957]}
store['active_learning_steps'].append({})
store['active_learning_steps'][53]['training']={}
store['active_learning_steps'][53]['training']['epochs']=[]
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 1.8860280513763428})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 2.7335586547851562})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 2.50717830657959})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 2.5525288581848145})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 3.240211009979248})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 3.3274080753326416})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 3.574286937713623})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 3.048849582672119})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 3.1155567169189453})
store['active_learning_steps'][53]['training']['best_epoch']=6
store['active_learning_steps'][53]['evaluation_metrics']={'accuracy': 0.6206, 'crossentropy': 3.6340421875}
store['active_learning_steps'][53]['acquisition']={'indices': [['id', 20240], ['id', 32869], ['id', 58855], ['id', 41311], ['id', 4875]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4750174001367133, 2.7041769532818396, 3.586500895426143, 4.132705345067023, 4.389562036718015]}
store['active_learning_steps'].append({})
store['active_learning_steps'][54]['training']={}
store['active_learning_steps'][54]['training']['epochs']=[]
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 1.7650600671768188})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 2.5105154514312744})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 2.5320539474487305})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 2.88860821723938})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 2.8258185386657715})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 3.100978374481201})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 3.2886834144592285})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 3.18660831451416})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 3.526402711868286})
store['active_learning_steps'][54]['training']['best_epoch']=6
store['active_learning_steps'][54]['evaluation_metrics']={'accuracy': 0.6209, 'crossentropy': 3.350583203125}
