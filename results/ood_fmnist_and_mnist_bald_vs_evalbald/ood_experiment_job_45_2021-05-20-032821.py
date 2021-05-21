store = {}
store['timestamp']=1621477701
store['cmdline']=['/home/kell4989/git/active_learning_redux/batchbald_redux/ood_experiment.py', '--id=45']
store['commit']='8a2cf4fb40ce306533b4e439b08268c53f009a3b'
store['github_url']='8a2cf4fb40ce306533b4e439b08268c53f009a3b'
store['experiment']='/home/kell4989/git/active_learning_redux/batchbald_redux/ood_experiment.py'
store['job_id']=45
store['worker_id']=45
store['num_workers']=80
store['config']={'seed': 1281, 'uniform_ood': True, 'id_dataset_type': 'batchbald_redux.fast_mnist.FastFashionMNIST', 'ood_dataset_type': 'batchbald_redux.fast_mnist.FastMNIST', 'initial_training_set_size': 20, 'validation_set_size': 1024, 'evaluation_set_size': 256, 'id_repetitions': 1, 'ood_repetitions': 1, 'add_dataset_noise': False, 'validation_split_random_state': 0, 'acquisition_size': 5, 'max_training_set': 200, 'num_pool_samples': 100, 'num_validation_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'min_samples_per_epoch': 5056, 'acquisition_function': 'batchbald_redux.acquisition_functions.BatchBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationEvalModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 8}
store['log']={}
store['dataset_info']={'training': "(FastFashionMNIST (train; 58976 samples) | one_hot_targets{'num_classes': 10}) + ('FastMNIST Train (60000 samples)' | uniform_targets{'num_classes': 10})", 'test': "'FastFashionMNIST Test (10000 samples)'"}
store['initial_training_set_indices']=[55573, 380, 12640, 44119, 30392, 58226, 43812, 52440, 3091, 29974, 49512, 46037, 53434, 22015, 37915, 52296, 8533, 58125, 22304, 35472]
store['evaluation_set_indices']=[42890, 40646, 10110, 32775, 33736, 27254, 306, 37354, 19689, 57811, 34482, 15494, 19215, 18819, 11554, 8108, 29048, 30362, 48953, 5588, 8719, 48602, 33140, 46397, 56710, 14640, 39579, 5573, 5715, 47420, 27135, 26129, 16927, 39050, 42295, 51555, 51600, 43234, 33891, 20917, 38856, 17032, 13036, 11228, 46700, 50498, 40741, 9834, 24971, 17759, 45567, 2728, 1774, 33486, 43252, 43803, 50036, 46861, 53831, 54003, 53362, 229, 767, 36270, 10432, 23451, 6612, 8710, 41077, 48498, 46683, 45260, 37098, 55148, 49775, 52801, 15969, 57520, 36797, 34198, 27145, 3029, 37047, 31965, 26501, 48519, 5803, 43415, 35794, 33581, 5897, 27573, 30980, 29614, 35237, 51755, 57690, 26516, 5380, 25589, 53689, 31444, 29950, 44803, 396, 56990, 24052, 12108, 54426, 42320, 35072, 21536, 49304, 49595, 44428, 72, 57175, 52679, 41082, 30184, 54017, 10232, 17968, 31935, 43587, 801, 48031, 2206, 2404, 58741, 29079, 49986, 46464, 17659, 30072, 39879, 29556, 52389, 13092, 37129, 11773, 15822, 37625, 7382, 7121, 17195, 32625, 43141, 28181, 50055, 55187, 34588, 38725, 50466, 40018, 37115, 20801, 23496, 4321, 42102, 12075, 54012, 28833, 18880, 26520, 27580, 14637, 40466, 54800, 24110, 13859, 51027, 45005, 57541, 34361, 26479, 43321, 44048, 45974, 15675, 10508, 49549, 28991, 13074, 9574, 44454, 36688, 8821, 12610, 54422, 34121, 27019, 21800, 44138, 36367, 44100, 33464, 51760, 15917, 495, 50997, 48032, 40334, 21423, 46870, 18137, 4701, 18693, 17506, 6968, 13359, 35372, 7356, 2289, 55733, 5481, 37157, 56054, 2400, 56137, 1005, 56096, 53538, 55783, 37709, 3792, 10664, 5616, 32972, 30013, 19757, 49169, 47417, 38430, 41512, 14035, 35714, 16068, 20076, 26853, 26428, 48521, 11261, 12917, 257, 43981, 8705, 27383, 10113, 7896]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 2.57702374458313})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 2.891390323638916})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 3.252559185028076})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 3.60660982131958})
store['active_learning_steps'][0]['training']['best_epoch']=1
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.6083, 'crossentropy': 2.48582421875}
store['active_learning_steps'][0]['acquisition']={'indices': [['id', 6804], ['id', 20960], ['id', 14047], ['id', 38796], ['id', 16971]], 'labels': [[0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [1.5710294582342859, 2.5881961995654086, 3.372539167123451, 3.879621130653165, 4.187008734001379]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.595703125, 'crossentropy': 1.6525912284851074})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 2.325932741165161})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 2.7479195594787598})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.59375, 'crossentropy': 2.791623592376709})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.5947265625, 'crossentropy': 3.028040647506714})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.603515625, 'crossentropy': 2.9356203079223633})
store['active_learning_steps'][1]['training']['best_epoch']=3
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.5881, 'crossentropy': 2.8216853515625}
store['active_learning_steps'][1]['acquisition']={'indices': [['id', 38806], ['id', 28431], ['id', 59468], ['id', 56587], ['id', 27791]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [1.0233169755654317, 1.873706119298034, 2.606262380877613, 3.2006193013106508, 3.6480114681521467]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.5830078125, 'crossentropy': 1.6661311388015747})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.591796875, 'crossentropy': 2.1520681381225586})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.5859375, 'crossentropy': 2.7111501693725586})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.5986328125, 'crossentropy': 2.693856716156006})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 2.6030774116516113})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.5927734375, 'crossentropy': 2.9398837089538574})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.59375, 'crossentropy': 3.099714994430542})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.59375, 'crossentropy': 2.999976873397827})
store['active_learning_steps'][2]['training']['best_epoch']=5
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.5739, 'crossentropy': 3.0027685546875}
store['active_learning_steps'][2]['acquisition']={'indices': [['id', 9440], ['id', 22937], ['id', 39272], ['id', 6846], ['id', 7511]], 'labels': [[0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.9449095624482722, 1.7587661295623707, 2.493131513879046, 3.0843481612666164, 3.5509518343553044]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.5830078125, 'crossentropy': 1.5444414615631104})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.59765625, 'crossentropy': 2.2719879150390625})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.57421875, 'crossentropy': 2.514177083969116})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.58984375, 'crossentropy': 3.017186164855957})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.59375, 'crossentropy': 2.7805614471435547})
store['active_learning_steps'][3]['training']['best_epoch']=2
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.5727, 'crossentropy': 2.3614369140625}
store['active_learning_steps'][3]['acquisition']={'indices': [['id', 54785], ['id', 32330], ['id', 33574], ['id', 55809], ['id', 24172]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.9003725420744124, 1.6143382884581707, 2.222431840882215, 2.7364124421283753, 3.147037379005706]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.5869140625, 'crossentropy': 1.5674470663070679})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.599609375, 'crossentropy': 2.2252721786499023})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.59765625, 'crossentropy': 2.4999070167541504})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 2.3352787494659424})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.59765625, 'crossentropy': 2.762303590774536})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.603515625, 'crossentropy': 2.6788458824157715})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 2.940640449523926})
store['active_learning_steps'][4]['training']['best_epoch']=4
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.5893, 'crossentropy': 2.6179458984375}
store['active_learning_steps'][4]['acquisition']={'indices': [['id', 54405], ['id', 23444], ['id', 55019], ['id', 28787], ['id', 28039]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.8320653406076408, 1.6060719582036893, 2.2930827333129047, 2.8680988849284867, 3.3190291209125133]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 1.506223440170288})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 2.1899893283843994})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 2.316699504852295})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 2.4882984161376953})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 2.576122760772705})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 2.5908117294311523})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 3.1820180416107178})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 2.7888550758361816})
store['active_learning_steps'][5]['training']['best_epoch']=5
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.6053, 'crossentropy': 2.821056640625}
store['active_learning_steps'][5]['acquisition']={'indices': [['id', 22069], ['id', 52549], ['id', 49939], ['id', 53745], ['id', 4645]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.8546077710571349, 1.6595184805125882, 2.313884148542037, 2.863828238565869, 3.3209887658480355]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 1.389098882675171})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 1.8056328296661377})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 2.0550241470336914})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 1.992751955986023})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 2.299682140350342})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 2.48299503326416})
store['active_learning_steps'][6]['training']['best_epoch']=3
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.6144, 'crossentropy': 2.2066724609375}
store['active_learning_steps'][6]['acquisition']={'indices': [['id', 17312], ['id', 40160], ['id', 70], ['id', 38438], ['id', 49130]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.9218055055165113, 1.7408369887954263, 2.4453197878659507, 2.98321236369895, 3.407615877586718]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.5732421875, 'crossentropy': 1.6305063962936401})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.5947265625, 'crossentropy': 1.8436076641082764})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 2.214986801147461})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 2.2595386505126953})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 2.500493049621582})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 2.6117472648620605})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 2.653733730316162})
store['active_learning_steps'][7]['training']['best_epoch']=4
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.6019, 'crossentropy': 2.4480455078125}
store['active_learning_steps'][7]['acquisition']={'indices': [['id', 28871], ['id', 57213], ['id', 32498], ['id', 29765], ['id', 25243]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.824396014725133, 1.5525081014037694, 2.227559064355372, 2.7900012542334576, 3.244154310657187]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 1.554520606994629})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 1.5445210933685303})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 1.8981302976608276})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 1.8978577852249146})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 2.2866873741149902})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 2.089313268661499})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 2.2187259197235107})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 2.2350821495056152})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 2.43441104888916})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 2.3103537559509277})
store['active_learning_steps'][8]['training']['best_epoch']=7
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.6343, 'crossentropy': 2.276273046875}
store['active_learning_steps'][8]['acquisition']={'indices': [['id', 33141], ['id', 34530], ['id', 41166], ['id', 20624], ['id', 801]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [1.0213426054829844, 1.854139236330905, 2.580173815423203, 3.1691066976967317, 3.61043754236384]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 1.3822226524353027})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 1.6911488771438599})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 1.7549042701721191})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 2.1668784618377686})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 2.0994067192077637})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 2.1536412239074707})
store['active_learning_steps'][9]['training']['best_epoch']=3
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.6211, 'crossentropy': 1.91737109375}
store['active_learning_steps'][9]['acquisition']={'indices': [['id', 36416], ['id', 12701], ['id', 46618], ['id', 29443], ['id', 39750]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.8803166671832288, 1.660960000230749, 2.3817123178269677, 2.9732520979227175, 3.424903178441027]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 1.4029099941253662})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 1.6609876155853271})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 1.740950107574463})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 1.6509461402893066})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 2.028571844100952})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 2.283048629760742})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 2.169039726257324})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 2.073153018951416})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 2.4845316410064697})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 2.4099647998809814})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 2.5798592567443848})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 2.3553805351257324})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 2.517591953277588})
store['active_learning_steps'][10]['training']['best_epoch']=10
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.6585, 'crossentropy': 2.3753240234375}
store['active_learning_steps'][10]['acquisition']={'indices': [['id', 47152], ['id', 37623], ['id', 25255], ['id', 14442], ['id', 25963]], 'labels': [[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [1.0011738618482382, 1.9336707800886828, 2.740489768789004, 3.3890555773834965, 3.8588953230693193]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 1.3949332237243652})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 1.390376329421997})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 1.6539747714996338})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 1.761803150177002})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 1.8630504608154297})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 1.8626244068145752})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 1.8386023044586182})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 2.18361234664917})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 2.004739284515381})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 2.378335475921631})
store['active_learning_steps'][11]['training']['best_epoch']=7
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.6718, 'crossentropy': 1.86280625}
store['active_learning_steps'][11]['acquisition']={'indices': [['id', 10305], ['id', 56753], ['id', 56348], ['id', 31517], ['id', 1862]], 'labels': [[0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.9985467770911549, 1.8436440823970477, 2.598514177082084, 3.202099279466979, 3.6546331620003834]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 1.2985749244689941})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 1.266019582748413})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 1.4224591255187988})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 1.5885250568389893})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 1.717991828918457})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 1.8708302974700928})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 1.8793214559555054})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 1.833020806312561})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 1.9183963537216187})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 2.0235090255737305})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 2.1326701641082764})
store['active_learning_steps'][12]['training']['best_epoch']=8
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.6711, 'crossentropy': 1.950088671875}
store['active_learning_steps'][12]['acquisition']={'indices': [['id', 41912], ['id', 58915], ['id', 27863], ['id', 46083], ['id', 44492]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.9596249661052656, 1.8117666164418678, 2.5674864040036436, 3.1749443908216843, 3.649401477495008]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.595703125, 'crossentropy': 1.3024520874023438})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 1.2558975219726562})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 1.3942933082580566})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 1.490772008895874})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 1.68381667137146})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 1.8471555709838867})
store['active_learning_steps'][13]['training']['best_epoch']=3
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.6887, 'crossentropy': 1.41642099609375}
store['active_learning_steps'][13]['acquisition']={'indices': [['id', 51231], ['id', 10052], ['id', 19291], ['id', 40095], ['id', 38100]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.7935388075039169, 1.469066278122825, 2.0689009248138355, 2.5925465047818737, 3.040468025416894]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.5810546875, 'crossentropy': 1.453622579574585})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 1.19635808467865})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 1.3865612745285034})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 1.5107784271240234})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 1.6848533153533936})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 1.8655719757080078})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 1.9198265075683594})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 1.8776061534881592})
store['active_learning_steps'][14]['training']['best_epoch']=5
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.6864, 'crossentropy': 1.701840625}
store['active_learning_steps'][14]['acquisition']={'indices': [['id', 57132], ['id', 48321], ['id', 58716], ['id', 7844], ['id', 17463]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.8750150948273445, 1.7051239941035994, 2.4372201529219097, 3.0263414313324404, 3.497412646939912]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 1.3244043588638306})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 1.1712911128997803})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 1.2818907499313354})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 1.5566959381103516})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 1.6049046516418457})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 1.786369800567627})
store['active_learning_steps'][15]['training']['best_epoch']=3
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.6951, 'crossentropy': 1.2950701171875}
store['active_learning_steps'][15]['acquisition']={'indices': [['id', 4752], ['id', 45660], ['id', 23690], ['id', 13195], ['id', 3457]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.643954992108954, 1.2589459638376375, 1.838423155729739, 2.355244384616465, 2.800760922272727]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 1.3953381776809692})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 1.2109822034835815})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 1.3416997194290161})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 1.4715139865875244})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 1.4619742631912231})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 1.8538861274719238})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 1.8523744344711304})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 1.7583351135253906})
store['active_learning_steps'][16]['training']['best_epoch']=5
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.7003, 'crossentropy': 1.4795166015625}
store['active_learning_steps'][16]['acquisition']={'indices': [['id', 23930], ['id', 13608], ['id', 13862], ['id', 7], ['id', 3379]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.7669002328894932, 1.4850942038185533, 2.134936515739848, 2.6982716629093826, 3.1592366488119037]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 1.2459282875061035})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 1.1724774837493896})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 1.4562478065490723})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 1.4128432273864746})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 1.7187403440475464})
store['active_learning_steps'][17]['training']['best_epoch']=2
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.6851, 'crossentropy': 1.2804568359375}
store['active_learning_steps'][17]['acquisition']={'indices': [['id', 52331], ['id', 14591], ['id', 10211], ['id', 29183], ['id', 5893]], 'labels': [[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.6789695565595559, 1.2609342092674636, 1.7737174862306713, 2.2263074274340697, 2.6300755758184824]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 1.3761067390441895})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 1.0976231098175049})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 1.186279535293579})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 1.294632077217102})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.716796875, 'crossentropy': 1.3565595149993896})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 1.4942899942398071})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 1.690915584564209})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 1.5886411666870117})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 1.7627832889556885})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 1.8532600402832031})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.71484375, 'crossentropy': 1.7030787467956543})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 1.9526275396347046})
store['active_learning_steps'][18]['training']['best_epoch']=9
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.716, 'crossentropy': 1.7672765625}
store['active_learning_steps'][18]['acquisition']={'indices': [['id', 5643], ['id', 19225], ['id', 5708], ['id', 49152], ['id', 47983]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.8452254501666168, 1.626862452020105, 2.359088877051641, 2.9846155852690313, 3.4874625753413877]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 1.3990027904510498})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 1.1501753330230713})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 1.1807169914245605})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.71484375, 'crossentropy': 1.3395354747772217})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 1.4482394456863403})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.72265625, 'crossentropy': 1.4135737419128418})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 1.7270383834838867})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 1.8450976610183716})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 1.7797800302505493})
store['active_learning_steps'][19]['training']['best_epoch']=6
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.708, 'crossentropy': 1.50053193359375}
store['active_learning_steps'][19]['acquisition']={'indices': [['id', 50158], ['id', 59721], ['id', 16858], ['id', 18307], ['id', 59771]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.8119348583654296, 1.5472546054427392, 2.2014932002532044, 2.7651211810769905, 3.2416884861449837]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 1.33817458152771})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 1.1067758798599243})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 1.1377358436584473})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 1.2380759716033936})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 1.487424373626709})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 1.4594202041625977})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.716796875, 'crossentropy': 1.657263994216919})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 1.4886913299560547})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 1.6009342670440674})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 1.912243366241455})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 1.6373603343963623})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.7236328125, 'crossentropy': 1.6961469650268555})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 1.8402565717697144})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 1.8717635869979858})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 1.7406225204467773})
store['active_learning_steps'][20]['training']['best_epoch']=12
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.7192, 'crossentropy': 1.780255078125}
store['active_learning_steps'][20]['acquisition']={'indices': [['id', 25800], ['id', 34817], ['id', 34739], ['id', 22163], ['id', 37921]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.8630882240741937, 1.6678881468562707, 2.410059163846551, 3.051554085126904, 3.559348541240138]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 1.3006020784378052})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 1.0842187404632568})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.1488535404205322})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 1.2478878498077393})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 1.4094653129577637})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 1.3992242813110352})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 1.5336837768554688})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 1.7033402919769287})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 1.6603976488113403})
store['active_learning_steps'][21]['training']['best_epoch']=6
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.7035, 'crossentropy': 1.48388515625}
store['active_learning_steps'][21]['acquisition']={'indices': [['id', 32065], ['id', 36872], ['id', 44654], ['id', 54147], ['id', 4915]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.8116251570847051, 1.5789009048228175, 2.2526131533469496, 2.8301027471690112, 3.287303183867568]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 1.393006443977356})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 1.0866320133209229})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 1.2068188190460205})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 1.2520450353622437})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 1.2905404567718506})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 1.4995452165603638})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 1.6030168533325195})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.71484375, 'crossentropy': 1.5579454898834229})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 1.621342658996582})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 1.8291915655136108})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.712890625, 'crossentropy': 1.8175044059753418})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 1.6371996402740479})
store['active_learning_steps'][22]['training']['best_epoch']=9
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.7178, 'crossentropy': 1.690994140625}
store['active_learning_steps'][22]['acquisition']={'indices': [['id', 15622], ['id', 931], ['id', 44743], ['id', 21103], ['id', 31229]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [1.0280457777961374, 1.8859357817715376, 2.617319035904435, 3.240759224787568, 3.7005805617159364]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 1.3594163656234741})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 1.10672926902771})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 1.1526858806610107})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 1.2255336046218872})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 1.3402941226959229})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 1.4694777727127075})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 1.3801183700561523})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 1.5116469860076904})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 1.6052261590957642})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.712890625, 'crossentropy': 1.7145373821258545})
store['active_learning_steps'][23]['training']['best_epoch']=7
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.7212, 'crossentropy': 1.43956533203125}
store['active_learning_steps'][23]['acquisition']={'indices': [['id', 125], ['id', 54641], ['id', 10438], ['id', 57827], ['id', 43139]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.8866080503808818, 1.6965917641728727, 2.4121207017234676, 2.9754180988322974, 3.4113290883789684]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 1.2678738832473755})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 1.0709116458892822})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 1.061100959777832})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.7265625, 'crossentropy': 1.2183654308319092})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.7265625, 'crossentropy': 1.2632291316986084})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 1.3373191356658936})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.724609375, 'crossentropy': 1.5965938568115234})
store['active_learning_steps'][24]['training']['best_epoch']=4
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.7186, 'crossentropy': 1.20978115234375}
store['active_learning_steps'][24]['acquisition']={'indices': [['id', 13384], ['id', 3410], ['id', 2800], ['id', 5111], ['id', 24661]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.7854535796231568, 1.4689069541616986, 2.0590701222090626, 2.5775380157816015, 3.0175733614854696]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 1.4471371173858643})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 1.0859370231628418})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 1.1175508499145508})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 1.201871395111084})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 1.2639272212982178})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 1.3088014125823975})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 1.3648943901062012})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 1.4222283363342285})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 1.6305582523345947})
store['active_learning_steps'][25]['training']['best_epoch']=6
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.7067, 'crossentropy': 1.4332455078125}
store['active_learning_steps'][25]['acquisition']={'indices': [['id', 34402], ['id', 22016], ['id', 34547], ['id', 10736], ['id', 13257]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.7847283087943491, 1.5216882593302374, 2.1894108927277394, 2.7719548762862187, 3.236889114040186]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 1.310105323791504})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 1.1492302417755127})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 1.0880035161972046})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.724609375, 'crossentropy': 1.208481788635254})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.724609375, 'crossentropy': 1.2762998342514038})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 1.3795628547668457})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.732421875, 'crossentropy': 1.3829052448272705})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.7216796875, 'crossentropy': 1.5787684917449951})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.7216796875, 'crossentropy': 1.5843886137008667})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.72265625, 'crossentropy': 1.6045204401016235})
store['active_learning_steps'][26]['training']['best_epoch']=7
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.7289, 'crossentropy': 1.4088890625}
store['active_learning_steps'][26]['acquisition']={'indices': [['id', 13320], ['id', 44606], ['id', 37457], ['id', 59731], ['id', 1882]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.9369563027307741, 1.7259640697082177, 2.462178509928725, 3.046477029018673, 3.499984633630006]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 1.2895245552062988})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 1.0886863470077515})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 1.1595404148101807})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.7216796875, 'crossentropy': 1.1229422092437744})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.72265625, 'crossentropy': 1.1861202716827393})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.72265625, 'crossentropy': 1.3815219402313232})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 1.3975245952606201})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.724609375, 'crossentropy': 1.4620293378829956})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 1.5279021263122559})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.7216796875, 'crossentropy': 1.538016676902771})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.72265625, 'crossentropy': 1.6707074642181396})
store['active_learning_steps'][27]['training']['best_epoch']=8
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.7104, 'crossentropy': 1.5209490234375}
store['active_learning_steps'][27]['acquisition']={'indices': [['id', 13903], ['id', 41355], ['id', 12073], ['id', 38974], ['id', 51071]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.0768245312847187, 1.9411415606654092, 2.6755494741254076, 3.2868691682143503, 3.716735920739316]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.5576171875, 'crossentropy': 1.495567798614502})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 1.1385459899902344})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 1.0813679695129395})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 1.1161396503448486})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 1.2588694095611572})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.71484375, 'crossentropy': 1.3944847583770752})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.716796875, 'crossentropy': 1.347154974937439})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.7236328125, 'crossentropy': 1.451413869857788})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.712890625, 'crossentropy': 1.4117395877838135})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.7265625, 'crossentropy': 1.6091177463531494})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 1.6406245231628418})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.716796875, 'crossentropy': 1.6175363063812256})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.73046875, 'crossentropy': 1.5518553256988525})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 1.7736289501190186})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.7216796875, 'crossentropy': 1.6777164936065674})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.71484375, 'crossentropy': 1.618574857711792})
store['active_learning_steps'][28]['training']['best_epoch']=13
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.7168, 'crossentropy': 1.57096826171875}
store['active_learning_steps'][28]['acquisition']={'indices': [['id', 42917], ['id', 30290], ['id', 12580], ['id', 25420], ['id', 48210]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [1.0491956956490367, 1.9254183205542081, 2.6669413561770288, 3.2720542712761427, 3.7177255646196237]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.5859375, 'crossentropy': 1.4563161134719849})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 1.1018401384353638})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 1.1242468357086182})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 1.1168221235275269})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.724609375, 'crossentropy': 1.0903911590576172})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 1.3054168224334717})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 1.295519232749939})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.716796875, 'crossentropy': 1.4479455947875977})
store['active_learning_steps'][29]['training']['best_epoch']=5
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.7224, 'crossentropy': 1.15373818359375}
store['active_learning_steps'][29]['acquisition']={'indices': [['id', 33673], ['id', 54033], ['id', 380], ['id', 1031], ['id', 11531]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.7699756110049376, 1.4565695787931272, 2.0852609167676643, 2.6338541142620358, 3.091441670162565]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 1.4228534698486328})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 1.1860957145690918})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 1.0866196155548096})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 1.104353427886963})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.728515625, 'crossentropy': 1.2147438526153564})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 1.3452515602111816})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 1.3988590240478516})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.732421875, 'crossentropy': 1.5480968952178955})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.7255859375, 'crossentropy': 1.4019770622253418})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.736328125, 'crossentropy': 1.49812912940979})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.7265625, 'crossentropy': 1.6623071432113647})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.73046875, 'crossentropy': 1.6183137893676758})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.72265625, 'crossentropy': 1.6305360794067383})
store['active_learning_steps'][30]['training']['best_epoch']=10
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.7225, 'crossentropy': 1.658928125}
store['active_learning_steps'][30]['acquisition']={'indices': [['id', 55018], ['id', 16490], ['id', 43342], ['id', 12381], ['id', 31648]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [0.8730543335504066, 1.671518394335247, 2.384115842237688, 2.9975367450992847, 3.4790473427471245]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 1.4383329153060913})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 1.166424036026001})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 1.1845614910125732})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 1.1386566162109375})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 1.2801687717437744})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 1.3325023651123047})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 1.4091341495513916})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 1.4768798351287842})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 1.4797568321228027})
store['active_learning_steps'][31]['training']['best_epoch']=6
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.7052, 'crossentropy': 1.3692865234375}
store['active_learning_steps'][31]['acquisition']={'indices': [['id', 3951], ['id', 35305], ['id', 45010], ['id', 16361], ['id', 9572]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.8054245504517197, 1.548578963387854, 2.2232679666667092, 2.7737586852335987, 3.2291386153450725]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.591796875, 'crossentropy': 1.500753402709961})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 1.2091797590255737})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 1.089715600013733})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 1.1466354131698608})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 1.3083311319351196})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.716796875, 'crossentropy': 1.3246042728424072})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.7255859375, 'crossentropy': 1.2874150276184082})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.7314453125, 'crossentropy': 1.4433917999267578})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.72265625, 'crossentropy': 1.470198392868042})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.732421875, 'crossentropy': 1.713407278060913})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.73828125, 'crossentropy': 1.509690284729004})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.7314453125, 'crossentropy': 1.6293294429779053})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.7216796875, 'crossentropy': 1.6015942096710205})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.728515625, 'crossentropy': 1.5169867277145386})
store['active_learning_steps'][32]['training']['best_epoch']=11
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.7236, 'crossentropy': 1.6686994140625}
store['active_learning_steps'][32]['acquisition']={'indices': [['id', 59264], ['id', 33405], ['id', 22181], ['id', 2576], ['id', 36568]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.9332617607107894, 1.7693420967888787, 2.5326132939658077, 3.1704816278670265, 3.6375871156079223]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.5693359375, 'crossentropy': 1.4509528875350952})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 1.1800730228424072})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 1.1581473350524902})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 1.144869089126587})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 1.2088043689727783})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 1.2171396017074585})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.712890625, 'crossentropy': 1.2217494249343872})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 1.329453468322754})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 1.475303292274475})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 1.4994590282440186})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.732421875, 'crossentropy': 1.4535095691680908})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.7275390625, 'crossentropy': 1.6012495756149292})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.7470703125, 'crossentropy': 1.385408639907837})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 1.5298829078674316})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 1.6429376602172852})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.7314453125, 'crossentropy': 1.595665454864502})
store['active_learning_steps'][33]['training']['best_epoch']=13
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.7301, 'crossentropy': 1.479444921875}
store['active_learning_steps'][33]['acquisition']={'indices': [['id', 17574], ['id', 726], ['id', 15716], ['id', 47079], ['id', 47725]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.9517982784922929, 1.7937091278490316, 2.551713759436625, 3.1751890826029605, 3.6457234076674334]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.552734375, 'crossentropy': 1.4281840324401855})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 1.1291179656982422})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 1.0037206411361694})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.7216796875, 'crossentropy': 1.0722241401672363})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.7236328125, 'crossentropy': 1.172088623046875})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.7265625, 'crossentropy': 1.2362459897994995})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.7421875, 'crossentropy': 1.1568267345428467})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.7236328125, 'crossentropy': 1.3676689863204956})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.7353515625, 'crossentropy': 1.338715672492981})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.73828125, 'crossentropy': 1.3823105096817017})
store['active_learning_steps'][34]['training']['best_epoch']=7
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.7342, 'crossentropy': 1.24016162109375}
store['active_learning_steps'][34]['acquisition']={'indices': [['id', 26263], ['id', 57582], ['id', 34274], ['id', 22224], ['id', 28491]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.7882652058376114, 1.5243681346112847, 2.2108917734709594, 2.798409663851608, 3.2771332644662525]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.57421875, 'crossentropy': 1.5118643045425415})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 1.173084020614624})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 1.0616302490234375})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 1.1219193935394287})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.7294921875, 'crossentropy': 1.1450382471084595})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.7353515625, 'crossentropy': 1.2934620380401611})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.732421875, 'crossentropy': 1.1910185813903809})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.732421875, 'crossentropy': 1.294609546661377})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.72265625, 'crossentropy': 1.403490424156189})
store['active_learning_steps'][35]['training']['best_epoch']=6
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.7253, 'crossentropy': 1.2438625}
store['active_learning_steps'][35]['acquisition']={'indices': [['id', 18913], ['id', 16778], ['id', 22369], ['id', 25857], ['id', 31879]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.7943443287579857, 1.4786187640289468, 2.0877561697481726, 2.631293353087033, 3.0984026643321094]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 1.4114848375320435})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 1.0923314094543457})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.71484375, 'crossentropy': 1.05708646774292})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.7236328125, 'crossentropy': 1.087143898010254})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.7294921875, 'crossentropy': 1.12784743309021})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.7373046875, 'crossentropy': 1.1536412239074707})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.7353515625, 'crossentropy': 1.3256127834320068})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.740234375, 'crossentropy': 1.2883710861206055})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.7421875, 'crossentropy': 1.3512415885925293})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.736328125, 'crossentropy': 1.3487377166748047})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.73046875, 'crossentropy': 1.466769814491272})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.744140625, 'crossentropy': 1.4695429801940918})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.7421875, 'crossentropy': 1.5849556922912598})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.7333984375, 'crossentropy': 1.6338515281677246})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.7373046875, 'crossentropy': 1.6651465892791748})
store['active_learning_steps'][36]['training']['best_epoch']=12
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.7375, 'crossentropy': 1.54106484375}
