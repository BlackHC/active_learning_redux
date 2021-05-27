store = {}
store['timestamp']=1622064902
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/experiment_ood.py', '--id=3']
store['commit']='687a8dd5b631132403a94f206eb0a7ba2c3b7a98'
store['github_url']='687a8dd5b631132403a94f206eb0a7ba2c3b7a98'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/experiment_ood.py'
store['job_id']=3
store['worker_id']=3
store['num_workers']=80
store['config']={'seed': 1237, 'uniform_ood': False, 'id_dataset_type': 'batchbald_redux.fast_mnist.FastFashionMNIST', 'ood_dataset_type': 'batchbald_redux.fast_mnist.FastMNIST', 'initial_training_set_size': 20, 'validation_set_size': 1024, 'evaluation_set_size': 16, 'id_repetitions': 1, 'ood_repetitions': 1, 'add_dataset_noise': False, 'validation_split_random_state': 0, 'acquisition_size': 5, 'max_training_set': 200, 'num_pool_samples': 100, 'num_validation_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'min_samples_per_epoch': 5056, 'acquisition_function': 'batchbald_redux.acquisition_functions.BatchEvalBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationEvalModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 8}
store['log']={}
store['dataset_info']={'training': "(FastFashionMNIST (train; 58976 samples)) + ('FastMNIST Train (60000 samples)' | constant_target{'target': tensor(-1, device='cuda:0'), 'num_classes': 10})", 'test': "'FastFashionMNIST Test (10000 samples)'"}
store['initial_training_set_indices']=[55573, 380, 12640, 44119, 30392, 58226, 43812, 52440, 3091, 29974, 49512, 46037, 53434, 22015, 37915, 52296, 8533, 58125, 22304, 35472]
store['evaluation_set_indices']=[42890, 14640, 45567, 52801, 53689, 801, 55187, 26479, 50997, 3792]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 2.220853805541992})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 2.6909327507019043})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 2.9579710960388184})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 3.031991720199585})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 3.7753753662109375})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 3.5379536151885986})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 3.1273884773254395})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 3.190985918045044})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 3.650599479675293})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 3.607814311981201})
store['active_learning_steps'][0]['training']['best_epoch']=7
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.6101, 'crossentropy': 3.36756640625}
store['active_learning_steps'][0]['eval_training']={}
store['active_learning_steps'][0]['eval_training']['epochs']=[]
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 1.6753374338150024})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 1.7432823181152344})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 1.617645263671875})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 1.6313049793243408})
store['active_learning_steps'][0]['eval_training']['best_epoch']=1
store['active_learning_steps'][0]['acquisition']={'indices': [['ood', 22481], ['ood', 4014], ['id', 26279], ['ood', 1477], ['id', 10567]], 'labels': [-1, -1, 6, -1, 3], 'scores': [1.053139121627829, 1.7835589384247161, 2.255411773208232, 2.5244731662924442, 2.701362411209551]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.5771484375, 'crossentropy': 2.3945364952087402})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 3.1169400215148926})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 3.2034854888916016})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.560546875, 'crossentropy': 3.8625295162200928})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 3.441411256790161})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 4.102725505828857})
store['active_learning_steps'][1]['training']['best_epoch']=3
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.5879, 'crossentropy': 3.488129296875}
store['active_learning_steps'][1]['eval_training']={}
store['active_learning_steps'][1]['eval_training']['epochs']=[]
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 1.8497848510742188})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 1.8455047607421875})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.603515625, 'crossentropy': 1.989394187927246})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 1.8584904670715332})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 1.8910393714904785})
store['active_learning_steps'][1]['eval_training']['best_epoch']=5
store['active_learning_steps'][1]['acquisition']={'indices': [['ood', 914], ['ood', 8932], ['ood', 38211], ['ood', 8762], ['ood', 5580]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.093551697860704, 1.8838387993330261, 2.5020992520885326, 2.91888562382566, 3.1279088072732146]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.599609375, 'crossentropy': 2.3940768241882324})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 2.8346452713012695})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 3.0743610858917236})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 3.2359707355499268})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 3.510432243347168})
store['active_learning_steps'][2]['training']['best_epoch']=2
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.6009, 'crossentropy': 2.79224375}
store['active_learning_steps'][2]['eval_training']={}
store['active_learning_steps'][2]['eval_training']['epochs']=[]
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 1.76076340675354})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.59765625, 'crossentropy': 1.7884190082550049})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.6005859375, 'crossentropy': 1.7941361665725708})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.5908203125, 'crossentropy': 1.662725567817688})
store['active_learning_steps'][2]['eval_training']['best_epoch']=1
store['active_learning_steps'][2]['acquisition']={'indices': [['ood', 41339], ['ood', 55177], ['ood', 35483], ['id', 45450], ['id', 16611]], 'labels': [-1, -1, -1, 7, 2], 'scores': [0.88303404927417, 1.588381002618581, 2.041253256969793, 2.357838020197579, 2.5276405315010866]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.5947265625, 'crossentropy': 2.4049124717712402})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.595703125, 'crossentropy': 3.377661943435669})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.583984375, 'crossentropy': 4.104168891906738})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.5732421875, 'crossentropy': 3.8044731616973877})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.572265625, 'crossentropy': 4.054912567138672})
store['active_learning_steps'][3]['training']['best_epoch']=2
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.57, 'crossentropy': 3.796761328125}
store['active_learning_steps'][3]['eval_training']={}
store['active_learning_steps'][3]['eval_training']['epochs']=[]
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.603515625, 'crossentropy': 1.8061444759368896})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.5869140625, 'crossentropy': 1.9847314357757568})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.599609375, 'crossentropy': 1.9000579118728638})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.5888671875, 'crossentropy': 2.0463156700134277})
store['active_learning_steps'][3]['eval_training']['best_epoch']=1
store['active_learning_steps'][3]['acquisition']={'indices': [['ood', 59101], ['id', 49224], ['ood', 55041], ['ood', 4875], ['id', 21636]], 'labels': [-1, 5, -1, -1, 0], 'scores': [0.9084854316634823, 1.594055357151536, 2.0534412498530124, 2.327965948818365, 2.475926091411332]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.58203125, 'crossentropy': 2.533261775970459})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.580078125, 'crossentropy': 3.0603556632995605})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.583984375, 'crossentropy': 3.9623658657073975})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.5830078125, 'crossentropy': 3.0994873046875})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.5908203125, 'crossentropy': 4.283539772033691})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.5830078125, 'crossentropy': 4.237751007080078})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.5732421875, 'crossentropy': 4.308269023895264})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 4.396562099456787})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.5888671875, 'crossentropy': 3.824437141418457})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.5810546875, 'crossentropy': 4.809474945068359})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.5830078125, 'crossentropy': 4.1715922355651855})
store['active_learning_steps'][4]['training']['best_epoch']=8
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.5865, 'crossentropy': 4.575020703125}
store['active_learning_steps'][4]['eval_training']={}
store['active_learning_steps'][4]['eval_training']['epochs']=[]
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 2.0150673389434814})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.5947265625, 'crossentropy': 2.0148348808288574})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.599609375, 'crossentropy': 2.1173887252807617})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.599609375, 'crossentropy': 1.9833334684371948})
store['active_learning_steps'][4]['eval_training']['best_epoch']=1
store['active_learning_steps'][4]['acquisition']={'indices': [['ood', 38001], ['ood', 111], ['ood', 8376], ['ood', 6377], ['ood', 5652]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.1816945752671875, 2.1328936267188974, 2.792309545886869, 3.1486541901035396, 3.32688547539027]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.595703125, 'crossentropy': 2.3483991622924805})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.5947265625, 'crossentropy': 3.0852346420288086})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 3.6235620975494385})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 3.762336015701294})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 3.9902405738830566})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 3.6422739028930664})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 3.9204721450805664})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 3.7982566356658936})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.595703125, 'crossentropy': 4.008077144622803})
store['active_learning_steps'][5]['training']['best_epoch']=6
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.5877, 'crossentropy': 3.952782421875}
store['active_learning_steps'][5]['eval_training']={}
store['active_learning_steps'][5]['eval_training']['epochs']=[]
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.58984375, 'crossentropy': 1.8887333869934082})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 1.9434301853179932})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.595703125, 'crossentropy': 2.0288326740264893})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.5966796875, 'crossentropy': 2.113281011581421})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.59375, 'crossentropy': 2.1952295303344727})
store['active_learning_steps'][5]['eval_training']['best_epoch']=2
store['active_learning_steps'][5]['acquisition']={'indices': [['ood', 53956], ['ood', 36295], ['ood', 50939], ['ood', 34314], ['ood', 32776]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.1806910830835813, 2.0921645635320596, 2.6312616924894225, 2.9699878832634465, 3.101844792646073]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.5859375, 'crossentropy': 2.3955068588256836})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.5927734375, 'crossentropy': 3.0503034591674805})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.591796875, 'crossentropy': 3.6491315364837646})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 3.683307647705078})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.59375, 'crossentropy': 3.5656251907348633})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.5810546875, 'crossentropy': 4.338352203369141})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6005859375, 'crossentropy': 4.03116512298584})
store['active_learning_steps'][6]['training']['best_epoch']=4
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.582, 'crossentropy': 4.063527734375}
store['active_learning_steps'][6]['eval_training']={}
store['active_learning_steps'][6]['eval_training']['epochs']=[]
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 2.0494399070739746})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.5908203125, 'crossentropy': 2.2721385955810547})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.5859375, 'crossentropy': 2.3946173191070557})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.595703125, 'crossentropy': 2.2210919857025146})
store['active_learning_steps'][6]['eval_training']['best_epoch']=1
store['active_learning_steps'][6]['acquisition']={'indices': [['ood', 47303], ['ood', 12003], ['id', 52904], ['id', 4809], ['ood', 59731]], 'labels': [-1, -1, 8, 9, -1], 'scores': [1.0651358946950404, 1.9201709204779185, 2.4084110847747477, 2.720313395823844, 2.889209135957273]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 2.1517515182495117})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.5986328125, 'crossentropy': 3.0909833908081055})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.599609375, 'crossentropy': 2.935910701751709})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 3.757999897003174})
store['active_learning_steps'][7]['training']['best_epoch']=1
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.591, 'crossentropy': 2.27773203125}
store['active_learning_steps'][7]['eval_training']={}
store['active_learning_steps'][7]['eval_training']['epochs']=[]
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.5986328125, 'crossentropy': 1.5482560396194458})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.5927734375, 'crossentropy': 1.5674622058868408})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.5888671875, 'crossentropy': 1.4989306926727295})
store['active_learning_steps'][7]['eval_training']['best_epoch']=1
store['active_learning_steps'][7]['acquisition']={'indices': [['ood', 50622], ['ood', 2634], ['ood', 48072], ['id', 53215], ['id', 32992]], 'labels': [-1, -1, -1, 5, 6], 'scores': [0.8531260864582766, 1.5323723064487735, 2.0160851996335136, 2.32175926910013, 2.46798421621755]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.5966796875, 'crossentropy': 2.1003851890563965})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.595703125, 'crossentropy': 3.1761999130249023})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.5986328125, 'crossentropy': 3.3251938819885254})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 3.443199634552002})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 3.5811352729797363})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 3.612006664276123})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 3.426295757293701})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 3.7660727500915527})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 4.3458147048950195})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 3.3537347316741943})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.599609375, 'crossentropy': 4.158792972564697})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.58984375, 'crossentropy': 4.468881130218506})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 4.276734828948975})
store['active_learning_steps'][8]['training']['best_epoch']=10
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.6103, 'crossentropy': 3.64501953125}
store['active_learning_steps'][8]['eval_training']={}
store['active_learning_steps'][8]['eval_training']['epochs']=[]
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.5888671875, 'crossentropy': 2.090862274169922})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 1.8806366920471191})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 1.872375726699829})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 1.8596690893173218})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 1.914232611656189})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 1.8415336608886719})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 1.8210030794143677})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 1.937093734741211})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 1.929255723953247})
store['active_learning_steps'][8]['eval_training']['best_epoch']=6
store['active_learning_steps'][8]['acquisition']={'indices': [['ood', 34551], ['ood', 8826], ['id', 1254], ['id', 59475], ['id', 10647]], 'labels': [-1, -1, 0, 2, 0], 'scores': [0.9243967636363759, 1.6419129312923928, 2.1548860631510274, 2.4516473409188553, 2.6466722913730414]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 1.903458595275879})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 2.7093255519866943})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 3.022383213043213})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 3.761711359024048})
store['active_learning_steps'][9]['training']['best_epoch']=1
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.5976, 'crossentropy': 2.03333359375}
store['active_learning_steps'][9]['eval_training']={}
store['active_learning_steps'][9]['eval_training']['epochs']=[]
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 1.2987332344055176})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 1.2692453861236572})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 1.2921018600463867})
store['active_learning_steps'][9]['eval_training']['best_epoch']=1
store['active_learning_steps'][9]['acquisition']={'indices': [['ood', 24625], ['ood', 37010], ['ood', 9379], ['ood', 40547], ['id', 53134]], 'labels': [-1, -1, -1, -1, 0], 'scores': [0.6982510388873873, 1.2259090051095218, 1.5960590012110885, 1.8532036884239949, 2.020973010546787]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 1.9542338848114014})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.59765625, 'crossentropy': 3.2652974128723145})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.599609375, 'crossentropy': 3.3680524826049805})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.5869140625, 'crossentropy': 3.648466110229492})
store['active_learning_steps'][10]['training']['best_epoch']=1
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.5957, 'crossentropy': 2.04608359375}
store['active_learning_steps'][10]['eval_training']={}
store['active_learning_steps'][10]['eval_training']['epochs']=[]
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 1.3297898769378662})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 1.2014944553375244})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 1.2495381832122803})
store['active_learning_steps'][10]['eval_training']['best_epoch']=3
store['active_learning_steps'][10]['acquisition']={'indices': [['ood', 7859], ['ood', 18846], ['ood', 48402], ['ood', 53921], ['id', 55305]], 'labels': [-1, -1, -1, -1, 2], 'scores': [0.8398333106186575, 1.4437009652457689, 1.9231129336314252, 2.2278331097231407, 2.4641422990445556]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 2.0548434257507324})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 2.7313475608825684})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 3.422837257385254})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 3.360161781311035})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 3.2631306648254395})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 3.496201992034912})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 3.5489819049835205})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 4.065823554992676})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 3.918771266937256})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 4.036929130554199})
store['active_learning_steps'][11]['training']['best_epoch']=7
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.6093, 'crossentropy': 3.986243359375}
store['active_learning_steps'][11]['eval_training']={}
store['active_learning_steps'][11]['eval_training']['epochs']=[]
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 1.945820689201355})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.5947265625, 'crossentropy': 2.40323543548584})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 2.4544646739959717})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.6005859375, 'crossentropy': 2.535688877105713})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 2.294114589691162})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 2.455483913421631})
store['active_learning_steps'][11]['eval_training']['best_epoch']=3
store['active_learning_steps'][11]['acquisition']={'indices': [['ood', 2648], ['ood', 26496], ['ood', 28], ['ood', 27537], ['ood', 59802]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.2662443203995015, 2.181838228902943, 2.7483273675440727, 3.099422625002297, 3.3438512358753316]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 2.0585670471191406})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 2.679631233215332})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.5986328125, 'crossentropy': 3.268458366394043})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 3.31778883934021})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.603515625, 'crossentropy': 3.9297454357147217})
store['active_learning_steps'][12]['training']['best_epoch']=2
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.602, 'crossentropy': 2.81010390625}
store['active_learning_steps'][12]['eval_training']={}
store['active_learning_steps'][12]['eval_training']['epochs']=[]
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 1.787914752960205})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 1.7254209518432617})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 1.7229118347167969})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 1.6985130310058594})
store['active_learning_steps'][12]['eval_training']['best_epoch']=3
store['active_learning_steps'][12]['acquisition']={'indices': [['ood', 12027], ['ood', 48372], ['id', 45573], ['id', 34184], ['id', 49828]], 'labels': [-1, -1, 5, 0, 8], 'scores': [0.8369559946970127, 1.416475171744716, 1.8530248622059489, 2.1777514251023007, 2.373847397313111]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.5966796875, 'crossentropy': 1.810488224029541})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6005859375, 'crossentropy': 2.842292308807373})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 3.0036046504974365})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.591796875, 'crossentropy': 3.5002198219299316})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 3.1757960319519043})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 3.503401756286621})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.595703125, 'crossentropy': 3.651970863342285})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 3.8626856803894043})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 3.566340923309326})
store['active_learning_steps'][13]['training']['best_epoch']=6
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.613, 'crossentropy': 3.507087890625}
store['active_learning_steps'][13]['eval_training']={}
store['active_learning_steps'][13]['eval_training']['epochs']=[]
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.5966796875, 'crossentropy': 1.9560117721557617})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 1.965944766998291})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 2.0842819213867188})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 2.178316831588745})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 2.1993460655212402})
store['active_learning_steps'][13]['eval_training']['best_epoch']=2
store['active_learning_steps'][13]['acquisition']={'indices': [['ood', 20500], ['ood', 8644], ['ood', 19764], ['ood', 32288], ['id', 55521]], 'labels': [-1, -1, -1, -1, 5], 'scores': [0.8757065865687155, 1.5489747800715001, 2.007493993725811, 2.3192490074707752, 2.4874147661054486]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 1.7840230464935303})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 2.515625})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 3.1707444190979004})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 3.2878921031951904})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 3.2313714027404785})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 3.5966320037841797})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 3.7952609062194824})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 3.9222636222839355})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 4.462772846221924})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 4.448578834533691})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 4.356271743774414})
store['active_learning_steps'][14]['training']['best_epoch']=8
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.6303, 'crossentropy': 3.91672734375}
store['active_learning_steps'][14]['eval_training']={}
store['active_learning_steps'][14]['eval_training']['epochs']=[]
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 1.5815529823303223})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 1.7803692817687988})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 1.8514273166656494})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 1.9347138404846191})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 1.8968831300735474})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 1.9238762855529785})
store['active_learning_steps'][14]['eval_training']['best_epoch']=3
store['active_learning_steps'][14]['acquisition']={'indices': [['ood', 17041], ['ood', 3768], ['ood', 25793], ['ood', 38126], ['ood', 16072]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.1244997133284125, 1.9657389347477587, 2.6346080790909205, 3.084592581253366, 3.3148729494684135]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 1.8644075393676758})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 2.680250644683838})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.59375, 'crossentropy': 3.0844168663024902})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 3.2362771034240723})
store['active_learning_steps'][15]['training']['best_epoch']=1
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.6051, 'crossentropy': 1.7970830078125}
store['active_learning_steps'][15]['eval_training']={}
store['active_learning_steps'][15]['eval_training']['epochs']=[]
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 1.2954254150390625})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 1.2529932260513306})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 1.208223819732666})
store['active_learning_steps'][15]['eval_training']['best_epoch']=2
store['active_learning_steps'][15]['acquisition']={'indices': [['ood', 31726], ['id', 36482], ['ood', 38626], ['ood', 32459], ['ood', 8978]], 'labels': [-1, 8, -1, -1, -1], 'scores': [0.8020302506065691, 1.371239408219413, 1.8158437017198175, 2.1299950287001943, 2.2942715437356096]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 1.6774625778198242})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 2.329644203186035})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 3.1489388942718506})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 2.956984281539917})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 3.5817768573760986})
store['active_learning_steps'][16]['training']['best_epoch']=2
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.6202, 'crossentropy': 2.635202734375}
store['active_learning_steps'][16]['eval_training']={}
store['active_learning_steps'][16]['eval_training']['epochs']=[]
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.6005859375, 'crossentropy': 1.568519115447998})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 1.7490932941436768})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 1.5450942516326904})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 1.5360052585601807})
store['active_learning_steps'][16]['eval_training']['best_epoch']=4
store['active_learning_steps'][16]['acquisition']={'indices': [['ood', 18092], ['ood', 20113], ['ood', 53738], ['ood', 1477], ['ood', 42384]], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.9765652614581892, 1.7443257312764486, 2.284619089785806, 2.6874791382598575, 2.988697145702477]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.587890625, 'crossentropy': 1.895050048828125})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.5986328125, 'crossentropy': 2.664579153060913})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.5986328125, 'crossentropy': 2.9860267639160156})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 3.6043806076049805})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.5947265625, 'crossentropy': 4.036805629730225})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.595703125, 'crossentropy': 3.699812412261963})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 3.7018604278564453})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.603515625, 'crossentropy': 3.978283643722534})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 4.023881912231445})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.59375, 'crossentropy': 4.481252670288086})
store['active_learning_steps'][17]['training']['best_epoch']=7
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.6022, 'crossentropy': 3.7543890625}
store['active_learning_steps'][17]['eval_training']={}
store['active_learning_steps'][17]['eval_training']['epochs']=[]
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 1.6343297958374023})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 1.8756449222564697})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 2.077716827392578})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 2.0737037658691406})
store['active_learning_steps'][17]['eval_training']['best_epoch']=1
store['active_learning_steps'][17]['acquisition']={'indices': [['ood', 15403], ['ood', 27431], ['ood', 33821], ['ood', 34901], ['id', 1305]], 'labels': [-1, -1, -1, -1, 9], 'scores': [0.9598927667107436, 1.7009297981832139, 2.215746476414479, 2.516101617989815, 2.69742408827715]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 1.7345764636993408})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 2.5865111351013184})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 2.79140567779541})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 3.439943313598633})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 2.982654094696045})
store['active_learning_steps'][18]['training']['best_epoch']=2
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.6249, 'crossentropy': 2.5153064453125}
store['active_learning_steps'][18]['eval_training']={}
store['active_learning_steps'][18]['eval_training']['epochs']=[]
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 1.5561914443969727})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 1.3916034698486328})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 1.4676389694213867})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 1.336256980895996})
store['active_learning_steps'][18]['eval_training']['best_epoch']=2
store['active_learning_steps'][18]['acquisition']={'indices': [['ood', 38687], ['ood', 18572], ['id', 21979], ['id', 23444], ['ood', 23226]], 'labels': [-1, -1, 0, 2, -1], 'scores': [0.8805546178244164, 1.4521172652635141, 1.8827698146898157, 2.1679483942963724, 2.341909527054047]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.595703125, 'crossentropy': 1.7598317861557007})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 2.5023627281188965})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 2.644834518432617})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 3.2109293937683105})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 3.173258066177368})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 3.4238901138305664})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 3.228402614593506})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 3.8358101844787598})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 3.3138184547424316})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 4.149706840515137})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 3.8220057487487793})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 4.041794776916504})
store['active_learning_steps'][19]['training']['best_epoch']=9
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.6199, 'crossentropy': 3.708821875}
store['active_learning_steps'][19]['eval_training']={}
store['active_learning_steps'][19]['eval_training']['epochs']=[]
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 1.6717817783355713})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 2.0219106674194336})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 1.9321057796478271})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 1.970930814743042})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 1.893564224243164})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 1.8330426216125488})
store['active_learning_steps'][19]['eval_training']['best_epoch']=3
store['active_learning_steps'][19]['acquisition']={'indices': [['ood', 47276], ['id', 55453], ['id', 21487], ['ood', 45885], ['id', 40538]], 'labels': [-1, 8, 5, -1, 5], 'scores': [1.122158221938907, 1.8443464002569527, 2.4077288294360155, 2.784497492608981, 2.999933400498257]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 1.6196866035461426})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 2.2140188217163086})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 2.5238687992095947})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 2.876023530960083})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 2.5692989826202393})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 2.9314846992492676})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 3.155351161956787})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 3.2178871631622314})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 3.305377960205078})
store['active_learning_steps'][20]['training']['best_epoch']=6
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.6525, 'crossentropy': 3.1331677734375}
store['active_learning_steps'][20]['eval_training']={}
store['active_learning_steps'][20]['eval_training']['epochs']=[]
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 1.6163421869277954})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 2.3054146766662598})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 2.0237584114074707})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 2.1180922985076904})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 2.053225040435791})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 1.9619759321212769})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 1.987058401107788})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 1.9610915184020996})
store['active_learning_steps'][20]['eval_training']['best_epoch']=8
store['active_learning_steps'][20]['acquisition']={'indices': [['ood', 42585], ['ood', 48135], ['ood', 17797], ['ood', 11621], ['ood', 43648]], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.9205089506264468, 1.647602413491406, 2.2128299267441642, 2.5824038981421142, 2.8002693513730508]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 1.8222408294677734})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 2.426262855529785})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 2.6762428283691406})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 2.8721370697021484})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 3.1897988319396973})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 3.117859363555908})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 3.116333484649658})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 3.5130839347839355})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 3.3472728729248047})
store['active_learning_steps'][21]['training']['best_epoch']=6
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.6392, 'crossentropy': 3.18278203125}
store['active_learning_steps'][21]['eval_training']={}
store['active_learning_steps'][21]['eval_training']['epochs']=[]
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 1.6797857284545898})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 1.8719780445098877})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 1.8143351078033447})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 1.8976727724075317})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 1.725425124168396})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 1.8276586532592773})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 1.7079464197158813})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 1.7766432762145996})
store['active_learning_steps'][21]['eval_training']['best_epoch']=5
store['active_learning_steps'][21]['acquisition']={'indices': [['ood', 6767], ['ood', 11074], ['ood', 16043], ['id', 3751], ['id', 35788]], 'labels': [-1, -1, -1, 4, 3], 'scores': [1.0140732632257965, 1.6704640207287453, 2.1106990166730952, 2.450556359581705, 2.6549610224575066]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 1.5590910911560059})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 2.1532864570617676})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 2.501478672027588})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 2.35988712310791})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 3.111584186553955})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 2.949970245361328})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 3.166639566421509})
store['active_learning_steps'][22]['training']['best_epoch']=4
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.642, 'crossentropy': 2.7069083984375}
store['active_learning_steps'][22]['eval_training']={}
store['active_learning_steps'][22]['eval_training']['epochs']=[]
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 1.4757331609725952})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 1.6454353332519531})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 1.508342981338501})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 1.4972991943359375})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 1.4655802249908447})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 1.371985912322998})
store['active_learning_steps'][22]['eval_training']['best_epoch']=6
store['active_learning_steps'][22]['acquisition']={'indices': [['ood', 27837], ['ood', 48239], ['ood', 29022], ['id', 52816], ['ood', 38520]], 'labels': [-1, -1, -1, 5, -1], 'scores': [0.8882059597136478, 1.603626656651505, 2.0542564005890704, 2.3453253888518617, 2.545029961478925]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 1.413682460784912})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 1.915952444076538})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 2.2249884605407715})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 2.542707920074463})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 2.6915581226348877})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 2.6723380088806152})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 3.047698974609375})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 2.981419563293457})
store['active_learning_steps'][23]['training']['best_epoch']=5
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.6339, 'crossentropy': 2.844255078125}
store['active_learning_steps'][23]['eval_training']={}
store['active_learning_steps'][23]['eval_training']['epochs']=[]
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 1.3871829509735107})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 1.5571589469909668})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 1.4408249855041504})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 1.4482510089874268})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 1.5701607465744019})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 1.5438084602355957})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 1.453115463256836})
store['active_learning_steps'][23]['eval_training']['best_epoch']=4
store['active_learning_steps'][23]['acquisition']={'indices': [['ood', 50280], ['ood', 4829], ['ood', 40447], ['ood', 7102], ['id', 55277]], 'labels': [-1, -1, -1, -1, 3], 'scores': [1.0062224555519057, 1.8392719880709072, 2.344599567300806, 2.6263444260633197, 2.7720696842260746]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 1.3973617553710938})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 2.1117682456970215})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 2.356300115585327})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 2.375046968460083})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 2.5880508422851562})
store['active_learning_steps'][24]['training']['best_epoch']=2
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.6327, 'crossentropy': 2.0802513671875}
store['active_learning_steps'][24]['eval_training']={}
store['active_learning_steps'][24]['eval_training']['epochs']=[]
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 1.3252079486846924})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 1.2945606708526611})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 1.2954018115997314})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 1.3067784309387207})
store['active_learning_steps'][24]['eval_training']['best_epoch']=3
store['active_learning_steps'][24]['acquisition']={'indices': [['ood', 12758], ['ood', 31095], ['ood', 48704], ['id', 53015], ['ood', 42119]], 'labels': [-1, -1, -1, 0, -1], 'scores': [0.8974212843043052, 1.5571259273803646, 2.0027177267772114, 2.3181176481346317, 2.491636475551759]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 1.6633687019348145})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 2.202052593231201})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 2.6541085243225098})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 2.499938488006592})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 3.033952474594116})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 2.745720386505127})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 2.7809386253356934})
store['active_learning_steps'][25]['training']['best_epoch']=4
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.6245, 'crossentropy': 2.7760640625}
store['active_learning_steps'][25]['eval_training']={}
store['active_learning_steps'][25]['eval_training']['epochs']=[]
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 1.316314458847046})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 1.497659683227539})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 1.4825961589813232})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 1.458221673965454})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 1.3387645483016968})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 1.443169355392456})
store['active_learning_steps'][25]['eval_training']['best_epoch']=5
store['active_learning_steps'][25]['acquisition']={'indices': [['ood', 4451], ['ood', 43993], ['ood', 55492], ['ood', 16785], ['id', 10026]], 'labels': [-1, -1, -1, -1, 1], 'scores': [0.8810998297904529, 1.5714194224926294, 2.1431054961875216, 2.5549807243157048, 2.821505158691539]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 1.5234407186508179})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 2.199906349182129})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 2.4451723098754883})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 2.7327651977539062})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 2.5422120094299316})
store['active_learning_steps'][26]['training']['best_epoch']=2
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.614, 'crossentropy': 2.2211587890625}
store['active_learning_steps'][26]['eval_training']={}
store['active_learning_steps'][26]['eval_training']['epochs']=[]
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 1.2758660316467285})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 1.391028642654419})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 1.4674150943756104})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 1.3131535053253174})
store['active_learning_steps'][26]['eval_training']['best_epoch']=2
store['active_learning_steps'][26]['acquisition']={'indices': [['ood', 46441], ['ood', 44059], ['ood', 47206], ['ood', 22225], ['ood', 23074]], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.7053374267699448, 1.28129255932547, 1.7408397752736362, 2.020357630571767, 2.1751788864469948]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 1.3667021989822388})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 1.8272068500518799})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 2.15971302986145})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 2.322667121887207})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 2.758812189102173})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 3.022679090499878})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 2.8286848068237305})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 3.378573417663574})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 3.0981802940368652})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 2.836564540863037})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 3.1523032188415527})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 3.3203721046447754})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 3.614647626876831})
store['active_learning_steps'][27]['training']['best_epoch']=10
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.6467, 'crossentropy': 3.113034375}
store['active_learning_steps'][27]['eval_training']={}
store['active_learning_steps'][27]['eval_training']['epochs']=[]
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 1.3673913478851318})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 1.6327905654907227})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 1.652174472808838})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 1.6211624145507812})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 1.7068530321121216})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 1.6606063842773438})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 1.5627386569976807})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 1.6169507503509521})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 1.5596040487289429})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 1.6331666707992554})
store['active_learning_steps'][27]['eval_training']['best_epoch']=7
store['active_learning_steps'][27]['acquisition']={'indices': [['ood', 3721], ['id', 14770], ['ood', 27202], ['ood', 8691], ['id', 17654]], 'labels': [-1, 8, -1, -1, 6], 'scores': [1.070192424532795, 1.8616283230232602, 2.465979830466645, 2.8683034312264635, 3.1094724541817667]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 1.4487721920013428})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 1.9058289527893066})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 2.012037515640259})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 2.1700820922851562})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 2.8921780586242676})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 2.5629091262817383})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 2.5879440307617188})
store['active_learning_steps'][28]['training']['best_epoch']=4
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.6423, 'crossentropy': 2.3207841796875}
store['active_learning_steps'][28]['eval_training']={}
store['active_learning_steps'][28]['eval_training']['epochs']=[]
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 1.334535837173462})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 1.5790324211120605})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 1.4326295852661133})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 1.4205914735794067})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 1.4753203392028809})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 1.378995418548584})
store['active_learning_steps'][28]['eval_training']['best_epoch']=5
store['active_learning_steps'][28]['acquisition']={'indices': [['ood', 22563], ['ood', 44412], ['ood', 25325], ['ood', 54757], ['ood', 57296]], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.8742830352142947, 1.51577318224861, 1.9870687620851415, 2.3033569870293746, 2.5357801248577094]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 1.3545241355895996})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 2.0486221313476562})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 2.423887252807617})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 2.5475261211395264})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 2.692244052886963})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 2.9962401390075684})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 2.9366180896759033})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 3.007884979248047})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 3.081173896789551})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 3.390029191970825})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 2.9676578044891357})
store['active_learning_steps'][29]['training']['best_epoch']=8
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.6476, 'crossentropy': 3.024836328125}
store['active_learning_steps'][29]['eval_training']={}
store['active_learning_steps'][29]['eval_training']['epochs']=[]
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.58984375, 'crossentropy': 1.5047913789749146})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 1.7492878437042236})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 1.6245191097259521})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 1.6859769821166992})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 1.7562077045440674})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 1.6747701168060303})
store['active_learning_steps'][29]['eval_training']['best_epoch']=3
store['active_learning_steps'][29]['acquisition']={'indices': [['ood', 51346], ['ood', 3294], ['ood', 53612], ['ood', 11960], ['ood', 45448]], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.927294309815141, 1.7375430618349696, 2.27880093341658, 2.576788050568286, 2.7450410086583243]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 1.2701244354248047})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 1.7476530075073242})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 2.1510281562805176})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 2.2764081954956055})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 2.388216733932495})
store['active_learning_steps'][30]['training']['best_epoch']=2
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.6412, 'crossentropy': 1.7959970703125}
store['active_learning_steps'][30]['eval_training']={}
store['active_learning_steps'][30]['eval_training']['epochs']=[]
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 1.2166125774383545})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 1.2534655332565308})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 1.1474970579147339})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 1.1861777305603027})
store['active_learning_steps'][30]['eval_training']['best_epoch']=4
store['active_learning_steps'][30]['acquisition']={'indices': [['ood', 50514], ['ood', 34497], ['ood', 39304], ['ood', 39738], ['ood', 49448]], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.7860563728373184, 1.4404860008947633, 1.9043587478097566, 2.2113586385856596, 2.3794865096413567]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 1.487668514251709})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 1.9354289770126343})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 2.0550358295440674})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 2.4037094116210938})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 2.350728988647461})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 2.875347137451172})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 3.1153180599212646})
store['active_learning_steps'][31]['training']['best_epoch']=4
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.6207, 'crossentropy': 2.6374234375}
store['active_learning_steps'][31]['eval_training']={}
store['active_learning_steps'][31]['eval_training']['epochs']=[]
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 1.2857823371887207})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 1.382742166519165})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 1.579421043395996})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 1.5428578853607178})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 1.5254521369934082})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 1.4945635795593262})
store['active_learning_steps'][31]['eval_training']['best_epoch']=6
store['active_learning_steps'][31]['acquisition']={'indices': [['ood', 9386], ['ood', 2502], ['id', 28830], ['ood', 28251], ['id', 36045]], 'labels': [-1, -1, 9, -1, 2], 'scores': [0.8905410732619843, 1.4965765094503682, 1.9453449084293117, 2.2368840321696712, 2.4165721341886934]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 1.4422340393066406})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 2.060774803161621})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 2.378418445587158})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 3.0710062980651855})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 3.113630771636963})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 3.5285229682922363})
store['active_learning_steps'][32]['training']['best_epoch']=3
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.611, 'crossentropy': 2.5922654296875}
store['active_learning_steps'][32]['eval_training']={}
store['active_learning_steps'][32]['eval_training']['epochs']=[]
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 1.3476924896240234})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 1.4521303176879883})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 1.5406341552734375})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 1.479745626449585})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 1.386448860168457})
store['active_learning_steps'][32]['eval_training']['best_epoch']=5
store['active_learning_steps'][32]['acquisition']={'indices': [['ood', 8001], ['ood', 56348], ['ood', 11600], ['ood', 14101], ['ood', 6906]], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.9899771963227929, 1.8276623345162066, 2.4391117347046776, 2.797728330813587, 3.003285402739344]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 1.5122616291046143})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.5966796875, 'crossentropy': 2.0090601444244385})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 2.2691290378570557})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 2.452084541320801})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 2.700333833694458})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 2.9825806617736816})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 3.1138687133789062})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 3.0533087253570557})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 3.439088821411133})
store['active_learning_steps'][33]['training']['best_epoch']=6
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.6365, 'crossentropy': 2.983611328125}
store['active_learning_steps'][33]['eval_training']={}
store['active_learning_steps'][33]['eval_training']['epochs']=[]
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 1.495086908340454})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 1.543750524520874})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 1.7099518775939941})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 1.646083116531372})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 1.7605855464935303})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 1.6868774890899658})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 1.5888913869857788})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 1.5739914178848267})
store['active_learning_steps'][33]['eval_training']['best_epoch']=8
store['active_learning_steps'][33]['acquisition']={'indices': [['ood', 43010], ['ood', 56427], ['ood', 56866], ['id', 57069], ['ood', 55206]], 'labels': [-1, -1, -1, 5, -1], 'scores': [0.9963075353145424, 1.831701696770753, 2.5087096935522317, 2.978181028263127, 3.203478350375267]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 1.544316053390503})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 1.7747206687927246})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 2.2116518020629883})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 2.222062826156616})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 2.8214612007141113})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 2.6518306732177734})
store['active_learning_steps'][34]['training']['best_epoch']=3
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.6384, 'crossentropy': 2.171027734375}
store['active_learning_steps'][34]['eval_training']={}
store['active_learning_steps'][34]['eval_training']['epochs']=[]
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 1.2554051876068115})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 1.4050648212432861})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 1.4796359539031982})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 1.400333046913147})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 1.3458473682403564})
store['active_learning_steps'][34]['eval_training']['best_epoch']=5
store['active_learning_steps'][34]['acquisition']={'indices': [['ood', 30552], ['ood', 46260], ['ood', 42198], ['id', 23569], ['ood', 53639]], 'labels': [-1, -1, -1, 3, -1], 'scores': [0.830247073506557, 1.5097295316933452, 2.0108307311710574, 2.382751987100625, 2.594621044294286]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 1.4570419788360596})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 1.6687288284301758})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 2.0583882331848145})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 2.2364540100097656})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 2.566317081451416})
store['active_learning_steps'][35]['training']['best_epoch']=2
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.6392, 'crossentropy': 1.748773046875}
store['active_learning_steps'][35]['eval_training']={}
store['active_learning_steps'][35]['eval_training']['epochs']=[]
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 1.396608591079712})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 1.2411150932312012})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 1.2012617588043213})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 1.1544021368026733})
store['active_learning_steps'][35]['eval_training']['best_epoch']=4
store['active_learning_steps'][35]['acquisition']={'indices': [['ood', 36946], ['ood', 26382], ['ood', 11922], ['ood', 35594], ['id', 39279]], 'labels': [-1, -1, -1, -1, 2], 'scores': [0.8632924896768328, 1.5425619688034877, 1.942400756334819, 2.2008552015559992, 2.3459103306894207]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 1.383580207824707})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 1.8760552406311035})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 2.3740453720092773})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 2.389880657196045})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 2.8136329650878906})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 2.610866069793701})
store['active_learning_steps'][36]['training']['best_epoch']=3
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.6117, 'crossentropy': 2.4368876953125}
store['active_learning_steps'][36]['eval_training']={}
store['active_learning_steps'][36]['eval_training']['epochs']=[]
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 1.2896050214767456})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 1.3506865501403809})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 1.3612849712371826})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 1.3748960494995117})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 1.314793586730957})
store['active_learning_steps'][36]['eval_training']['best_epoch']=2
store['active_learning_steps'][36]['acquisition']={'indices': [['ood', 11191], ['ood', 37281], ['ood', 25333], ['ood', 45801], ['ood', 50885]], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.8578760195007542, 1.500302008559264, 2.0014047753818094, 2.288468326575739, 2.4464511349770572]}
store['active_learning_steps'].append({})
store['active_learning_steps'][37]['training']={}
store['active_learning_steps'][37]['training']['epochs']=[]
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 1.7607421875})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 2.073617935180664})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 2.7819504737854004})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 2.8682894706726074})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 3.1428346633911133})
store['active_learning_steps'][37]['training']['best_epoch']=2
store['active_learning_steps'][37]['evaluation_metrics']={'accuracy': 0.6007, 'crossentropy': 2.18623046875}
store['active_learning_steps'][37]['eval_training']={}
store['active_learning_steps'][37]['eval_training']['epochs']=[]
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.58984375, 'crossentropy': 1.2794842720031738})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 1.4058995246887207})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 1.303504467010498})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 1.2563793659210205})
store['active_learning_steps'][37]['eval_training']['best_epoch']=4
store['active_learning_steps'][37]['acquisition']={'indices': [['ood', 59618], ['ood', 25311], ['ood', 17870], ['ood', 26343], ['id', 45263]], 'labels': [-1, -1, -1, -1, 5], 'scores': [0.8608177718226775, 1.5649842084061434, 2.037947425130276, 2.326728567487052, 2.5055856815375517]}
store['active_learning_steps'].append({})
store['active_learning_steps'][38]['training']={}
store['active_learning_steps'][38]['training']['epochs']=[]
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.6005859375, 'crossentropy': 1.489890694618225})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 2.452540397644043})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 2.604640007019043})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 2.6002604961395264})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.599609375, 'crossentropy': 3.252002477645874})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 3.2048206329345703})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 3.18039608001709})
store['active_learning_steps'][38]['training']['best_epoch']=4
store['active_learning_steps'][38]['evaluation_metrics']={'accuracy': 0.6108, 'crossentropy': 2.9782595703125}
store['active_learning_steps'][38]['eval_training']={}
store['active_learning_steps'][38]['eval_training']['epochs']=[]
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 1.3954622745513916})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 1.5344154834747314})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 1.4422519207000732})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 1.4709141254425049})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 1.4891644716262817})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 1.360437035560608})
store['active_learning_steps'][38]['eval_training']['best_epoch']=3
store['active_learning_steps'][38]['acquisition']={'indices': [['ood', 20932], ['ood', 1380], ['ood', 13652], ['ood', 7280], ['ood', 20836]], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.9974722710110512, 1.7300492219814958, 2.3370559958724364, 2.705532704037327, 2.933965891272418]}
store['active_learning_steps'].append({})
store['active_learning_steps'][39]['training']={}
store['active_learning_steps'][39]['training']['epochs']=[]
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.587890625, 'crossentropy': 1.4307308197021484})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 1.8171613216400146})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 2.3848671913146973})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 2.8801393508911133})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 3.0578994750976562})
store['active_learning_steps'][39]['training']['best_epoch']=2
store['active_learning_steps'][39]['evaluation_metrics']={'accuracy': 0.6134, 'crossentropy': 1.9503609375}
store['active_learning_steps'][39]['eval_training']={}
store['active_learning_steps'][39]['eval_training']['epochs']=[]
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 1.2458291053771973})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 1.235607385635376})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 1.2167009115219116})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 1.2080984115600586})
store['active_learning_steps'][39]['eval_training']['best_epoch']=2
store['active_learning_steps'][39]['acquisition']={'indices': [['ood', 31083], ['ood', 34285], ['id', 35279], ['ood', 43898], ['ood', 28863]], 'labels': [-1, -1, 0, -1, -1], 'scores': [0.7431054852200949, 1.2345881393485378, 1.6036972773662939, 1.8913051367750358, 2.0947946043191505]}
store['active_learning_steps'].append({})
store['active_learning_steps'][40]['training']={}
store['active_learning_steps'][40]['training']['epochs']=[]
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 1.6503111124038696})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 2.2104179859161377})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 2.552600622177124})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 2.888162851333618})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 3.478271722793579})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 3.603349208831787})
store['active_learning_steps'][40]['training']['best_epoch']=3
store['active_learning_steps'][40]['evaluation_metrics']={'accuracy': 0.6107, 'crossentropy': 2.9682046875}
store['active_learning_steps'][40]['eval_training']={}
store['active_learning_steps'][40]['eval_training']['epochs']=[]
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.5927734375, 'crossentropy': 1.3982980251312256})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 1.4364304542541504})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 1.421709656715393})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 1.4729766845703125})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 1.4534382820129395})
store['active_learning_steps'][40]['eval_training']['best_epoch']=5
store['active_learning_steps'][40]['acquisition']={'indices': [['ood', 52392], ['ood', 12922], ['id', 35985], ['ood', 25317], ['ood', 1593]], 'labels': [-1, -1, 5, -1, -1], 'scores': [0.8837148287241523, 1.563860402049447, 2.1060552780578545, 2.4916580802921953, 2.7487667563920644]}
store['active_learning_steps'].append({})
store['active_learning_steps'][41]['training']={}
store['active_learning_steps'][41]['training']['epochs']=[]
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 1.424609899520874})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 2.101388454437256})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 2.387751579284668})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 2.2009987831115723})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 2.5180540084838867})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 2.873110294342041})
store['active_learning_steps'][41]['training']['best_epoch']=3
store['active_learning_steps'][41]['evaluation_metrics']={'accuracy': 0.6403, 'crossentropy': 2.315437890625}
store['active_learning_steps'][41]['eval_training']={}
store['active_learning_steps'][41]['eval_training']['epochs']=[]
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.599609375, 'crossentropy': 1.4333610534667969})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 1.4425439834594727})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 1.5302234888076782})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 1.5309786796569824})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 1.4873000383377075})
store['active_learning_steps'][41]['eval_training']['best_epoch']=3
store['active_learning_steps'][41]['acquisition']={'indices': [['ood', 34924], ['ood', 43542], ['id', 16469], ['ood', 53503], ['ood', 28806]], 'labels': [-1, -1, 2, -1, -1], 'scores': [1.0765435334188493, 1.8411531056272543, 2.338871855845098, 2.6396466552022737, 2.8061300487735044]}
store['active_learning_steps'].append({})
store['active_learning_steps'][42]['training']={}
store['active_learning_steps'][42]['training']['epochs']=[]
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 1.4059315919876099})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 1.9840404987335205})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 2.2078819274902344})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 2.520578384399414})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 2.793889045715332})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 2.9050774574279785})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 2.786555767059326})
store['active_learning_steps'][42]['training']['best_epoch']=4
store['active_learning_steps'][42]['evaluation_metrics']={'accuracy': 0.6272, 'crossentropy': 2.550701953125}
store['active_learning_steps'][42]['eval_training']={}
store['active_learning_steps'][42]['eval_training']['epochs']=[]
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 1.2960375547409058})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 1.5206552743911743})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 1.57163667678833})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 1.4361846446990967})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 1.4541575908660889})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 1.435668706893921})
store['active_learning_steps'][42]['eval_training']['best_epoch']=6
store['active_learning_steps'][42]['acquisition']={'indices': [['ood', 19431], ['ood', 44383], ['ood', 48016], ['ood', 12354], ['id', 25784]], 'labels': [-1, -1, -1, -1, 8], 'scores': [0.8599488819633456, 1.5273934376751457, 2.076425633862903, 2.413268782443835, 2.6231414592004056]}
store['active_learning_steps'].append({})
store['active_learning_steps'][43]['training']={}
store['active_learning_steps'][43]['training']['epochs']=[]
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 1.3277795314788818})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 1.6739965677261353})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 2.254873514175415})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 2.686687469482422})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 2.5759482383728027})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 2.681705951690674})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 2.612532615661621})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 3.229112148284912})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 2.6353559494018555})
store['active_learning_steps'][43]['training']['best_epoch']=6
store['active_learning_steps'][43]['evaluation_metrics']={'accuracy': 0.6363, 'crossentropy': 2.804267578125}
store['active_learning_steps'][43]['eval_training']={}
store['active_learning_steps'][43]['eval_training']['epochs']=[]
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 1.3416856527328491})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 1.556016445159912})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 1.708564281463623})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 1.717224359512329})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 1.6390202045440674})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 1.665069818496704})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 1.5422859191894531})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 1.535051703453064})
store['active_learning_steps'][43]['eval_training']['best_epoch']=8
store['active_learning_steps'][43]['acquisition']={'indices': [['ood', 9210], ['ood', 9402], ['ood', 6242], ['ood', 17501], ['ood', 14031]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.0483542832161525, 1.8803533070267289, 2.542285306354365, 2.995283157399195, 3.258105032071401]}
store['active_learning_steps'].append({})
store['active_learning_steps'][44]['training']={}
store['active_learning_steps'][44]['training']['epochs']=[]
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 1.3683276176452637})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 1.9127411842346191})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 2.3173024654388428})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 2.434610366821289})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 2.5313360691070557})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 2.6539273262023926})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 2.925617218017578})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 2.727419137954712})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 3.2396492958068848})
store['active_learning_steps'][44]['training']['best_epoch']=6
store['active_learning_steps'][44]['evaluation_metrics']={'accuracy': 0.6422, 'crossentropy': 2.8087947265625}
store['active_learning_steps'][44]['eval_training']={}
store['active_learning_steps'][44]['eval_training']['epochs']=[]
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 1.3153438568115234})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 1.4367077350616455})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 1.4598064422607422})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 1.5242178440093994})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 1.5282464027404785})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 1.519234299659729})
store['active_learning_steps'][44]['eval_training']['best_epoch']=3
store['active_learning_steps'][44]['acquisition']={'indices': [['ood', 2389], ['ood', 36296], ['ood', 59589], ['id', 1882], ['id', 17030]], 'labels': [-1, -1, -1, 2, 5], 'scores': [0.9062715739797029, 1.618453059611235, 2.1105317634836225, 2.3934390511182944, 2.5278090786856797]}
store['active_learning_steps'].append({})
store['active_learning_steps'][45]['training']={}
store['active_learning_steps'][45]['training']['epochs']=[]
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 1.4687267541885376})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 1.9664064645767212})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 1.9701600074768066})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 2.5214860439300537})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 2.8340249061584473})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 2.9309492111206055})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 3.626220703125})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 3.285830020904541})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 3.448561191558838})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 3.4384143352508545})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 3.398480176925659})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 3.3602781295776367})
store['active_learning_steps'][45]['training']['best_epoch']=9
store['active_learning_steps'][45]['evaluation_metrics']={'accuracy': 0.6258, 'crossentropy': 3.663807421875}
store['active_learning_steps'][45]['eval_training']={}
store['active_learning_steps'][45]['eval_training']['epochs']=[]
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 1.2977678775787354})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 1.633138656616211})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 1.6966478824615479})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 1.5957120656967163})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 1.6641368865966797})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 1.6573963165283203})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 1.7000877857208252})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 1.6535193920135498})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 1.7372925281524658})
store['active_learning_steps'][45]['eval_training']['best_epoch']=6
store['active_learning_steps'][45]['acquisition']={'indices': [['ood', 10679], ['ood', 56258], ['ood', 47155], ['id', 34535], ['ood', 44712]], 'labels': [-1, -1, -1, 6, -1], 'scores': [1.0330275550654593, 1.928524062507307, 2.635193931782257, 3.085186279859746, 3.31449680884912]}
store['active_learning_steps'].append({})
store['active_learning_steps'][46]['training']={}
store['active_learning_steps'][46]['training']['epochs']=[]
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.603515625, 'crossentropy': 1.3653485774993896})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 1.9438560009002686})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 2.306757926940918})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 2.4250059127807617})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 2.3462233543395996})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 2.83306884765625})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 2.5313823223114014})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 3.20358943939209})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 3.043893814086914})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 3.1449673175811768})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 2.8179166316986084})
store['active_learning_steps'][46]['training']['best_epoch']=8
store['active_learning_steps'][46]['evaluation_metrics']={'accuracy': 0.6383, 'crossentropy': 3.295355078125}
store['active_learning_steps'][46]['eval_training']={}
store['active_learning_steps'][46]['eval_training']['epochs']=[]
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.5908203125, 'crossentropy': 1.419708490371704})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 1.6097052097320557})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 1.7324213981628418})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 1.8209843635559082})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 1.7375493049621582})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 1.802689790725708})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 1.9167366027832031})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 1.8211629390716553})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 1.815481424331665})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 1.7131465673446655})
store['active_learning_steps'][46]['eval_training']['best_epoch']=8
store['active_learning_steps'][46]['acquisition']={'indices': [['ood', 28158], ['ood', 13374], ['ood', 35663], ['ood', 40252], ['id', 54639]], 'labels': [-1, -1, -1, -1, 6], 'scores': [0.8877487275481734, 1.6392182314510813, 2.1527736880127417, 2.5015817269493796, 2.7116263086631163]}
store['active_learning_steps'].append({})
store['active_learning_steps'][47]['training']={}
store['active_learning_steps'][47]['training']['epochs']=[]
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 1.2895876169204712})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.599609375, 'crossentropy': 1.8920435905456543})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 2.252380847930908})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 2.1794958114624023})
store['active_learning_steps'][47]['training']['best_epoch']=1
store['active_learning_steps'][47]['evaluation_metrics']={'accuracy': 0.6341, 'crossentropy': 1.26918046875}
store['active_learning_steps'][47]['eval_training']={}
store['active_learning_steps'][47]['eval_training']['epochs']=[]
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 1.2190701961517334})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 1.0890498161315918})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 1.0932502746582031})
store['active_learning_steps'][47]['eval_training']['best_epoch']=2
store['active_learning_steps'][47]['acquisition']={'indices': [['ood', 6033], ['ood', 29017], ['ood', 2652], ['id', 3457], ['id', 19767]], 'labels': [-1, -1, -1, 8, 1], 'scores': [0.7126723653058853, 1.181813617434393, 1.5418023718703235, 1.8305866624954312, 2.0556112499737615]}
store['active_learning_steps'].append({})
store['active_learning_steps'][48]['training']={}
store['active_learning_steps'][48]['training']['epochs']=[]
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 1.3239202499389648})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 1.691705584526062})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 2.2382054328918457})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 2.547639846801758})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 2.3917856216430664})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 2.8176445960998535})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 2.976353406906128})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 2.9583740234375})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 2.8397159576416016})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 3.0419626235961914})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 3.1986608505249023})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 2.917774200439453})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 3.066507577896118})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 3.1870946884155273})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 3.2066144943237305})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 3.1708521842956543})
store['active_learning_steps'][48]['training']['best_epoch']=13
store['active_learning_steps'][48]['evaluation_metrics']={'accuracy': 0.6445, 'crossentropy': 3.3018921875}
store['active_learning_steps'][48]['eval_training']={}
store['active_learning_steps'][48]['eval_training']['epochs']=[]
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.5947265625, 'crossentropy': 1.4356184005737305})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 1.626455307006836})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 1.8977479934692383})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 1.7274982929229736})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 1.8776233196258545})
store['active_learning_steps'][48]['eval_training']['best_epoch']=2
store['active_learning_steps'][48]['acquisition']={'indices': [['ood', 17140], ['id', 33043], ['id', 10794], ['ood', 39855], ['id', 57132]], 'labels': [-1, 0, 5, -1, 0], 'scores': [0.8163779146732519, 1.5426421055351855, 2.0908220280780334, 2.4540834946561576, 2.6470683599596248]}
store['active_learning_steps'].append({})
store['active_learning_steps'][49]['training']={}
store['active_learning_steps'][49]['training']['epochs']=[]
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 1.2682576179504395})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 1.797139286994934})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 2.0347650051116943})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 2.3659005165100098})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 2.4715261459350586})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 2.818410873413086})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 3.0003910064697266})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 3.0870442390441895})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 2.7162344455718994})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 3.055274486541748})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 2.8862245082855225})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 3.110541343688965})
store['active_learning_steps'][49]['training']['best_epoch']=9
store['active_learning_steps'][49]['evaluation_metrics']={'accuracy': 0.6393, 'crossentropy': 2.80274296875}
store['active_learning_steps'][49]['eval_training']={}
store['active_learning_steps'][49]['eval_training']['epochs']=[]
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 1.2718148231506348})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 1.4531750679016113})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 1.4715547561645508})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 1.4215333461761475})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 1.446771264076233})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 1.4490578174591064})
store['active_learning_steps'][49]['eval_training']['best_epoch']=3
store['active_learning_steps'][49]['acquisition']={'indices': [['ood', 1967], ['ood', 43648], ['ood', 19869], ['ood', 50390], ['ood', 52919]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.0006349376682888, 1.8699157300222873, 2.466517379321263, 2.858640049618245, 3.0977248915673066]}
store['active_learning_steps'].append({})
store['active_learning_steps'][50]['training']={}
store['active_learning_steps'][50]['training']['epochs']=[]
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.5751953125, 'crossentropy': 1.390582799911499})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 1.6399636268615723})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 2.159599542617798})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 2.2263927459716797})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 2.6491379737854004})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 2.437610626220703})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 2.909788131713867})
store['active_learning_steps'][50]['training']['best_epoch']=4
store['active_learning_steps'][50]['evaluation_metrics']={'accuracy': 0.6382, 'crossentropy': 2.3213091796875}
store['active_learning_steps'][50]['eval_training']={}
store['active_learning_steps'][50]['eval_training']['epochs']=[]
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 1.2637443542480469})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 1.2480891942977905})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 1.3536934852600098})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 1.2932826280593872})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 1.2362093925476074})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 1.2582271099090576})
store['active_learning_steps'][50]['eval_training']['best_epoch']=6
store['active_learning_steps'][50]['acquisition']={'indices': [['ood', 46441], ['ood', 21692], ['ood', 15784], ['ood', 54433], ['id', 27235]], 'labels': [-1, -1, -1, -1, 5], 'scores': [1.0297443285310088, 1.7757825812302734, 2.306690109811238, 2.6386901634564337, 2.8477573159509992]}
store['active_learning_steps'].append({})
store['active_learning_steps'][51]['training']={}
store['active_learning_steps'][51]['training']['epochs']=[]
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 1.3576478958129883})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 1.669435977935791})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 1.9824143648147583})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 2.137012004852295})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 2.2079100608825684})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 2.503817558288574})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 2.4312844276428223})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 2.2657060623168945})
store['active_learning_steps'][51]['training']['best_epoch']=5
store['active_learning_steps'][51]['evaluation_metrics']={'accuracy': 0.6511, 'crossentropy': 2.3492044921875}
store['active_learning_steps'][51]['eval_training']={}
store['active_learning_steps'][51]['eval_training']['epochs']=[]
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 1.3577384948730469})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 1.3594179153442383})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 1.527877688407898})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 1.5092463493347168})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 1.4990522861480713})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 1.4215550422668457})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 1.344542384147644})
store['active_learning_steps'][51]['eval_training']['best_epoch']=7
store['active_learning_steps'][51]['acquisition']={'indices': [['ood', 51310], ['ood', 37044], ['ood', 53956], ['ood', 5140], ['id', 56561]], 'labels': [-1, -1, -1, -1, 2], 'scores': [0.9038114616174235, 1.5737710770317876, 2.0858090119770143, 2.4294675957415093, 2.635875906490588]}
store['active_learning_steps'].append({})
store['active_learning_steps'][52]['training']={}
store['active_learning_steps'][52]['training']['epochs']=[]
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 1.4067614078521729})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 1.798309087753296})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 2.040043354034424})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 2.265307903289795})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 2.3065645694732666})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 2.5037550926208496})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 2.8812472820281982})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 3.0345616340637207})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 2.7447094917297363})
store['active_learning_steps'][52]['training']['best_epoch']=6
store['active_learning_steps'][52]['evaluation_metrics']={'accuracy': 0.6389, 'crossentropy': 2.794855078125}
store['active_learning_steps'][52]['eval_training']={}
store['active_learning_steps'][52]['eval_training']['epochs']=[]
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 1.2880196571350098})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 1.414330005645752})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 1.4950437545776367})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 1.3698694705963135})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 1.501774549484253})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 1.4849001169204712})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 1.3816876411437988})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 1.5145683288574219})
store['active_learning_steps'][52]['eval_training']['best_epoch']=8
store['active_learning_steps'][52]['acquisition']={'indices': [['ood', 28423], ['ood', 28285], ['ood', 15718], ['ood', 6447], ['ood', 18868]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.0786207174864022, 1.8620293315646315, 2.4485270837514364, 2.806487151319205, 3.0098071095295444]}
store['active_learning_steps'].append({})
store['active_learning_steps'][53]['training']={}
store['active_learning_steps'][53]['training']['epochs']=[]
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 1.3659491539001465})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 1.9131512641906738})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 2.0653834342956543})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 2.414184093475342})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 2.430140495300293})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 2.3010001182556152})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 2.7713143825531006})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 2.8449883460998535})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 2.9632973670959473})
store['active_learning_steps'][53]['training']['best_epoch']=6
store['active_learning_steps'][53]['evaluation_metrics']={'accuracy': 0.6329, 'crossentropy': 2.725193359375}
store['active_learning_steps'][53]['eval_training']={}
store['active_learning_steps'][53]['eval_training']['epochs']=[]
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.59765625, 'crossentropy': 1.3068557977676392})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 1.3401552438735962})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 1.4867594242095947})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 1.5965020656585693})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 1.4636094570159912})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 1.4095124006271362})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 1.3918118476867676})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 1.401198148727417})
store['active_learning_steps'][53]['eval_training']['best_epoch']=6
store['active_learning_steps'][53]['acquisition']={'indices': [['ood', 5596], ['ood', 15205], ['ood', 12235], ['ood', 10497], ['ood', 986]], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.9265052015241262, 1.730361529335994, 2.261720775934186, 2.6591636728312236, 2.937093241838949]}
store['active_learning_steps'].append({})
store['active_learning_steps'][54]['training']={}
store['active_learning_steps'][54]['training']['epochs']=[]
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.578125, 'crossentropy': 1.310133934020996})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 1.6542558670043945})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.6005859375, 'crossentropy': 1.946737289428711})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 2.2661614418029785})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 2.413008451461792})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 2.7144060134887695})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 3.1196608543395996})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 2.9862923622131348})
store['active_learning_steps'][54]['training']['best_epoch']=5
store['active_learning_steps'][54]['evaluation_metrics']={'accuracy': 0.6426, 'crossentropy': 2.48027265625}
