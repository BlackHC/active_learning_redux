store = {}
store['timestamp']=1621479486
store['cmdline']=['/home/kell4989/git/active_learning_redux/batchbald_redux/ood_experiment.py', '--id=57']
store['commit']='8a2cf4fb40ce306533b4e439b08268c53f009a3b'
store['github_url']='8a2cf4fb40ce306533b4e439b08268c53f009a3b'
store['experiment']='/home/kell4989/git/active_learning_redux/batchbald_redux/ood_experiment.py'
store['job_id']=57
store['worker_id']=57
store['num_workers']=80
store['config']={'seed': 1294, 'uniform_ood': True, 'id_dataset_type': 'batchbald_redux.fast_mnist.FastFashionMNIST', 'ood_dataset_type': 'batchbald_redux.fast_mnist.FastMNIST', 'initial_training_set_size': 20, 'validation_set_size': 1024, 'evaluation_set_size': 16, 'id_repetitions': 1, 'ood_repetitions': 1, 'add_dataset_noise': False, 'validation_split_random_state': 0, 'acquisition_size': 5, 'max_training_set': 200, 'num_pool_samples': 100, 'num_validation_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'min_samples_per_epoch': 5056, 'acquisition_function': 'batchbald_redux.acquisition_functions.BatchBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationEvalModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 8}
store['log']={}
store['dataset_info']={'training': "(FastFashionMNIST (train; 58976 samples) | one_hot_targets{'num_classes': 10}) + ('FastMNIST Train (60000 samples)' | uniform_targets{'num_classes': 10})", 'test': "'FastFashionMNIST Test (10000 samples)'"}
store['initial_training_set_indices']=[55573, 380, 12640, 44119, 30392, 58226, 43812, 52440, 3091, 29974, 49512, 46037, 53434, 22015, 37915, 52296, 8533, 58125, 22304, 35472]
store['evaluation_set_indices']=[42890, 14640, 45567, 52801, 53689, 801, 55187, 26479, 50997, 3792]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 2.125455856323242})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 2.5505850315093994})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 2.7869017124176025})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 3.2604005336761475})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 3.5748276710510254})
store['active_learning_steps'][0]['training']['best_epoch']=2
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.6161, 'crossentropy': 2.6363291015625}
store['active_learning_steps'][0]['acquisition']={'indices': [['id', 1646], ['id', 47230], ['id', 56210], ['id', 55055], ['id', 32776]], 'labels': [[0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [1.6306052330698262, 2.8394991565062098, 3.6520664409704224, 4.1252433355082925, 4.367527159140202]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.5751953125, 'crossentropy': 1.825154185295105})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 2.524202346801758})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 2.661200761795044})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 2.8201332092285156})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.595703125, 'crossentropy': 3.0908572673797607})
store['active_learning_steps'][1]['training']['best_epoch']=2
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.5948, 'crossentropy': 2.5319169921875}
store['active_learning_steps'][1]['acquisition']={'indices': [['id', 38806], ['id', 7502], ['id', 21977], ['id', 51231], ['id', 31705]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.8973481130004028, 1.7154900690743982, 2.4161026898501063, 2.9947227072513707, 3.4147509466602717]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.595703125, 'crossentropy': 1.6796544790267944})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 2.6004624366760254})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.5927734375, 'crossentropy': 2.5605969429016113})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.5947265625, 'crossentropy': 2.954899311065674})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 3.0455031394958496})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.5966796875, 'crossentropy': 3.3411972522735596})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.59765625, 'crossentropy': 2.88808536529541})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.5966796875, 'crossentropy': 3.1970584392547607})
store['active_learning_steps'][2]['training']['best_epoch']=5
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.588, 'crossentropy': 3.2313623046875}
store['active_learning_steps'][2]['acquisition']={'indices': [['id', 31895], ['id', 59924], ['id', 47164], ['id', 24388], ['id', 48801]], 'labels': [[0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.1271267461610606, 1.9433486387954737, 2.639095529375701, 3.202992782665069, 3.622821919452579]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.578125, 'crossentropy': 1.7719465494155884})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.5810546875, 'crossentropy': 2.3345460891723633})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 2.33152437210083})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 2.3736629486083984})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 2.74660587310791})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 2.671436071395874})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 2.946086883544922})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 2.9618728160858154})
store['active_learning_steps'][3]['training']['best_epoch']=5
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.5877, 'crossentropy': 2.765048828125}
store['active_learning_steps'][3]['acquisition']={'indices': [['id', 46619], ['id', 21134], ['id', 43735], ['id', 2434], ['id', 37322]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [1.1189208238151567, 2.039874552837088, 2.846694568315587, 3.399148869242648, 3.8091428961833538]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 1.472222924232483})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 2.001312494277954})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 2.4087162017822266})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 2.460662364959717})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 2.410923957824707})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 2.660196304321289})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 3.1552157402038574})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 2.604334831237793})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 3.0437655448913574})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 2.982771396636963})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 2.7201976776123047})
store['active_learning_steps'][4]['training']['best_epoch']=8
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.6245, 'crossentropy': 2.64586953125}
store['active_learning_steps'][4]['acquisition']={'indices': [['id', 54405], ['id', 27800], ['id', 2460], ['id', 36351], ['id', 31026]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.9830070394458386, 1.9013955725118183, 2.6235081030630916, 3.216305146626862, 3.6548172959202336]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 1.4923558235168457})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 1.7805739641189575})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 2.487495183944702})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.599609375, 'crossentropy': 2.557994842529297})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 2.663025379180908})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6005859375, 'crossentropy': 2.7713656425476074})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 2.917948007583618})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 2.815551280975342})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 3.0736498832702637})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 3.2954916954040527})
store['active_learning_steps'][5]['training']['best_epoch']=7
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.6131, 'crossentropy': 2.9664599609375}
store['active_learning_steps'][5]['acquisition']={'indices': [['id', 34309], ['id', 20071], ['id', 34452], ['id', 39750], ['id', 33141]], 'labels': [[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [1.0165327576173273, 1.9549429547292152, 2.6889153980130445, 3.243804972114452, 3.6833126683941977]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 1.5269907712936401})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 1.7590484619140625})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 1.9052112102508545})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 2.366352081298828})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 2.4153690338134766})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 2.437635898590088})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 2.5904946327209473})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 2.589646816253662})
store['active_learning_steps'][6]['training']['best_epoch']=5
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.6411, 'crossentropy': 2.710660546875}
store['active_learning_steps'][6]['acquisition']={'indices': [['id', 24759], ['id', 11417], ['id', 7456], ['id', 11374], ['id', 20584]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.0135215418965715, 1.8180510995157055, 2.5217543814273276, 3.1155649245785355, 3.559835945080449]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.5966796875, 'crossentropy': 1.5100781917572021})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 1.83837890625})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 2.3454792499542236})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 2.636012077331543})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 2.569446086883545})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 3.2121691703796387})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 3.2755627632141113})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 3.0040712356567383})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 2.924520969390869})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 3.0429327487945557})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 2.8836019039154053})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 3.198920249938965})
store['active_learning_steps'][7]['training']['best_epoch']=9
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.6439, 'crossentropy': 3.24051796875}
store['active_learning_steps'][7]['acquisition']={'indices': [['id', 33888], ['id', 49597], ['id', 11531], ['id', 53157], ['id', 23690]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.0527240162451788, 1.974635827348906, 2.7792275803178805, 3.390989686460986, 3.8258148911454217]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 1.3747789859771729})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 1.541761875152588})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 2.0075278282165527})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 1.911268711090088})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 2.3276050090789795})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 2.505955219268799})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 2.6006534099578857})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 2.350797653198242})
store['active_learning_steps'][8]['training']['best_epoch']=5
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.6419, 'crossentropy': 2.5671923828125}
store['active_learning_steps'][8]['acquisition']={'indices': [['id', 25434], ['id', 6394], ['id', 8485], ['id', 19809], ['id', 11095]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.9053545883112424, 1.6733236762212544, 2.3822085026048985, 2.9930729211497376, 3.4740942125137657]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.5830078125, 'crossentropy': 1.4942413568496704})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 1.9131710529327393})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 1.9841487407684326})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 2.168675184249878})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 2.508563995361328})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 2.4032468795776367})
store['active_learning_steps'][9]['training']['best_epoch']=3
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.6381, 'crossentropy': 2.069080078125}
store['active_learning_steps'][9]['acquisition']={'indices': [['id', 11901], ['id', 44686], ['id', 4618], ['id', 28080], ['id', 907]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.7279167590577282, 1.4048235736454027, 2.004131966520756, 2.520343624589726, 2.963982112696111]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.5703125, 'crossentropy': 1.5331528186798096})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 1.6198225021362305})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 1.8440876007080078})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 2.1824886798858643})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 2.285433292388916})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 2.5152111053466797})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 2.4435479640960693})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 2.55043363571167})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 2.6811370849609375})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 2.9165706634521484})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 2.833589792251587})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 2.879108428955078})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 2.678925037384033})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 3.0396714210510254})
store['active_learning_steps'][10]['training']['best_epoch']=11
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.6203, 'crossentropy': 3.1797021484375}
store['active_learning_steps'][10]['acquisition']={'indices': [['id', 1674], ['id', 53338], ['id', 4915], ['id', 33781], ['id', 58220]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.9871931109247811, 1.8700454663081976, 2.662641230179063, 3.2701841213113703, 3.7300875201881007]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.5224609375, 'crossentropy': 1.5571104288101196})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 1.494504451751709})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 1.8977234363555908})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 2.1988425254821777})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 2.189396619796753})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 2.3636064529418945})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 2.8602118492126465})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 2.834169387817383})
store['active_learning_steps'][11]['training']['best_epoch']=5
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.607, 'crossentropy': 2.5463337890625}
store['active_learning_steps'][11]['acquisition']={'indices': [['id', 44492], ['id', 18729], ['id', 15574], ['id', 41355], ['id', 27592]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.9140021820588191, 1.7771004245969282, 2.533221831109679, 3.146470997167196, 3.6105542737499796]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.58203125, 'crossentropy': 1.4757213592529297})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 1.5309804677963257})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 1.731076717376709})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 1.9786884784698486})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 2.2769999504089355})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 2.4015657901763916})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 2.154555082321167})
store['active_learning_steps'][12]['training']['best_epoch']=4
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.6164, 'crossentropy': 2.1132171875}
store['active_learning_steps'][12]['acquisition']={'indices': [['id', 27719], ['id', 39279], ['id', 10050], ['id', 56866], ['id', 9302]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.888735697343513, 1.6408607092200862, 2.3149563275716023, 2.9022099421814893, 3.3642402658824704]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 1.3534927368164062})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 1.4528038501739502})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 1.9058756828308105})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 2.003239631652832})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 2.041375160217285})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 2.2019622325897217})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 2.243100643157959})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 2.3147644996643066})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 2.402395725250244})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 2.3208799362182617})
store['active_learning_steps'][13]['training']['best_epoch']=7
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.6252, 'crossentropy': 2.5003208984375}
store['active_learning_steps'][13]['acquisition']={'indices': [['id', 35781], ['id', 15300], ['id', 16751], ['id', 5893], ['id', 4703]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.9562243584886188, 1.8097447856699715, 2.5278513083933998, 3.117386828593613, 3.5700670075014944]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.5615234375, 'crossentropy': 1.4382102489471436})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 1.4606677293777466})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 1.6922898292541504})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 1.959923267364502})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.599609375, 'crossentropy': 2.183990240097046})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 2.137451171875})
store['active_learning_steps'][14]['training']['best_epoch']=3
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.6171, 'crossentropy': 1.7906259765625}
store['active_learning_steps'][14]['acquisition']={'indices': [['id', 1921], ['id', 51167], ['id', 26636], ['id', 47079], ['id', 18255]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.7563169379461046, 1.420180538742497, 2.038558807689384, 2.560640290241479, 3.004709485190583]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.58203125, 'crossentropy': 1.347506046295166})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 1.3474509716033936})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 1.5722579956054688})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 1.8183529376983643})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 2.064579486846924})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 1.6677027940750122})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 2.1682939529418945})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 2.1075544357299805})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 2.1605749130249023})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 2.1686224937438965})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 2.462871551513672})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 2.421736240386963})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 2.0216710567474365})
store['active_learning_steps'][15]['training']['best_epoch']=10
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.6498, 'crossentropy': 2.3147544921875}
store['active_learning_steps'][15]['acquisition']={'indices': [['id', 9943], ['id', 52955], ['id', 33446], ['id', 57783], ['id', 13384]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.9062611804815635, 1.7805667602332682, 2.570726200256975, 3.1846670886697392, 3.650852011425367]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.5693359375, 'crossentropy': 1.460775375366211})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 1.3709684610366821})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 1.5399565696716309})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 1.6340758800506592})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 1.818387746810913})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 1.9190139770507812})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 2.013113021850586})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 1.9576778411865234})
store['active_learning_steps'][16]['training']['best_epoch']=5
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.6313, 'crossentropy': 1.9227068359375}
store['active_learning_steps'][16]['acquisition']={'indices': [['id', 42424], ['id', 57213], ['id', 43543], ['id', 22875], ['id', 36749]], 'labels': [[0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.8356557439757755, 1.61259015171514, 2.2991513346467887, 2.9050245319770776, 3.366273862290422]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.5673828125, 'crossentropy': 1.366865634918213})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 1.3598639965057373})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 1.4044909477233887})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 1.677002191543579})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 1.927026391029358})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 2.0619618892669678})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 2.153170108795166})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 2.11857271194458})
store['active_learning_steps'][17]['training']['best_epoch']=5
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.6253, 'crossentropy': 2.0967154296875}
store['active_learning_steps'][17]['acquisition']={'indices': [['id', 25420], ['id', 3009], ['id', 38438], ['id', 22139], ['id', 22069]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.9472578262370233, 1.7660030872020425, 2.40226801014002, 2.921485561864543, 3.3509388952630825]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.595703125, 'crossentropy': 1.4372990131378174})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 1.3855156898498535})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 1.6420625448226929})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 1.9483612775802612})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 2.04107666015625})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 1.9923837184906006})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 2.099843740463257})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 2.1658406257629395})
store['active_learning_steps'][18]['training']['best_epoch']=5
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.6366, 'crossentropy': 2.1516158203125}
store['active_learning_steps'][18]['acquisition']={'indices': [['id', 21615], ['id', 12579], ['id', 9692], ['id', 50158], ['id', 44511]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [1.0178434207235452, 1.7895717132561524, 2.4706099431201176, 3.05759182927903, 3.4930683299305096]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.560546875, 'crossentropy': 1.3992295265197754})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.591796875, 'crossentropy': 1.3035144805908203})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.599609375, 'crossentropy': 1.4925496578216553})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 1.6454226970672607})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 1.7471554279327393})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 1.9612746238708496})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 2.0126075744628906})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 2.200701951980591})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 2.0689826011657715})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 2.417006492614746})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 2.2090044021606445})
store['active_learning_steps'][19]['training']['best_epoch']=8
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.6177, 'crossentropy': 2.38761640625}
store['active_learning_steps'][19]['acquisition']={'indices': [['id', 55037], ['id', 2388], ['id', 13903], ['id', 4194], ['id', 47659]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.994895058001686, 1.7944909973856742, 2.5014104130385135, 3.0951612776454827, 3.5630729625854336]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 1.398125171661377})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 1.262845754623413})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 1.3162438869476318})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 1.4275895357131958})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 1.5820598602294922})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 1.8146506547927856})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 1.8580231666564941})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 2.142153263092041})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 2.1217947006225586})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 2.259037971496582})
store['active_learning_steps'][20]['training']['best_epoch']=7
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.6477, 'crossentropy': 2.016029296875}
store['active_learning_steps'][20]['acquisition']={'indices': [['id', 53882], ['id', 29437], ['id', 45510], ['id', 10319], ['id', 26217]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.8109291755198871, 1.567230809855642, 2.2491971337567485, 2.8369459533952455, 3.3265439590843204]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.513671875, 'crossentropy': 1.4649730920791626})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 1.2058517932891846})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 1.347808837890625})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 1.3678486347198486})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 1.5531556606292725})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 1.6962027549743652})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 1.775602102279663})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 1.829163908958435})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 1.9290766716003418})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 1.8936536312103271})
store['active_learning_steps'][21]['training']['best_epoch']=7
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.6341, 'crossentropy': 1.8427052734375}
store['active_learning_steps'][21]['acquisition']={'indices': [['id', 12692], ['id', 38683], ['id', 59953], ['id', 59691], ['id', 35913]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.9342742360684613, 1.8008167867615876, 2.48951618418854, 3.0534343554667123, 3.4957520779400397]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.5771484375, 'crossentropy': 1.2969907522201538})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.5947265625, 'crossentropy': 1.2775986194610596})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 1.4676568508148193})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 1.5462672710418701})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 1.7426090240478516})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 1.794296383857727})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 2.016436815261841})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 2.0211682319641113})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 2.0221338272094727})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 2.113783359527588})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 2.1779065132141113})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 2.2144947052001953})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 2.1200122833251953})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 2.236544609069824})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 2.2631077766418457})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 2.20068359375})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 2.412942409515381})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 2.539142608642578})
store['active_learning_steps'][22]['training']['best_epoch']=15
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.6518, 'crossentropy': 2.4179689453125}
store['active_learning_steps'][22]['acquisition']={'indices': [['id', 7859], ['id', 56244], ['id', 2464], ['id', 38782], ['id', 45276]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.092568825367135, 1.952821218098654, 2.7198497311723964, 3.3496327023800063, 3.7957016302908775]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.556640625, 'crossentropy': 1.439990520477295})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 1.169870138168335})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 1.2814304828643799})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 1.411757469177246})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 1.6187286376953125})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 1.5183429718017578})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 1.5667598247528076})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 1.9101569652557373})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 1.7681727409362793})
store['active_learning_steps'][23]['training']['best_epoch']=6
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.6522, 'crossentropy': 1.649833203125}
store['active_learning_steps'][23]['acquisition']={'indices': [['id', 36323], ['id', 18584], ['id', 55968], ['id', 24433], ['id', 26263]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.8610919915232853, 1.6418367149374928, 2.3468111364372586, 2.9127389334622844, 3.3801875503072303]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.564453125, 'crossentropy': 1.510080337524414})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 1.1459976434707642})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 1.2287557125091553})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 1.439704179763794})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 1.4180395603179932})
store['active_learning_steps'][24]['training']['best_epoch']=2
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.6666, 'crossentropy': 1.17201484375}
store['active_learning_steps'][24]['acquisition']={'indices': [['id', 1254], ['id', 29012], ['id', 21960], ['id', 3301], ['id', 49891]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5027968576145534, 0.9451205376586178, 1.3570437621364402, 1.736326079031354, 2.0876515248116476]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.5244140625, 'crossentropy': 1.47199547290802})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 1.186124563217163})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 1.2847349643707275})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 1.3942835330963135})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 1.4224231243133545})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 1.5830883979797363})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 1.6546580791473389})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 1.6481196880340576})
store['active_learning_steps'][25]['training']['best_epoch']=5
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.67, 'crossentropy': 1.46157421875}
store['active_learning_steps'][25]['acquisition']={'indices': [['id', 22576], ['id', 31016], ['id', 28356], ['id', 56635], ['id', 22163]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.7504883541074974, 1.4285726396707705, 2.0512343741573726, 2.5767485290792322, 3.0230300604534097]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.5478515625, 'crossentropy': 1.4504709243774414})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.595703125, 'crossentropy': 1.186015009880066})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 1.2024555206298828})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 1.2542777061462402})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 1.3693431615829468})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 1.5294930934906006})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 1.6211551427841187})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 1.8277297019958496})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 1.6001468896865845})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 2.0123467445373535})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 1.8620707988739014})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 1.878136157989502})
store['active_learning_steps'][26]['training']['best_epoch']=9
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.6635, 'crossentropy': 1.8368390625}
store['active_learning_steps'][26]['acquisition']={'indices': [['id', 1799], ['id', 39153], ['id', 17574], ['id', 45484], ['id', 34091]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.9556836290511237, 1.8595227558304392, 2.5659586228556863, 3.147920855261143, 3.5752720360573687]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.5576171875, 'crossentropy': 1.5019323825836182})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 1.2211694717407227})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 1.309751033782959})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 1.3747273683547974})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 1.6424672603607178})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 1.7375690937042236})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 1.7625970840454102})
store['active_learning_steps'][27]['training']['best_epoch']=4
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.6521, 'crossentropy': 1.42287109375}
store['active_learning_steps'][27]['acquisition']={'indices': [['id', 36872], ['id', 55098], ['id', 57976], ['id', 43542], ['id', 41358]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6811942617539322, 1.2952334242262986, 1.8736280111638761, 2.3778338282478106, 2.829197279814978]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.5048828125, 'crossentropy': 1.5293381214141846})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 1.1464662551879883})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 1.1692898273468018})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 1.3416424989700317})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 1.6491115093231201})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 1.6569089889526367})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 1.7820346355438232})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 1.914623737335205})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 1.879404067993164})
store['active_learning_steps'][28]['training']['best_epoch']=6
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.6712, 'crossentropy': 1.63625029296875}
store['active_learning_steps'][28]['acquisition']={'indices': [['id', 70], ['id', 17613], ['id', 9924], ['id', 19888], ['id', 12205]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.813667579413724, 1.5464877968800375, 2.2102853299815273, 2.794361019557627, 3.271295088927304]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.513671875, 'crossentropy': 1.5183000564575195})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.591796875, 'crossentropy': 1.2285387516021729})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 1.253075361251831})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 1.2826457023620605})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 1.4812119007110596})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 1.637493371963501})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 1.7133413553237915})
store['active_learning_steps'][29]['training']['best_epoch']=4
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.6697, 'crossentropy': 1.311825390625}
store['active_learning_steps'][29]['acquisition']={'indices': [['id', 20173], ['id', 17076], ['id', 21784], ['id', 58110], ['id', 52266]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6662686456273792, 1.2672969835639711, 1.82972754968133, 2.3314508704845913, 2.7823245250495203]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.478515625, 'crossentropy': 1.6061017513275146})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 1.1808699369430542})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 1.2271971702575684})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 1.3114471435546875})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 1.5314204692840576})
store['active_learning_steps'][30]['training']['best_epoch']=2
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.6394, 'crossentropy': 1.22404853515625}
store['active_learning_steps'][30]['acquisition']={'indices': [['id', 56781], ['id', 10860], ['id', 1031], ['id', 56756], ['id', 59657]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.4623721841774593, 0.9067852744695779, 1.3018223506379147, 1.6740520375268098, 2.008350490558958]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.5458984375, 'crossentropy': 1.4758234024047852})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 1.225069522857666})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 1.2692019939422607})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 1.3195314407348633})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 1.3971378803253174})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 1.6350395679473877})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 1.6593546867370605})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 1.7094614505767822})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 1.8210716247558594})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 1.84629225730896})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 2.022782802581787})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 1.9503788948059082})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 2.1238512992858887})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 2.093513011932373})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 2.0857815742492676})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 2.204817771911621})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 2.3096866607666016})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 2.309607982635498})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 2.564164400100708})
store['active_learning_steps'][31]['training']['best_epoch']=16
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.6733, 'crossentropy': 2.132879296875}
store['active_learning_steps'][31]['acquisition']={'indices': [['id', 22718], ['id', 1145], ['id', 26392], ['id', 38264], ['id', 2898]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.9154639883812203, 1.784894548616255, 2.5413735488106335, 3.178406905544451, 3.656925037984263]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.5322265625, 'crossentropy': 1.5370771884918213})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 1.2912406921386719})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 1.213496446609497})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 1.3106021881103516})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 1.5229511260986328})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 1.6534898281097412})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 1.7581071853637695})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 1.7613403797149658})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 1.7868865728378296})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 2.03603196144104})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 1.9089093208312988})
store['active_learning_steps'][32]['training']['best_epoch']=8
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.6797, 'crossentropy': 1.83538515625}
store['active_learning_steps'][32]['acquisition']={'indices': [['id', 19268], ['id', 3734], ['id', 7593], ['id', 20841], ['id', 31256]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.8032508908767002, 1.5584707483168412, 2.2403130644963873, 2.8391868327397702, 3.309411847619958]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.498046875, 'crossentropy': 1.5489323139190674})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 1.2061705589294434})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 1.1502406597137451})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 1.203021764755249})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 1.546617031097412})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 1.4733299016952515})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 1.5993363857269287})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 1.7075855731964111})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 1.8816018104553223})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 1.744035005569458})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 1.8395951986312866})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 1.7532165050506592})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 2.0240750312805176})
store['active_learning_steps'][33]['training']['best_epoch']=10
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.6671, 'crossentropy': 1.8547765625}
store['active_learning_steps'][33]['acquisition']={'indices': [['id', 59468], ['id', 44983], ['id', 5413], ['id', 36293], ['id', 58557]], 'labels': [[0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.8014131899442236, 1.5505893315109653, 2.2453999697019187, 2.841721727410766, 3.323934632404411]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.51953125, 'crossentropy': 1.6323041915893555})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 1.2237282991409302})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 1.2167797088623047})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 1.3128819465637207})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 1.4835985898971558})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 1.4152644872665405})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 1.6329903602600098})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 1.576637864112854})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 1.7393317222595215})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 1.8234777450561523})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 1.9394824504852295})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 2.143324851989746})
store['active_learning_steps'][34]['training']['best_epoch']=9
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.6672, 'crossentropy': 1.8307884765625}
store['active_learning_steps'][34]['acquisition']={'indices': [['id', 30098], ['id', 57225], ['id', 36120], ['id', 3976], ['id', 7372]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.8232452918911579, 1.5866919977443712, 2.2774799898694837, 2.86774923043137, 3.3479559594236337]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.51171875, 'crossentropy': 1.6625094413757324})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.5908203125, 'crossentropy': 1.3220436573028564})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 1.214349389076233})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 1.225099802017212})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 1.3129404783248901})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 1.4835985898971558})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 1.5772502422332764})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 1.6759517192840576})
store['active_learning_steps'][35]['training']['best_epoch']=5
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.6742, 'crossentropy': 1.39740546875}
store['active_learning_steps'][35]['acquisition']={'indices': [['id', 20624], ['id', 29354], ['id', 9862], ['id', 13237], ['id', 5513]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6982900399650047, 1.3500459744158055, 1.9406886603165177, 2.475828607695844, 2.92537093886345]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.548828125, 'crossentropy': 1.4674221277236938})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 1.1821458339691162})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 1.2077529430389404})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 1.2989625930786133})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 1.3219380378723145})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 1.5044803619384766})
store['active_learning_steps'][36]['training']['best_epoch']=3
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.6562, 'crossentropy': 1.2515048828125}
