store = {}
store['timestamp']=1621483606
store['cmdline']=['/home/kell4989/git/active_learning_redux/batchbald_redux/ood_experiment.py', '--id=77']
store['commit']='8a2cf4fb40ce306533b4e439b08268c53f009a3b'
store['github_url']='8a2cf4fb40ce306533b4e439b08268c53f009a3b'
store['experiment']='/home/kell4989/git/active_learning_redux/batchbald_redux/ood_experiment.py'
store['job_id']=77
store['worker_id']=77
store['num_workers']=80
store['config']={'seed': 1315, 'uniform_ood': True, 'id_dataset_type': 'batchbald_redux.fast_mnist.FastFashionMNIST', 'ood_dataset_type': 'batchbald_redux.fast_mnist.FastMNIST', 'initial_training_set_size': 20, 'validation_set_size': 1024, 'evaluation_set_size': 256, 'id_repetitions': 1, 'ood_repetitions': 1, 'add_dataset_noise': False, 'validation_split_random_state': 0, 'acquisition_size': 5, 'max_training_set': 200, 'num_pool_samples': 100, 'num_validation_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'min_samples_per_epoch': 5056, 'acquisition_function': 'batchbald_redux.acquisition_functions.BatchBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationEvalModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 8}
store['log']={}
store['dataset_info']={'training': "(FastFashionMNIST (train; 58976 samples) | one_hot_targets{'num_classes': 10}) + ('FastMNIST Train (60000 samples)' | uniform_targets{'num_classes': 10})", 'test': "'FastFashionMNIST Test (10000 samples)'"}
store['initial_training_set_indices']=[55573, 380, 12640, 44119, 30392, 58226, 43812, 52440, 3091, 29974, 49512, 46037, 53434, 22015, 37915, 52296, 8533, 58125, 22304, 35472]
store['evaluation_set_indices']=[42890, 40646, 10110, 32775, 33736, 27254, 306, 37354, 19689, 57811, 34482, 15494, 19215, 18819, 11554, 8108, 29048, 30362, 48953, 5588, 8719, 48602, 33140, 46397, 56710, 14640, 39579, 5573, 5715, 47420, 27135, 26129, 16927, 39050, 42295, 51555, 51600, 43234, 33891, 20917, 38856, 17032, 13036, 11228, 46700, 50498, 40741, 9834, 24971, 17759, 45567, 2728, 1774, 33486, 43252, 43803, 50036, 46861, 53831, 54003, 53362, 229, 767, 36270, 10432, 23451, 6612, 8710, 41077, 48498, 46683, 45260, 37098, 55148, 49775, 52801, 15969, 57520, 36797, 34198, 27145, 3029, 37047, 31965, 26501, 48519, 5803, 43415, 35794, 33581, 5897, 27573, 30980, 29614, 35237, 51755, 57690, 26516, 5380, 25589, 53689, 31444, 29950, 44803, 396, 56990, 24052, 12108, 54426, 42320, 35072, 21536, 49304, 49595, 44428, 72, 57175, 52679, 41082, 30184, 54017, 10232, 17968, 31935, 43587, 801, 48031, 2206, 2404, 58741, 29079, 49986, 46464, 17659, 30072, 39879, 29556, 52389, 13092, 37129, 11773, 15822, 37625, 7382, 7121, 17195, 32625, 43141, 28181, 50055, 55187, 34588, 38725, 50466, 40018, 37115, 20801, 23496, 4321, 42102, 12075, 54012, 28833, 18880, 26520, 27580, 14637, 40466, 54800, 24110, 13859, 51027, 45005, 57541, 34361, 26479, 43321, 44048, 45974, 15675, 10508, 49549, 28991, 13074, 9574, 44454, 36688, 8821, 12610, 54422, 34121, 27019, 21800, 44138, 36367, 44100, 33464, 51760, 15917, 495, 50997, 48032, 40334, 21423, 46870, 18137, 4701, 18693, 17506, 6968, 13359, 35372, 7356, 2289, 55733, 5481, 37157, 56054, 2400, 56137, 1005, 56096, 53538, 55783, 37709, 3792, 10664, 5616, 32972, 30013, 19757, 49169, 47417, 38430, 41512, 14035, 35714, 16068, 20076, 26853, 26428, 48521, 11261, 12917, 257, 43981, 8705, 27383, 10113, 7896]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 2.4243111610412598})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 2.9108471870422363})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 3.212575912475586})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 3.035694122314453})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 3.24114990234375})
store['active_learning_steps'][0]['training']['best_epoch']=2
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.5995, 'crossentropy': 3.0993529296875}
store['active_learning_steps'][0]['acquisition']={'indices': [['id', 45137], ['id', 14335], ['id', 35930], ['id', 36197], ['id', 14536]], 'labels': [[0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [1.5119904186856057, 2.6661903082477743, 3.4969703574609072, 4.021692520135707, 4.315063524967554]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.5654296875, 'crossentropy': 2.1117782592773438})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.5947265625, 'crossentropy': 2.6497912406921387})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.5830078125, 'crossentropy': 3.2768707275390625})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.591796875, 'crossentropy': 3.347158908843994})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.5849609375, 'crossentropy': 3.303954839706421})
store['active_learning_steps'][1]['training']['best_epoch']=2
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.5797, 'crossentropy': 2.7253853515625}
store['active_learning_steps'][1]['acquisition']={'indices': [['id', 31627], ['id', 22546], ['id', 46139], ['id', 13317], ['id', 17728]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.9699574995324824, 1.7621756145625476, 2.436946868392873, 2.98438440176095, 3.4177904066217693]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.5966796875, 'crossentropy': 1.7536141872406006})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 2.5967519283294678})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.595703125, 'crossentropy': 2.9869022369384766})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.59765625, 'crossentropy': 2.8371682167053223})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 2.893153190612793})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 3.024059534072876})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.5986328125, 'crossentropy': 3.417987823486328})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 3.1475043296813965})
store['active_learning_steps'][2]['training']['best_epoch']=5
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.5886, 'crossentropy': 3.0010666015625}
store['active_learning_steps'][2]['acquisition']={'indices': [['id', 35309], ['id', 12270], ['id', 41036], ['id', 25420], ['id', 51688]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.798904784866121, 1.5525070262129423, 2.2457571204302846, 2.8074923632266877, 3.2698859731442145]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.5859375, 'crossentropy': 1.626648187637329})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 2.240062713623047})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.603515625, 'crossentropy': 2.568734645843506})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 2.8347625732421875})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 2.7294440269470215})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 2.9580001831054688})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 3.479408025741577})
store['active_learning_steps'][3]['training']['best_epoch']=4
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.5994, 'crossentropy': 2.8179017578125}
store['active_learning_steps'][3]['acquisition']={'indices': [['id', 27435], ['id', 53796], ['id', 13137], ['id', 22937], ['id', 6844]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.8772540052227622, 1.6952920692928823, 2.3744115472925422, 2.9580694229866467, 3.4297967258123583]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6005859375, 'crossentropy': 1.5872840881347656})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 2.122917652130127})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 2.363638401031494})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 2.8964643478393555})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 3.1858038902282715})
store['active_learning_steps'][4]['training']['best_epoch']=2
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.6081, 'crossentropy': 2.221471484375}
store['active_learning_steps'][4]['acquisition']={'indices': [['id', 34994], ['id', 4068], ['id', 36445], ['id', 18307], ['id', 57976]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.7431915800937414, 1.4095986416044304, 2.005947201267489, 2.543694843095464, 2.9963491113740943]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.583984375, 'crossentropy': 1.4779064655303955})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 1.7322406768798828})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 1.9851893186569214})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 2.0547385215759277})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 2.1342530250549316})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 2.1138219833374023})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 2.4965176582336426})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 2.613837480545044})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 2.468320846557617})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 2.4040231704711914})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 2.621904134750366})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 2.55808162689209})
store['active_learning_steps'][5]['training']['best_epoch']=9
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.6288, 'crossentropy': 2.7270595703125}
store['active_learning_steps'][5]['acquisition']={'indices': [['id', 18486], ['id', 54737], ['id', 33703], ['id', 3457], ['id', 54813]], 'labels': [[0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [1.1811470479211557, 2.1967992654096595, 3.073173334082144, 3.663552152776777, 4.058491333747796]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 1.4644962549209595})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 1.6549384593963623})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 2.168062686920166})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 2.379878282546997})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 2.4102747440338135})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 2.591134548187256})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 2.4775919914245605})
store['active_learning_steps'][6]['training']['best_epoch']=4
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.6231, 'crossentropy': 2.4164576171875}
store['active_learning_steps'][6]['acquisition']={'indices': [['id', 41355], ['id', 4935], ['id', 32110], ['id', 13995], ['id', 7303]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.9514314792725227, 1.8341676769597983, 2.612665304439763, 3.2361283623559594, 3.6811733926932924]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.5361328125, 'crossentropy': 1.5359660387039185})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 1.7033038139343262})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 1.9693493843078613})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 2.4081268310546875})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 2.444068431854248})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 2.3935375213623047})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 2.8588266372680664})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 2.691495895385742})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 3.190492630004883})
store['active_learning_steps'][7]['training']['best_epoch']=6
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.6347, 'crossentropy': 2.6348017578125}
store['active_learning_steps'][7]['acquisition']={'indices': [['id', 27409], ['id', 37829], ['id', 47112], ['id', 29088], ['id', 16530]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [1.002857596926059, 1.9201276352925483, 2.667237844568227, 3.2437563766852673, 3.661078376469221]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.5634765625, 'crossentropy': 1.477048635482788})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 1.461188793182373})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 1.864575982093811})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 2.1387312412261963})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 2.346318006515503})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 2.467222213745117})
store['active_learning_steps'][8]['training']['best_epoch']=3
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.6172, 'crossentropy': 2.058010546875}
store['active_learning_steps'][8]['acquisition']={'indices': [['id', 47164], ['id', 11094], ['id', 3932], ['id', 19756], ['id', 48113]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.8269080197840548, 1.5616497915852836, 2.2010826923927302, 2.7536660625908187, 3.1978728444364464]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.5673828125, 'crossentropy': 1.4028899669647217})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 1.6478888988494873})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 1.8135058879852295})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 2.2180142402648926})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 2.3412094116210938})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 2.208911895751953})
store['active_learning_steps'][9]['training']['best_epoch']=3
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.6261, 'crossentropy': 1.8286310546875}
store['active_learning_steps'][9]['acquisition']={'indices': [['id', 16154], ['id', 56561], ['id', 47664], ['id', 55765], ['id', 36568]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.7802680371486397, 1.5221937643231964, 2.135050023607384, 2.679695770676677, 3.1360476020289774]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.583984375, 'crossentropy': 1.4545834064483643})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 1.679412841796875})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 1.9411770105361938})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 2.3067779541015625})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 2.507005214691162})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 2.580108880996704})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 2.817473888397217})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 3.1436784267425537})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 2.8011794090270996})
store['active_learning_steps'][10]['training']['best_epoch']=6
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.637, 'crossentropy': 2.885815234375}
store['active_learning_steps'][10]['acquisition']={'indices': [['id', 13031], ['id', 33405], ['id', 35684], ['id', 39750], ['id', 4091]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.8639767173863673, 1.7087430378062942, 2.433130197260491, 3.058961084398643, 3.5234949677409677]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.580078125, 'crossentropy': 1.4200587272644043})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.5986328125, 'crossentropy': 1.5743106603622437})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 1.9673161506652832})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 2.193282127380371})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 2.3817062377929688})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 2.428162097930908})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 2.9292612075805664})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 3.038313388824463})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 2.8256893157958984})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 3.044034719467163})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 3.155463218688965})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 3.1941399574279785})
store['active_learning_steps'][11]['training']['best_epoch']=9
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.6422, 'crossentropy': 3.0322009765625}
store['active_learning_steps'][11]['acquisition']={'indices': [['id', 54405], ['id', 25963], ['id', 30201], ['id', 59860], ['id', 59177]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.9781030475740313, 1.7943055419709957, 2.5276733884915323, 3.141193869141979, 3.6097537055580924]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.541015625, 'crossentropy': 1.4766011238098145})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 1.4741826057434082})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 1.806815505027771})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 1.8882009983062744})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 2.434833526611328})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 2.316744327545166})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 2.4923999309539795})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 2.820761203765869})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 2.7632503509521484})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 2.5455312728881836})
store['active_learning_steps'][12]['training']['best_epoch']=7
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.6316, 'crossentropy': 2.797428125}
store['active_learning_steps'][12]['acquisition']={'indices': [['id', 22069], ['id', 33875], ['id', 44676], ['id', 23295], ['id', 33111]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.9482825631592138, 1.7983288589682163, 2.538471347706655, 3.1651087848755033, 3.6334932462307625]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.58984375, 'crossentropy': 1.3883813619613647})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 1.4203784465789795})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 1.482151746749878})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 1.9192478656768799})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 2.0528383255004883})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 2.0582966804504395})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 2.480095863342285})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 2.826202392578125})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 2.731832981109619})
store['active_learning_steps'][13]['training']['best_epoch']=6
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.6224, 'crossentropy': 2.268911328125}
store['active_learning_steps'][13]['acquisition']={'indices': [['id', 43346], ['id', 25324], ['id', 48763], ['id', 29755], ['id', 1033]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.8952711966315448, 1.690552029012094, 2.4035406394134666, 2.984539212490243, 3.458592717715546]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.5869140625, 'crossentropy': 1.4368481636047363})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 1.5047199726104736})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 1.7318062782287598})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 2.2016441822052})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 2.491067409515381})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 2.198971748352051})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 2.4951467514038086})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 2.76119065284729})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 3.0971508026123047})
store['active_learning_steps'][14]['training']['best_epoch']=6
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.6249, 'crossentropy': 2.64433828125}
store['active_learning_steps'][14]['acquisition']={'indices': [['id', 53338], ['id', 30767], ['id', 52150], ['id', 33381], ['id', 59312]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.8791830888959367, 1.6495272288818477, 2.3563151221738767, 2.952819948641711, 3.438445043837567]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.578125, 'crossentropy': 1.4810669422149658})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 1.5266735553741455})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 1.7523465156555176})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 2.325404167175293})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 2.1900722980499268})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 2.2544946670532227})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 2.251251459121704})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 2.4779109954833984})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 2.7672793865203857})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 2.7413458824157715})
store['active_learning_steps'][15]['training']['best_epoch']=7
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.6416, 'crossentropy': 2.4076318359375}
store['active_learning_steps'][15]['acquisition']={'indices': [['id', 44685], ['id', 28546], ['id', 58339], ['id', 39395], ['id', 26132]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.9031834889120993, 1.7293168231362652, 2.4456043483022922, 3.022516098750339, 3.4870742234129697]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 1.3581035137176514})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 1.304322361946106})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 1.45027494430542})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 1.5409544706344604})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 1.9596385955810547})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 2.0198469161987305})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 2.1833066940307617})
store['active_learning_steps'][16]['training']['best_epoch']=4
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.6657, 'crossentropy': 1.7263693359375}
store['active_learning_steps'][16]['acquisition']={'indices': [['id', 10567], ['id', 20009], ['id', 51163], ['id', 49224], ['id', 55098]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.7861028908243721, 1.52464079128338, 2.2077985411761425, 2.786667436788216, 3.2499797365236107]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 1.3000069856643677})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 1.2449405193328857})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 1.3502814769744873})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 1.6201841831207275})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 1.9528871774673462})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 1.8935556411743164})
store['active_learning_steps'][17]['training']['best_epoch']=3
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.6504, 'crossentropy': 1.44849111328125}
store['active_learning_steps'][17]['acquisition']={'indices': [['id', 26636], ['id', 51952], ['id', 1674], ['id', 13611], ['id', 20946]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.7864900007267861, 1.4094319151273345, 1.9827016453175013, 2.5036982609458045, 2.945924247712277]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.587890625, 'crossentropy': 1.39154052734375})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 1.1837329864501953})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 1.2879650592803955})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 1.4684441089630127})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 1.5046333074569702})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 1.5556650161743164})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 1.695302963256836})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 1.8046233654022217})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 2.098179578781128})
store['active_learning_steps'][18]['training']['best_epoch']=6
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.6818, 'crossentropy': 1.59814453125}
store['active_learning_steps'][18]['acquisition']={'indices': [['id', 25184], ['id', 53488], ['id', 3895], ['id', 53914], ['id', 55037]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.8599937210341138, 1.6134988799420262, 2.3223738305059882, 2.8999605418003647, 3.3665212774954085]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.5556640625, 'crossentropy': 1.452284812927246})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 1.2773637771606445})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 1.4667713642120361})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 1.5970637798309326})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 1.7944575548171997})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 1.9263856410980225})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.928128719329834})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 2.131895065307617})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 2.521416187286377})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 2.4585490226745605})
store['active_learning_steps'][19]['training']['best_epoch']=7
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.6579, 'crossentropy': 2.07313515625}
store['active_learning_steps'][19]['acquisition']={'indices': [['id', 37489], ['id', 7755], ['id', 5918], ['id', 1031], ['id', 51869]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.8711867481993418, 1.6894669397807354, 2.4237813432745074, 3.026025410844351, 3.499488256542441]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 1.382500410079956})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 1.2613790035247803})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 1.4415907859802246})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 1.6545305252075195})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 1.617232084274292})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 1.8349261283874512})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 2.0703635215759277})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 2.048433780670166})
store['active_learning_steps'][20]['training']['best_epoch']=5
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.6673, 'crossentropy': 1.8012001953125}
store['active_learning_steps'][20]['acquisition']={'indices': [['id', 57213], ['id', 31557], ['id', 20011], ['id', 40160], ['id', 56440]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.7767083847629412, 1.5128725342125047, 2.15487441371231, 2.702412231665866, 3.157254544849602]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.52734375, 'crossentropy': 1.4924304485321045})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 1.1645050048828125})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 1.2613470554351807})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 1.3277685642242432})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 1.3514108657836914})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 1.6437852382659912})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 1.9550464153289795})
store['active_learning_steps'][21]['training']['best_epoch']=4
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.6776, 'crossentropy': 1.46151767578125}
store['active_learning_steps'][21]['acquisition']={'indices': [['id', 21204], ['id', 59671], ['id', 987], ['id', 31654], ['id', 41333]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6629850298412343, 1.2994690908775572, 1.8997896845846292, 2.4227824223676215, 2.8747509526478474]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.5419921875, 'crossentropy': 1.4446730613708496})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 1.1512787342071533})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 1.1729027032852173})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 1.3564943075180054})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 1.326524257659912})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 1.5233995914459229})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 1.5541565418243408})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 1.7620106935501099})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 1.6165893077850342})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 1.8392599821090698})
store['active_learning_steps'][22]['training']['best_epoch']=7
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.7006, 'crossentropy': 1.64416484375}
store['active_learning_steps'][22]['acquisition']={'indices': [['id', 70], ['id', 46547], ['id', 26785], ['id', 54827], ['id', 18913]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.1002817754713972, 1.9765499402325304, 2.7385537871690193, 3.30806019791276, 3.7215487747546927]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.5771484375, 'crossentropy': 1.3625373840332031})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 1.201631784439087})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 1.2900586128234863})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 1.2349252700805664})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 1.3798308372497559})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 1.380284309387207})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.712890625, 'crossentropy': 1.5713664293289185})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 1.6875364780426025})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 1.6432504653930664})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 1.9587138891220093})
store['active_learning_steps'][23]['training']['best_epoch']=7
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.7003, 'crossentropy': 1.64428828125}
store['active_learning_steps'][23]['acquisition']={'indices': [['id', 13499], ['id', 17030], ['id', 49152], ['id', 59731], ['id', 59091]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.9120788691784578, 1.7546323904822083, 2.453498084459267, 3.0489141198889556, 3.5160231549793117]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.591796875, 'crossentropy': 1.3327147960662842})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 1.1769609451293945})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 1.137499213218689})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.71484375, 'crossentropy': 1.0825581550598145})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 1.2420175075531006})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 1.5024151802062988})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 1.5720926523208618})
store['active_learning_steps'][24]['training']['best_epoch']=4
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.7054, 'crossentropy': 1.1495623046875}
store['active_learning_steps'][24]['acquisition']={'indices': [['id', 31662], ['id', 32351], ['id', 2972], ['id', 43543], ['id', 13598]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6516830663658286, 1.2669691340511564, 1.8268233217105676, 2.327472463653912, 2.776106797936194]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.5537109375, 'crossentropy': 1.4970436096191406})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 1.188555121421814})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 1.1735906600952148})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 1.2103170156478882})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 1.3046197891235352})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 1.4877946376800537})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 1.5270459651947021})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 1.6090848445892334})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 1.7701077461242676})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 1.7524714469909668})
store['active_learning_steps'][25]['training']['best_epoch']=7
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.6997, 'crossentropy': 1.560330859375}
store['active_learning_steps'][25]['acquisition']={'indices': [['id', 49891], ['id', 30162], ['id', 20624], ['id', 37650], ['id', 39951]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.8884032586675465, 1.6792533604554354, 2.3865228970794057, 2.965499496306361, 3.443170399803412]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.5166015625, 'crossentropy': 1.4127863645553589})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 1.1249110698699951})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.0835542678833008})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 1.3124313354492188})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 1.2942380905151367})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 1.5731775760650635})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 1.647690773010254})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 1.6691322326660156})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 1.731734037399292})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 1.5764306783676147})
store['active_learning_steps'][26]['training']['best_epoch']=7
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.689, 'crossentropy': 1.6582400390625}
store['active_learning_steps'][26]['acquisition']={'indices': [['id', 29183], ['id', 13237], ['id', 30098], ['id', 47851], ['id', 19268]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.883616982376283, 1.7199080372211766, 2.453621404343269, 3.062866157677121, 3.527550645856639]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.5634765625, 'crossentropy': 1.405605435371399})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 1.1403261423110962})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 1.0832905769348145})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 1.1254066228866577})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 1.3593907356262207})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.4340786933898926})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 1.5297293663024902})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 1.4987350702285767})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 1.6307505369186401})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 1.7148979902267456})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 1.5924310684204102})
store['active_learning_steps'][27]['training']['best_epoch']=8
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.6926, 'crossentropy': 1.5318126953125}
store['active_learning_steps'][27]['acquisition']={'indices': [['id', 5355], ['id', 28962], ['id', 40189], ['id', 49995], ['id', 38782]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.8902772513007235, 1.7499448436509644, 2.461420521896816, 3.012049710910925, 3.4537625091362765]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 1.3780910968780518})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 1.132387399673462})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 1.2241480350494385})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 1.2523090839385986})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 1.3347550630569458})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 1.3784854412078857})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 1.618506908416748})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 1.5336151123046875})
store['active_learning_steps'][28]['training']['best_epoch']=5
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.6887, 'crossentropy': 1.3305828125}
store['active_learning_steps'][28]['acquisition']={'indices': [['id', 6893], ['id', 17312], ['id', 44521], ['id', 21487], ['id', 2731]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.8098162862405289, 1.5440225364316182, 2.228931922765762, 2.825029132454924, 3.2828534177550477]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.5146484375, 'crossentropy': 1.4529573917388916})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 1.159335732460022})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 1.1402190923690796})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.1298003196716309})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 1.1507973670959473})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.716796875, 'crossentropy': 1.3078508377075195})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 1.2921391725540161})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 1.3966546058654785})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 1.51337468624115})
store['active_learning_steps'][29]['training']['best_epoch']=6
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.7018, 'crossentropy': 1.37356826171875}
store['active_learning_steps'][29]['acquisition']={'indices': [['id', 48480], ['id', 35305], ['id', 44410], ['id', 38806], ['id', 47903]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.778805455650762, 1.4964134954538348, 2.120126726275454, 2.662914286314141, 3.123259963379013]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.4931640625, 'crossentropy': 1.5584237575531006})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 1.2226266860961914})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 1.1084041595458984})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 1.0732407569885254})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 1.2080767154693604})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 1.3178839683532715})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 1.341674566268921})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.716796875, 'crossentropy': 1.381356954574585})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 1.4694387912750244})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 1.5153921842575073})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 1.5277092456817627})
store['active_learning_steps'][30]['training']['best_epoch']=8
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.7101, 'crossentropy': 1.366073046875}
store['active_learning_steps'][30]['acquisition']={'indices': [['id', 33141], ['id', 380], ['id', 3009], ['id', 44144], ['id', 10052]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [1.0224076732360872, 1.8438413604165782, 2.5398075754399585, 3.1212412240545895, 3.584291817832751]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.5673828125, 'crossentropy': 1.4809479713439941})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 1.1011749505996704})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 1.0358378887176514})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 1.1733286380767822})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 1.2095363140106201})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 1.3340837955474854})
store['active_learning_steps'][31]['training']['best_epoch']=3
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.6991, 'crossentropy': 1.07809248046875}
store['active_learning_steps'][31]['acquisition']={'indices': [['id', 59771], ['id', 59726], ['id', 47079], ['id', 50529], ['id', 43241]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5466278043162174, 1.052786959712639, 1.5290659128684245, 1.9744709907093476, 2.381928847712217]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.5751953125, 'crossentropy': 1.3844707012176514})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 1.0836291313171387})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 1.0647468566894531})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 1.1592597961425781})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 1.0872334241867065})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 1.2220042943954468})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 1.3178532123565674})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 1.3225133419036865})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 1.3436517715454102})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 1.5925171375274658})
store['active_learning_steps'][32]['training']['best_epoch']=7
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.7096, 'crossentropy': 1.33021865234375}
store['active_learning_steps'][32]['acquisition']={'indices': [['id', 20643], ['id', 13133], ['id', 28741], ['id', 54465], ['id', 49410]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.8394794256907359, 1.6223375874918426, 2.3253087203753102, 2.9163155850310565, 3.390813142238546]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.529296875, 'crossentropy': 1.4418106079101562})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 1.1247926950454712})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 1.0387458801269531})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 1.0916900634765625})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 1.12727689743042})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 1.297816276550293})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 1.306565761566162})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 1.4187049865722656})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 1.4349796772003174})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.71484375, 'crossentropy': 1.469731092453003})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 1.580959439277649})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 1.7093517780303955})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.71484375, 'crossentropy': 1.678938388824463})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 1.7506346702575684})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 1.687292218208313})
store['active_learning_steps'][33]['training']['best_epoch']=12
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.7158, 'crossentropy': 1.689629296875}
store['active_learning_steps'][33]['acquisition']={'indices': [['id', 3219], ['id', 19479], ['id', 20809], ['id', 54078], ['id', 21810]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.9700339066779187, 1.844594412359748, 2.626667270482896, 3.2586679254186386, 3.725899901636252]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.5419921875, 'crossentropy': 1.5345215797424316})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 1.099855661392212})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 1.073827862739563})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 1.171064019203186})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 1.1672179698944092})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 1.1934456825256348})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.3555881977081299})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.4237682819366455})
store['active_learning_steps'][34]['training']['best_epoch']=5
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.6976, 'crossentropy': 1.207707421875}
store['active_learning_steps'][34]['acquisition']={'indices': [['id', 10233], ['id', 38100], ['id', 44204], ['id', 26380], ['id', 10548]], 'labels': [[0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.7292650202441466, 1.4114791116358765, 2.038926435033016, 2.5645076613513957, 3.008419900348878]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.513671875, 'crossentropy': 1.583473801612854})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 1.0939505100250244})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 1.000492811203003})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 1.030929684638977})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 1.109192132949829})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 1.2178728580474854})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 1.256044626235962})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 1.2811415195465088})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.71484375, 'crossentropy': 1.346481204032898})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.7236328125, 'crossentropy': 1.3952791690826416})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 1.486145257949829})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.732421875, 'crossentropy': 1.4860936403274536})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.7294921875, 'crossentropy': 1.4943230152130127})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.724609375, 'crossentropy': 1.6170978546142578})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.7265625, 'crossentropy': 1.5678136348724365})
store['active_learning_steps'][35]['training']['best_epoch']=12
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.7336, 'crossentropy': 1.4918494140625}
store['active_learning_steps'][35]['acquisition']={'indices': [['id', 17565], ['id', 46848], ['id', 23586], ['id', 38886], ['id', 49055]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [0.9426610662574557, 1.8074731719560369, 2.568693707035025, 3.1859774892690202, 3.667248606851185]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.53125, 'crossentropy': 1.4608163833618164})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 1.0989480018615723})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 1.0454083681106567})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 1.1230965852737427})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 1.1906388998031616})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 1.2142541408538818})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 1.292020320892334})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 1.4102158546447754})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 1.4608402252197266})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 1.5694565773010254})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 1.6650502681732178})
store['active_learning_steps'][36]['training']['best_epoch']=8
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.7135, 'crossentropy': 1.4035615234375}
