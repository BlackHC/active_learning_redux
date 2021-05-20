store = {}
store['timestamp']=1621477916
store['cmdline']=['/home/kell4989/git/active_learning_redux/batchbald_redux/ood_experiment.py', '--id=49']
store['commit']='8a2cf4fb40ce306533b4e439b08268c53f009a3b'
store['github_url']='8a2cf4fb40ce306533b4e439b08268c53f009a3b'
store['experiment']='/home/kell4989/git/active_learning_redux/batchbald_redux/ood_experiment.py'
store['job_id']=49
store['worker_id']=49
store['num_workers']=80
store['config']={'seed': 1286, 'uniform_ood': True, 'id_dataset_type': 'batchbald_redux.fast_mnist.FastFashionMNIST', 'ood_dataset_type': 'batchbald_redux.fast_mnist.FastMNIST', 'initial_training_set_size': 20, 'validation_set_size': 1024, 'evaluation_set_size': 16, 'id_repetitions': 1, 'ood_repetitions': 1, 'add_dataset_noise': False, 'validation_split_random_state': 0, 'acquisition_size': 5, 'max_training_set': 200, 'num_pool_samples': 100, 'num_validation_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'min_samples_per_epoch': 5056, 'acquisition_function': 'batchbald_redux.acquisition_functions.BatchEvalBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationEvalModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 8}
store['log']={}
store['dataset_info']={'training': "(FastFashionMNIST (train; 58976 samples) | one_hot_targets{'num_classes': 10}) + ('FastMNIST Train (60000 samples)' | uniform_targets{'num_classes': 10})", 'test': "'FastFashionMNIST Test (10000 samples)'"}
store['initial_training_set_indices']=[55573, 380, 12640, 44119, 30392, 58226, 43812, 52440, 3091, 29974, 49512, 46037, 53434, 22015, 37915, 52296, 8533, 58125, 22304, 35472]
store['evaluation_set_indices']=[42890, 14640, 45567, 52801, 53689, 801, 55187, 26479, 50997, 3792]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 2.3137927055358887})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 2.886263370513916})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 2.755542278289795})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 3.4018797874450684})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 3.483750581741333})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 3.6368508338928223})
store['active_learning_steps'][0]['training']['best_epoch']=3
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.6163, 'crossentropy': 3.080165625}
store['active_learning_steps'][0]['eval_training']={}
store['active_learning_steps'][0]['eval_training']['epochs']=[]
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 1.7635425329208374})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.591796875, 'crossentropy': 1.8365849256515503})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 1.8230829238891602})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.5966796875, 'crossentropy': 1.8735790252685547})
store['active_learning_steps'][0]['eval_training']['best_epoch']=1
store['active_learning_steps'][0]['acquisition']={'indices': [['id', 10791], ['id', 26947], ['id', 6169], ['id', 10992], ['id', 55511]], 'labels': [[0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.92663744015569, 1.6300239511311791, 2.1452145071720468, 2.4551851871021864, 2.6314135781195933]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.5849609375, 'crossentropy': 2.113612174987793})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.5888671875, 'crossentropy': 3.1045749187469482})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.5771484375, 'crossentropy': 3.900944232940674})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.587890625, 'crossentropy': 3.75101900100708})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.580078125, 'crossentropy': 4.11706018447876})
store['active_learning_steps'][1]['training']['best_epoch']=2
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.5784, 'crossentropy': 3.0830162109375}
store['active_learning_steps'][1]['eval_training']={}
store['active_learning_steps'][1]['eval_training']['epochs']=[]
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.5947265625, 'crossentropy': 1.774061918258667})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.578125, 'crossentropy': 1.961069107055664})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.58984375, 'crossentropy': 1.7251689434051514})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.5888671875, 'crossentropy': 1.7496081590652466})
store['active_learning_steps'][1]['eval_training']['best_epoch']=1
store['active_learning_steps'][1]['acquisition']={'indices': [['id', 25210], ['id', 3895], ['id', 5019], ['id', 31624], ['id', 21760]], 'labels': [[0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.5906648656681108, 1.0649534301439703, 1.4926366204317167, 1.8015183742294107, 2.0009124831711915]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.591796875, 'crossentropy': 1.695136547088623})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.5966796875, 'crossentropy': 2.4326937198638916})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 2.909359931945801})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 3.1637649536132812})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 3.0111379623413086})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.5966796875, 'crossentropy': 3.5154783725738525})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.5927734375, 'crossentropy': 3.8717830181121826})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.595703125, 'crossentropy': 3.465946674346924})
store['active_learning_steps'][2]['training']['best_epoch']=5
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.6056, 'crossentropy': 3.0806025390625}
store['active_learning_steps'][2]['eval_training']={}
store['active_learning_steps'][2]['eval_training']['epochs']=[]
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.6005859375, 'crossentropy': 1.6301188468933105})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 1.8524562120437622})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 1.8572062253952026})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.5966796875, 'crossentropy': 1.7025625705718994})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 1.870642900466919})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 1.7324485778808594})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 1.87588369846344})
store['active_learning_steps'][2]['eval_training']['best_epoch']=5
store['active_learning_steps'][2]['acquisition']={'indices': [['id', 58529], ['id', 23978], ['id', 57069], ['id', 15322], ['id', 55587]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6722993373351585, 1.1925821726062436, 1.6309181584508758, 1.978597418267913, 2.2274954197060204]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.580078125, 'crossentropy': 1.658637523651123})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 2.3969779014587402})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.5966796875, 'crossentropy': 2.8268673419952393})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.59375, 'crossentropy': 3.2615556716918945})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 3.411379814147949})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 3.676347255706787})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 3.3326892852783203})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.603515625, 'crossentropy': 3.2890961170196533})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 3.511354923248291})
store['active_learning_steps'][3]['training']['best_epoch']=6
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.6142, 'crossentropy': 3.38113515625}
store['active_learning_steps'][3]['eval_training']={}
store['active_learning_steps'][3]['eval_training']['epochs']=[]
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 1.4929075241088867})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 1.9565775394439697})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 2.035977840423584})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 1.9163458347320557})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 2.0737125873565674})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 1.881474256515503})
store['active_learning_steps'][3]['eval_training']['best_epoch']=3
store['active_learning_steps'][3]['acquisition']={'indices': [['id', 50879], ['id', 34535], ['id', 52889], ['id', 45785], ['id', 54073]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.7384489367335854, 1.4384474544761248, 1.967327147325271, 2.3593812490042576, 2.6543796778947826]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 1.3916306495666504})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 2.0046422481536865})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 2.162254810333252})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 2.561041831970215})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 2.664891242980957})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 2.9639694690704346})
store['active_learning_steps'][4]['training']['best_epoch']=3
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.6453, 'crossentropy': 2.237209765625}
store['active_learning_steps'][4]['eval_training']={}
store['active_learning_steps'][4]['eval_training']['epochs']=[]
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 1.407982349395752})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 1.4604982137680054})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 1.4228618144989014})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 1.3756349086761475})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 1.3391432762145996})
store['active_learning_steps'][4]['eval_training']['best_epoch']=5
store['active_learning_steps'][4]['acquisition']={'indices': [['id', 5513], ['id', 50898], ['id', 44], ['id', 56393], ['id', 50303]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5952750451568154, 1.1456584108908456, 1.5779800304398135, 1.9273144530474395, 2.210811309698072]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 1.3512892723083496})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 1.6225451231002808})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 2.150815725326538})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 2.319103479385376})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 2.7905526161193848})
store['active_learning_steps'][5]['training']['best_epoch']=2
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.6256, 'crossentropy': 1.7414140625}
store['active_learning_steps'][5]['eval_training']={}
store['active_learning_steps'][5]['eval_training']['epochs']=[]
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 1.2749216556549072})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 1.26937735080719})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 1.261606216430664})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 1.2511192560195923})
store['active_learning_steps'][5]['eval_training']['best_epoch']=2
store['active_learning_steps'][5]['acquisition']={'indices': [['id', 24842], ['id', 326], ['id', 21246], ['id', 17293], ['id', 931]], 'labels': [[0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5034277195618546, 0.9661585986626968, 1.370203910173359, 1.6719022160807109, 1.8899681144353782]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.578125, 'crossentropy': 1.3726320266723633})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 1.5609750747680664})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 2.179598808288574})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 2.153759717941284})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 2.72009539604187})
store['active_learning_steps'][6]['training']['best_epoch']=2
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.6272, 'crossentropy': 1.63836435546875}
store['active_learning_steps'][6]['eval_training']={}
store['active_learning_steps'][6]['eval_training']['epochs']=[]
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.5908203125, 'crossentropy': 1.3048436641693115})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 1.255421757698059})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 1.2586467266082764})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 1.200594186782837})
store['active_learning_steps'][6]['eval_training']['best_epoch']=2
store['active_learning_steps'][6]['acquisition']={'indices': [['id', 47230], ['id', 48056], ['id', 18112], ['id', 22583], ['id', 49603]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.3995387426167174, 0.7597604298163882, 1.0415684086002885, 1.2758887083041506, 1.472170622231224]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 1.3770372867584229})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 1.860640287399292})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 2.0989606380462646})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 2.462589740753174})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 2.5145795345306396})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 2.8537940979003906})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 2.728996753692627})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 2.8028407096862793})
store['active_learning_steps'][7]['training']['best_epoch']=5
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.6301, 'crossentropy': 2.53470859375}
store['active_learning_steps'][7]['eval_training']={}
store['active_learning_steps'][7]['eval_training']['epochs']=[]
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.580078125, 'crossentropy': 1.4886164665222168})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 1.5245368480682373})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.5986328125, 'crossentropy': 1.6994216442108154})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 1.603740930557251})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 1.5711594820022583})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 1.6027990579605103})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 1.463315486907959})
store['active_learning_steps'][7]['eval_training']['best_epoch']=5
store['active_learning_steps'][7]['acquisition']={'indices': [['id', 20410], ['id', 17005], ['id', 8276], ['id', 46826], ['id', 32992]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.5696522458948201, 1.035898990018575, 1.4680563470949544, 1.8176086550073665, 2.0849921924179435]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.587890625, 'crossentropy': 1.3761241436004639})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.603515625, 'crossentropy': 1.8362095355987549})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 2.3498473167419434})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 2.290133476257324})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 3.005953311920166})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 3.0774035453796387})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 3.0756497383117676})
store['active_learning_steps'][8]['training']['best_epoch']=4
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.6235, 'crossentropy': 2.41584375}
store['active_learning_steps'][8]['eval_training']={}
store['active_learning_steps'][8]['eval_training']['epochs']=[]
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.591796875, 'crossentropy': 1.3925412893295288})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.5888671875, 'crossentropy': 1.6884772777557373})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 1.6216156482696533})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 1.6007463932037354})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 1.6474332809448242})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 1.58681321144104})
store['active_learning_steps'][8]['eval_training']['best_epoch']=5
store['active_learning_steps'][8]['acquisition']={'indices': [['id', 59771], ['id', 40744], ['id', 25939], ['id', 55098], ['id', 15119]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5971806095264895, 1.1486905182094804, 1.6717585089585454, 2.067391857109719, 2.3748690800974557]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 1.2191452980041504})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 1.426922082901001})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 2.017993927001953})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 2.1171770095825195})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 2.51173734664917})
store['active_learning_steps'][9]['training']['best_epoch']=2
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.6257, 'crossentropy': 1.47750693359375}
store['active_learning_steps'][9]['eval_training']={}
store['active_learning_steps'][9]['eval_training']['epochs']=[]
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.5908203125, 'crossentropy': 1.3282692432403564})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 1.1764118671417236})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 1.1800198554992676})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 1.167205810546875})
store['active_learning_steps'][9]['eval_training']['best_epoch']=3
store['active_learning_steps'][9]['acquisition']={'indices': [['id', 54813], ['id', 28869], ['id', 24996], ['id', 32218], ['id', 41355]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.6139061015578742, 1.0954069594924642, 1.478809112561251, 1.7945456117220457, 2.025639086498156]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.5908203125, 'crossentropy': 1.2852839231491089})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 1.5192551612854004})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 1.7923797369003296})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 1.941866397857666})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 2.2722415924072266})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 2.2423205375671387})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 2.2564101219177246})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 2.438357353210449})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 2.3841233253479004})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 2.7115113735198975})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 2.5041260719299316})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 2.501521110534668})
store['active_learning_steps'][10]['training']['best_epoch']=9
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.6518, 'crossentropy': 2.4381234375}
store['active_learning_steps'][10]['eval_training']={}
store['active_learning_steps'][10]['eval_training']['epochs']=[]
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.5859375, 'crossentropy': 1.3773475885391235})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 1.4565486907958984})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 1.5341615676879883})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 1.4726194143295288})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 1.3664767742156982})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 1.3825284242630005})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 1.438897967338562})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 1.4210562705993652})
store['active_learning_steps'][10]['eval_training']['best_epoch']=5
store['active_learning_steps'][10]['acquisition']={'indices': [['id', 22718], ['id', 18126], ['id', 25796], ['id', 55157], ['id', 25144]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.6598199163496459, 1.2645158448665041, 1.7995276748568085, 2.2121001476963915, 2.5007580483189393]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 1.2917296886444092})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 1.304240345954895})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 1.5360453128814697})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 1.9371540546417236})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 1.9964520931243896})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 2.1790003776550293})
store['active_learning_steps'][11]['training']['best_epoch']=3
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.6503, 'crossentropy': 1.6434001953125}
store['active_learning_steps'][11]['eval_training']={}
store['active_learning_steps'][11]['eval_training']['epochs']=[]
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 1.2570396661758423})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 1.183090329170227})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 1.2236741781234741})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 1.2375251054763794})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 1.2663252353668213})
store['active_learning_steps'][11]['eval_training']['best_epoch']=3
store['active_learning_steps'][11]['acquisition']={'indices': [['id', 2434], ['id', 59835], ['id', 58458], ['id', 17338], ['id', 58300]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.4654408862360395, 0.8563117662405859, 1.198463623480551, 1.4796522284902158, 1.7049731892326907]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.599609375, 'crossentropy': 1.3517019748687744})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 1.3026089668273926})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 1.4857351779937744})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 1.8115959167480469})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 1.8243913650512695})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 1.798255205154419})
store['active_learning_steps'][12]['training']['best_epoch']=3
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.6451, 'crossentropy': 1.425434375}
store['active_learning_steps'][12]['eval_training']={}
store['active_learning_steps'][12]['eval_training']['epochs']=[]
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 1.2703534364700317})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 1.1486610174179077})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 1.1279830932617188})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 1.130329966545105})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 1.0824867486953735})
store['active_learning_steps'][12]['eval_training']['best_epoch']=5
store['active_learning_steps'][12]['acquisition']={'indices': [['id', 48293], ['id', 51231], ['id', 42192], ['id', 4284], ['id', 31662]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.5144135830148631, 0.9588709780834384, 1.3136075075071298, 1.6017399610265235, 1.8257984404012202]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.591796875, 'crossentropy': 1.4536056518554688})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 1.289933443069458})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 1.4384913444519043})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 1.8173878192901611})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 1.787003993988037})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 2.079277992248535})
store['active_learning_steps'][13]['training']['best_epoch']=3
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.6634, 'crossentropy': 1.49989765625}
store['active_learning_steps'][13]['eval_training']={}
store['active_learning_steps'][13]['eval_training']['epochs']=[]
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 1.2636079788208008})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 1.168707013130188})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 1.1178820133209229})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 1.1239449977874756})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 1.1228513717651367})
store['active_learning_steps'][13]['eval_training']['best_epoch']=3
store['active_learning_steps'][13]['acquisition']={'indices': [['id', 33801], ['id', 55519], ['id', 37613], ['id', 35649], ['id', 42681]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.574875497954997, 1.0405020010244685, 1.4514150378388733, 1.7888600538304624, 2.05453465389564]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.5615234375, 'crossentropy': 1.43571138381958})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 1.3786824941635132})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 1.5872575044631958})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 1.7735382318496704})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 1.8918073177337646})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 2.2841408252716064})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 2.31640625})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 2.287306308746338})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 2.0449864864349365})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 2.476606845855713})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 2.462790012359619})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 2.682490587234497})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 2.698381185531616})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 2.3949573040008545})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 2.670175075531006})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 2.5876874923706055})
store['active_learning_steps'][14]['training']['best_epoch']=13
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.6374, 'crossentropy': 2.9269361328125}
store['active_learning_steps'][14]['eval_training']={}
store['active_learning_steps'][14]['eval_training']['epochs']=[]
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.5830078125, 'crossentropy': 1.39146089553833})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 1.2489463090896606})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 1.436431884765625})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 1.5989444255828857})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 1.679785966873169})
store['active_learning_steps'][14]['eval_training']['best_epoch']=2
store['active_learning_steps'][14]['acquisition']={'indices': [['id', 30173], ['id', 2067], ['id', 12346], ['id', 42231], ['id', 41037]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.8342204019012149, 1.5133937636871861, 2.0990744134126, 2.542416589917573, 2.8620212801161085]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 1.3214740753173828})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 1.1597543954849243})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 1.2209677696228027})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 1.5620734691619873})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 1.4664311408996582})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 1.7611900568008423})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 1.6447436809539795})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 1.8524701595306396})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 1.830244779586792})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 1.786294937133789})
store['active_learning_steps'][15]['training']['best_epoch']=7
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.6761, 'crossentropy': 1.5976029296875}
store['active_learning_steps'][15]['eval_training']={}
store['active_learning_steps'][15]['eval_training']['epochs']=[]
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 1.2736974954605103})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 1.1123158931732178})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 1.1132326126098633})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 1.1336805820465088})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 1.1574628353118896})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 1.081520676612854})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 1.0946861505508423})
store['active_learning_steps'][15]['eval_training']['best_epoch']=4
store['active_learning_steps'][15]['acquisition']={'indices': [['id', 18584], ['id', 48802], ['id', 59559], ['id', 26635], ['id', 31994]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.6363900434595271, 1.190145272518753, 1.5982648229722174, 1.884557264615629, 2.0941932592514005]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 1.3250770568847656})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 1.1370799541473389})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 1.3719940185546875})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 1.365476131439209})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 1.670761227607727})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 1.9007288217544556})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 1.6370214223861694})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 1.8035471439361572})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 1.8876678943634033})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.9143955707550049})
store['active_learning_steps'][16]['training']['best_epoch']=7
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.6996, 'crossentropy': 1.62183291015625}
store['active_learning_steps'][16]['eval_training']={}
store['active_learning_steps'][16]['eval_training']['epochs']=[]
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.59375, 'crossentropy': 1.3165282011032104})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 1.1076925992965698})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 1.1021158695220947})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 1.0970168113708496})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 1.0866916179656982})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 1.081512212753296})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 1.0712995529174805})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 1.0361207723617554})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 1.0386011600494385})
store['active_learning_steps'][16]['eval_training']['best_epoch']=9
store['active_learning_steps'][16]['acquisition']={'indices': [['id', 23077], ['id', 7666], ['id', 22399], ['id', 13107], ['id', 16803]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.640357883101911, 1.1713233830120329, 1.628724036784785, 1.980919927875929, 2.230283107720151]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.595703125, 'crossentropy': 1.3277344703674316})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.1283471584320068})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 1.2825201749801636})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 1.3005764484405518})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 1.485280990600586})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 1.5943437814712524})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 1.617769718170166})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 1.7477672100067139})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 1.7764081954956055})
store['active_learning_steps'][17]['training']['best_epoch']=6
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.7064, 'crossentropy': 1.51405810546875}
store['active_learning_steps'][17]['eval_training']={}
store['active_learning_steps'][17]['eval_training']['epochs']=[]
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 1.2230409383773804})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 1.0510077476501465})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 1.0733613967895508})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 1.089760422706604})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 1.0908050537109375})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 1.0473871231079102})
store['active_learning_steps'][17]['eval_training']['best_epoch']=3
store['active_learning_steps'][17]['acquisition']={'indices': [['id', 21473], ['id', 15911], ['id', 59536], ['id', 22159], ['id', 14870]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5779736018335637, 1.1190676156845383, 1.5532164579030283, 1.896124218174454, 2.147283309203355]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 1.2888884544372559})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 1.11564302444458})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 1.2535316944122314})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 1.5044796466827393})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 1.6951558589935303})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 1.6901612281799316})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 2.03262996673584})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 2.036426544189453})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 2.2183923721313477})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 2.109715700149536})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 2.2238595485687256})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 2.1662349700927734})
store['active_learning_steps'][18]['training']['best_epoch']=9
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.6897, 'crossentropy': 2.192656640625}
store['active_learning_steps'][18]['eval_training']={}
store['active_learning_steps'][18]['eval_training']['epochs']=[]
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 1.2387537956237793})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.1093052625656128})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 1.221315860748291})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 1.3384449481964111})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 1.320925235748291})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 1.3693389892578125})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 1.3320969343185425})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.31196129322052})
store['active_learning_steps'][18]['eval_training']['best_epoch']=5
store['active_learning_steps'][18]['acquisition']={'indices': [['id', 13386], ['id', 23149], ['id', 14264], ['id', 28071], ['id', 1119]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.5974475158283015, 1.1275827491521473, 1.5658856864716473, 1.919028394446733, 2.1455957213135406]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.5615234375, 'crossentropy': 1.3525621891021729})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 1.209212064743042})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 1.3840574026107788})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 1.3671892881393433})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 1.6250195503234863})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 1.722102403640747})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 1.9197628498077393})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 2.089008331298828})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 2.158491611480713})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 2.0477511882781982})
store['active_learning_steps'][19]['training']['best_epoch']=7
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.7, 'crossentropy': 1.8064626953125}
store['active_learning_steps'][19]['eval_training']={}
store['active_learning_steps'][19]['eval_training']['epochs']=[]
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 1.1780428886413574})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 1.0936847925186157})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 1.1403242349624634})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 1.1027240753173828})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 1.1751779317855835})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 1.1269139051437378})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 1.1146776676177979})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 1.0282704830169678})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 1.077880859375})
store['active_learning_steps'][19]['eval_training']['best_epoch']=7
store['active_learning_steps'][19]['acquisition']={'indices': [['id', 52539], ['id', 13569], ['id', 30664], ['id', 30644], ['id', 22622]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.6081054521247804, 1.1440143396231215, 1.6190873851950398, 1.992924089960617, 2.2617522119657796]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 1.379022240638733})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 1.1117304563522339})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 1.2419958114624023})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 1.3878588676452637})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 1.3776459693908691})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 1.5836337804794312})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 1.8997931480407715})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.7545416355133057})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 1.9124419689178467})
store['active_learning_steps'][20]['training']['best_epoch']=6
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.6981, 'crossentropy': 1.62914794921875}
store['active_learning_steps'][20]['eval_training']={}
store['active_learning_steps'][20]['eval_training']['epochs']=[]
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 1.2852509021759033})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.092057704925537})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.0816596746444702})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 1.117728352546692})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 1.091548204421997})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 1.137930154800415})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 1.0676805973052979})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 1.1017160415649414})
store['active_learning_steps'][20]['eval_training']['best_epoch']=8
store['active_learning_steps'][20]['acquisition']={'indices': [['id', 34743], ['id', 16469], ['id', 55864], ['id', 13257], ['id', 21285]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.627566840723166, 1.1732169403401413, 1.6605922358947938, 2.0279343645992416, 2.29172624635922]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.53125, 'crossentropy': 1.3518697023391724})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 1.205471158027649})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 1.3211393356323242})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 1.405155062675476})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 1.643821358680725})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 1.9478213787078857})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 1.9928784370422363})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 1.9327266216278076})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 2.1077771186828613})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 2.1462655067443848})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 2.1315176486968994})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 2.191117525100708})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 1.8928256034851074})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 2.1591897010803223})
store['active_learning_steps'][21]['training']['best_epoch']=11
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.6934, 'crossentropy': 2.0366708984375}
store['active_learning_steps'][21]['eval_training']={}
store['active_learning_steps'][21]['eval_training']['epochs']=[]
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 1.2739123106002808})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 1.1521854400634766})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 1.2559573650360107})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 1.3298929929733276})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 1.2423949241638184})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 1.3030219078063965})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 1.2591642141342163})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 1.3524696826934814})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 1.2002317905426025})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.2477221488952637})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 1.2131383419036865})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 1.2362158298492432})
store['active_learning_steps'][21]['eval_training']['best_epoch']=9
store['active_learning_steps'][21]['acquisition']={'indices': [['id', 28537], ['id', 54138], ['id', 25302], ['id', 23401], ['id', 5914]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.7130141859123524, 1.3242777612944399, 1.8259693610358334, 2.188022446569015, 2.4380176417730564]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.5751953125, 'crossentropy': 1.3864965438842773})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 1.149167537689209})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 1.2974753379821777})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.3147785663604736})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 1.4218883514404297})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.712890625, 'crossentropy': 1.5776214599609375})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 1.5111193656921387})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 1.7237274646759033})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 1.7240184545516968})
store['active_learning_steps'][22]['training']['best_epoch']=6
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.7033, 'crossentropy': 1.5549099609375}
store['active_learning_steps'][22]['eval_training']={}
store['active_learning_steps'][22]['eval_training']['epochs']=[]
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 1.285071611404419})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 1.0805786848068237})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 1.0417265892028809})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 1.0445196628570557})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 1.037846565246582})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 1.0320154428482056})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 1.0015957355499268})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 1.0486359596252441})
store['active_learning_steps'][22]['eval_training']['best_epoch']=5
store['active_learning_steps'][22]['acquisition']={'indices': [['id', 22139], ['id', 19088], ['id', 23152], ['id', 33792], ['id', 16530]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [0.5811158586424492, 1.101229398753878, 1.5285531536679562, 1.8730869663064444, 2.1020981919480146]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 1.303436040878296})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 1.1297166347503662})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 1.238775372505188})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 1.3904566764831543})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 1.5374387502670288})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 1.605126976966858})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 1.6582863330841064})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 1.8909393548965454})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 2.104037284851074})
store['active_learning_steps'][23]['training']['best_epoch']=6
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.7029, 'crossentropy': 1.59889931640625}
store['active_learning_steps'][23]['eval_training']={}
store['active_learning_steps'][23]['eval_training']['epochs']=[]
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 1.2626111507415771})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 1.1434965133666992})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 1.1038414239883423})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 1.1232229471206665})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.712890625, 'crossentropy': 1.108333945274353})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 1.1788899898529053})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 1.128244161605835})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 1.145165205001831})
store['active_learning_steps'][23]['eval_training']['best_epoch']=5
store['active_learning_steps'][23]['acquisition']={'indices': [['id', 25420], ['id', 55575], ['id', 24749], ['id', 47111], ['id', 59264]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5382522141322525, 1.0329801398839416, 1.427803768700453, 1.702285004849374, 1.8937964757240975]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.55859375, 'crossentropy': 1.4129524230957031})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 1.108991026878357})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 1.2006487846374512})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 1.26577889919281})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 1.465646505355835})
store['active_learning_steps'][24]['training']['best_epoch']=2
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.6713, 'crossentropy': 1.134844921875}
store['active_learning_steps'][24]['eval_training']={}
store['active_learning_steps'][24]['eval_training']['epochs']=[]
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 1.3097798824310303})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 1.1409436464309692})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 1.0965898036956787})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 1.0735770463943481})
store['active_learning_steps'][24]['eval_training']['best_epoch']=4
store['active_learning_steps'][24]['acquisition']={'indices': [['id', 10100], ['id', 27090], ['id', 19888], ['id', 58130], ['id', 16778]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.40910414855076227, 0.7587090406858792, 1.0584224879655446, 1.3284752683879057, 1.5621129486410723]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.5908203125, 'crossentropy': 1.3778479099273682})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 1.1184589862823486})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 1.1124560832977295})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 1.232712984085083})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 1.3677728176116943})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 1.6174812316894531})
store['active_learning_steps'][25]['training']['best_epoch']=3
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.6955, 'crossentropy': 1.13478466796875}
store['active_learning_steps'][25]['eval_training']={}
store['active_learning_steps'][25]['eval_training']['epochs']=[]
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 1.3130509853363037})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 1.0643949508666992})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 1.0229837894439697})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 0.9971135854721069})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 0.9481918811798096})
store['active_learning_steps'][25]['eval_training']['best_epoch']=5
store['active_learning_steps'][25]['acquisition']={'indices': [['id', 11374], ['id', 52799], ['id', 43863], ['id', 63], ['id', 18729]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.4061505307654283, 0.7683777980208641, 1.1040782173086736, 1.4126050492487705, 1.665884399246707]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 1.2935643196105957})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 1.0968000888824463})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 1.1240646839141846})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 1.250730037689209})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 1.3566863536834717})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 1.515250325202942})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.5462011098861694})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.6466898918151855})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 1.7720036506652832})
store['active_learning_steps'][26]['training']['best_epoch']=6
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.6803, 'crossentropy': 1.49917568359375}
store['active_learning_steps'][26]['eval_training']={}
store['active_learning_steps'][26]['eval_training']['epochs']=[]
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.603515625, 'crossentropy': 1.299667477607727})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 1.0679657459259033})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.0453764200210571})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 1.034835696220398})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 1.0301823616027832})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 1.041473627090454})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 1.0528324842453003})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 1.0252469778060913})
store['active_learning_steps'][26]['eval_training']['best_epoch']=6
store['active_learning_steps'][26]['acquisition']={'indices': [['id', 35309], ['id', 49663], ['id', 40742], ['id', 48714], ['id', 39345]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6040679543005161, 1.0818571330049456, 1.4967139863502794, 1.8040088245824055, 2.032605818343912]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.58984375, 'crossentropy': 1.3826488256454468})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 1.1140341758728027})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 1.1509907245635986})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 1.2032406330108643})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 1.2185938358306885})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 1.4166417121887207})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 1.4473271369934082})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 1.6312021017074585})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 1.6376603841781616})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 1.7415255308151245})
store['active_learning_steps'][27]['training']['best_epoch']=7
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.6925, 'crossentropy': 1.5326703125}
store['active_learning_steps'][27]['eval_training']={}
store['active_learning_steps'][27]['eval_training']['epochs']=[]
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.5654296875, 'crossentropy': 1.3815454244613647})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 1.105243444442749})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 1.0674184560775757})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 1.0611838102340698})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 1.0698072910308838})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 1.0420255661010742})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 1.0190184116363525})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 1.0406115055084229})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 1.0441598892211914})
store['active_learning_steps'][27]['eval_training']['best_epoch']=9
store['active_learning_steps'][27]['acquisition']={'indices': [['id', 8335], ['id', 45674], ['id', 35305], ['id', 14145], ['id', 3410]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.5771451955633136, 1.124534045144931, 1.5825143077831427, 1.9397556061736836, 2.191251500311676]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.4599609375, 'crossentropy': 1.481652021408081})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 1.1139068603515625})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 1.0508322715759277})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 1.1442749500274658})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 1.2176353931427002})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 1.3685493469238281})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 1.4278385639190674})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 1.417314052581787})
store['active_learning_steps'][28]['training']['best_epoch']=5
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.6977, 'crossentropy': 1.2430841796875}
store['active_learning_steps'][28]['eval_training']={}
store['active_learning_steps'][28]['eval_training']['epochs']=[]
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.5498046875, 'crossentropy': 1.3564748764038086})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 1.0550792217254639})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 1.025740146636963})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 1.056074619293213})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 1.0152170658111572})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 1.0160232782363892})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 0.997168242931366})
store['active_learning_steps'][28]['eval_training']['best_epoch']=7
store['active_learning_steps'][28]['acquisition']={'indices': [['id', 5346], ['id', 7611], ['id', 47562], ['id', 47350], ['id', 51368]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.5894405525242483, 1.0602264156164671, 1.4649581533384382, 1.8058310154297796, 2.073179138168599]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.529296875, 'crossentropy': 1.4958360195159912})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 1.2044055461883545})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 1.0958812236785889})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 1.1763464212417603})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 1.2184836864471436})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 1.404977560043335})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 1.5337516069412231})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 1.565406084060669})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 1.7607872486114502})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 1.7859050035476685})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 1.7769911289215088})
store['active_learning_steps'][29]['training']['best_epoch']=8
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.6935, 'crossentropy': 1.615225}
store['active_learning_steps'][29]['eval_training']={}
store['active_learning_steps'][29]['eval_training']['epochs']=[]
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 1.297151803970337})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 1.0445404052734375})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 1.0330510139465332})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 1.025754451751709})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 1.020524024963379})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 0.9892063140869141})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.712890625, 'crossentropy': 1.008139967918396})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 1.0521831512451172})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 1.002300500869751})
store['active_learning_steps'][29]['eval_training']['best_epoch']=6
store['active_learning_steps'][29]['acquisition']={'indices': [['id', 12567], ['id', 57132], ['id', 16858], ['id', 46613], ['id', 15320]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.5931541230870894, 1.1110588273389785, 1.5816890121013882, 1.94127580135076, 2.202125373063197]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.5380859375, 'crossentropy': 1.4214184284210205})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 1.1250087022781372})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 1.1209936141967773})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 1.2130353450775146})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 1.2667993307113647})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 1.3942627906799316})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 1.4660276174545288})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.740445852279663})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 1.8607571125030518})
store['active_learning_steps'][30]['training']['best_epoch']=6
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.6937, 'crossentropy': 1.3619322265625}
store['active_learning_steps'][30]['eval_training']={}
store['active_learning_steps'][30]['eval_training']['epochs']=[]
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 1.3370270729064941})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 1.0194305181503296})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 1.018857717514038})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 0.9995817542076111})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.016451358795166})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 0.9895846247673035})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 0.9600954055786133})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 0.9701911211013794})
store['active_learning_steps'][30]['eval_training']['best_epoch']=7
store['active_learning_steps'][30]['acquisition']={'indices': [['id', 32065], ['id', 1462], ['id', 13696], ['id', 42294], ['id', 41318]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.555485720779719, 1.0248213251475637, 1.451946097610473, 1.7734866129039304, 2.0081282301140275]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.5703125, 'crossentropy': 1.3843598365783691})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 1.104243278503418})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 1.085735559463501})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 1.1954224109649658})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 1.224003553390503})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 1.4330949783325195})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 1.4006168842315674})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 1.528662085533142})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 1.4822001457214355})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 1.698314905166626})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 1.7056910991668701})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.71484375, 'crossentropy': 1.6358705759048462})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 1.8252629041671753})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 1.8351773023605347})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 1.838573932647705})
store['active_learning_steps'][31]['training']['best_epoch']=12
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.7027, 'crossentropy': 1.640644921875}
store['active_learning_steps'][31]['eval_training']={}
store['active_learning_steps'][31]['eval_training']['epochs']=[]
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.556640625, 'crossentropy': 1.3738343715667725})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 1.0553354024887085})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 1.053575873374939})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 1.0515626668930054})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 1.0385849475860596})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.71484375, 'crossentropy': 1.0423797369003296})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 1.0683497190475464})
store['active_learning_steps'][31]['eval_training']['best_epoch']=4
store['active_learning_steps'][31]['acquisition']={'indices': [['id', 39272], ['id', 32578], ['id', 47543], ['id', 51146], ['id', 44570]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6098377599046945, 1.1727746257559306, 1.6637797608976257, 2.010931721234618, 2.259468082343969]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.5712890625, 'crossentropy': 1.3708397150039673})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 1.1301114559173584})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 1.1187593936920166})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 1.0791553258895874})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 1.205543041229248})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 1.2866729497909546})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 1.3282901048660278})
store['active_learning_steps'][32]['training']['best_epoch']=4
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.699, 'crossentropy': 1.13126357421875}
store['active_learning_steps'][32]['eval_training']={}
store['active_learning_steps'][32]['eval_training']['epochs']=[]
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 1.3294296264648438})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 1.0541398525238037})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 0.9566243290901184})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 0.9276258945465088})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.716796875, 'crossentropy': 0.9248214960098267})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 0.9137142300605774})
store['active_learning_steps'][32]['eval_training']['best_epoch']=5
store['active_learning_steps'][32]['acquisition']={'indices': [['id', 56380], ['id', 15290], ['id', 19837], ['id', 57943], ['id', 20217]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.45823990444296747, 0.858120456856688, 1.2189925473477308, 1.5299217039855693, 1.7844029858022177]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.546875, 'crossentropy': 1.4008716344833374})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 1.0627801418304443})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 0.9910262227058411})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 1.0803022384643555})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 1.1096014976501465})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 1.2086267471313477})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 1.3588855266571045})
store['active_learning_steps'][33]['training']['best_epoch']=4
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.7131, 'crossentropy': 1.085015234375}
store['active_learning_steps'][33]['eval_training']={}
store['active_learning_steps'][33]['eval_training']['epochs']=[]
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.556640625, 'crossentropy': 1.3832767009735107})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 1.0337388515472412})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.71484375, 'crossentropy': 0.9921797513961792})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.7216796875, 'crossentropy': 0.957159161567688})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.71484375, 'crossentropy': 0.9433972835540771})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.728515625, 'crossentropy': 0.9248276948928833})
store['active_learning_steps'][33]['eval_training']['best_epoch']=6
store['active_learning_steps'][33]['acquisition']={'indices': [['id', 37251], ['id', 801], ['id', 39750], ['id', 45171], ['id', 26263]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.47477606905533487, 0.8809957007905829, 1.2372520036113306, 1.5358942366571302, 1.7929319535674146]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.46484375, 'crossentropy': 1.5507699251174927})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.5947265625, 'crossentropy': 1.1950522661209106})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 1.0716081857681274})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 1.0598750114440918})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 1.102818489074707})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 1.2944552898406982})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 1.2740867137908936})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 1.192553997039795})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.724609375, 'crossentropy': 1.3067582845687866})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 1.467421054840088})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.72265625, 'crossentropy': 1.4780704975128174})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.734375, 'crossentropy': 1.510280966758728})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 1.5725562572479248})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.7314453125, 'crossentropy': 1.5023984909057617})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.7236328125, 'crossentropy': 1.633744716644287})
store['active_learning_steps'][34]['training']['best_epoch']=12
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.7262, 'crossentropy': 1.504394921875}
store['active_learning_steps'][34]['eval_training']={}
store['active_learning_steps'][34]['eval_training']['epochs']=[]
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.482421875, 'crossentropy': 1.4827251434326172})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 1.1315200328826904})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.712890625, 'crossentropy': 0.9825679063796997})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 0.9598016738891602})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.732421875, 'crossentropy': 0.9333642721176147})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.732421875, 'crossentropy': 0.994731068611145})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.7392578125, 'crossentropy': 0.9738854169845581})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.732421875, 'crossentropy': 0.9577138423919678})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.7294921875, 'crossentropy': 0.9538442492485046})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.7490234375, 'crossentropy': 0.9611621499061584})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.744140625, 'crossentropy': 0.9619253873825073})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.732421875, 'crossentropy': 0.9588347673416138})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.7353515625, 'crossentropy': 0.9524245262145996})
store['active_learning_steps'][34]['eval_training']['best_epoch']=10
store['active_learning_steps'][34]['acquisition']={'indices': [['id', 3913], ['id', 42361], ['id', 54957], ['id', 23756], ['id', 20004]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.7211507299629527, 1.2724739700098397, 1.7272428741296348, 2.048996678948937, 2.2577315970177025]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.517578125, 'crossentropy': 1.4606293439865112})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 1.0947718620300293})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 1.091858148574829})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 1.0783746242523193})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 1.1447434425354004})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 1.089842677116394})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 1.2673970460891724})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.712890625, 'crossentropy': 1.3191291093826294})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.728515625, 'crossentropy': 1.3958086967468262})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.7216796875, 'crossentropy': 1.4589855670928955})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.7236328125, 'crossentropy': 1.5735116004943848})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.7265625, 'crossentropy': 1.5233831405639648})
store['active_learning_steps'][35]['training']['best_epoch']=9
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.719, 'crossentropy': 1.45070234375}
store['active_learning_steps'][35]['eval_training']={}
store['active_learning_steps'][35]['eval_training']['epochs']=[]
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.5517578125, 'crossentropy': 1.3959475755691528})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 1.111595630645752})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 1.006283164024353})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.7236328125, 'crossentropy': 0.9805040955543518})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.7255859375, 'crossentropy': 0.9607470035552979})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.7333984375, 'crossentropy': 0.9630085229873657})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.724609375, 'crossentropy': 0.9879618883132935})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.7314453125, 'crossentropy': 0.9406092166900635})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.73046875, 'crossentropy': 0.9272304773330688})
store['active_learning_steps'][35]['eval_training']['best_epoch']=6
store['active_learning_steps'][35]['acquisition']={'indices': [['id', 865], ['id', 2965], ['id', 15841], ['id', 34655], ['id', 18011]], 'labels': [[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.5266576603619675, 1.0148339171601828, 1.4543645553810371, 1.812301002621493, 2.058598728964042]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 1.3307240009307861})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 1.0361096858978271})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 1.0099769830703735})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.7216796875, 'crossentropy': 0.9589678645133972})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.712890625, 'crossentropy': 1.0718870162963867})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 1.176896333694458})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 1.2168738842010498})
store['active_learning_steps'][36]['training']['best_epoch']=4
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.7141, 'crossentropy': 1.00314033203125}
