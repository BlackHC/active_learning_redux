store = {}
store['timestamp']=1621477995
store['cmdline']=['/home/kell4989/git/active_learning_redux/batchbald_redux/ood_experiment.py', '--id=51']
store['commit']='8a2cf4fb40ce306533b4e439b08268c53f009a3b'
store['github_url']='8a2cf4fb40ce306533b4e439b08268c53f009a3b'
store['experiment']='/home/kell4989/git/active_learning_redux/batchbald_redux/ood_experiment.py'
store['job_id']=51
store['worker_id']=51
store['num_workers']=80
store['config']={'seed': 1288, 'uniform_ood': False, 'id_dataset_type': 'batchbald_redux.fast_mnist.FastFashionMNIST', 'ood_dataset_type': 'batchbald_redux.fast_mnist.FastMNIST', 'initial_training_set_size': 20, 'validation_set_size': 1024, 'evaluation_set_size': 16, 'id_repetitions': 1, 'ood_repetitions': 1, 'add_dataset_noise': False, 'validation_split_random_state': 0, 'acquisition_size': 5, 'max_training_set': 200, 'num_pool_samples': 100, 'num_validation_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'min_samples_per_epoch': 5056, 'acquisition_function': 'batchbald_redux.acquisition_functions.BatchEvalBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationEvalModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 8}
store['log']={}
store['dataset_info']={'training': "(FastFashionMNIST (train; 58976 samples)) + ('FastMNIST Train (60000 samples)' | constant_target{'target': tensor(-1, device='cuda:0'), 'num_classes': 10})", 'test': "'FastFashionMNIST Test (10000 samples)'"}
store['initial_training_set_indices']=[55573, 380, 12640, 44119, 30392, 58226, 43812, 52440, 3091, 29974, 49512, 46037, 53434, 22015, 37915, 52296, 8533, 58125, 22304, 35472]
store['evaluation_set_indices']=[42890, 14640, 45567, 52801, 53689, 801, 55187, 26479, 50997, 3792]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 2.389287233352661})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 3.067747116088867})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.5927734375, 'crossentropy': 3.674717426300049})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 3.5610601902008057})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.595703125, 'crossentropy': 3.6109137535095215})
store['active_learning_steps'][0]['training']['best_epoch']=2
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.6063, 'crossentropy': 3.1022728515625}
store['active_learning_steps'][0]['eval_training']={}
store['active_learning_steps'][0]['eval_training']['epochs']=[]
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.59375, 'crossentropy': 1.7513811588287354})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6005859375, 'crossentropy': 1.717702031135559})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 1.7242488861083984})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 1.7837949991226196})
store['active_learning_steps'][0]['eval_training']['best_epoch']=4
store['active_learning_steps'][0]['acquisition']={'indices': [['id', 26106], ['id', 55011], ['id', 6364], ['id', 37925], ['id', 33882]], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.8975479264037581, 1.568160784319667, 2.1287883715454976, 2.5085143934319163, 2.735368580939256]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 2.451680898666382})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 3.0052995681762695})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 3.3842415809631348})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.603515625, 'crossentropy': 3.452615737915039})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 3.859321117401123})
store['active_learning_steps'][1]['training']['best_epoch']=2
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.5956, 'crossentropy': 3.1511529296875}
store['active_learning_steps'][1]['eval_training']={}
store['active_learning_steps'][1]['eval_training']['epochs']=[]
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 1.7812373638153076})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 1.791396975517273})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 1.598325252532959})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 1.7901463508605957})
store['active_learning_steps'][1]['eval_training']['best_epoch']=4
store['active_learning_steps'][1]['acquisition']={'indices': [['id', 12758], ['id', 29054], ['id', 17850], ['id', 14661], ['id', 25728]], 'labels': [-1, -1, -1, -1, 3], 'scores': [1.092299193523496, 1.9283693478954533, 2.5200489430915285, 2.8756441643557236, 3.056869624054342]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 1.9984090328216553})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 2.6985039710998535})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 3.0010859966278076})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 3.1895947456359863})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 3.49003267288208})
store['active_learning_steps'][2]['training']['best_epoch']=2
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.6154, 'crossentropy': 2.8371228515625}
store['active_learning_steps'][2]['eval_training']={}
store['active_learning_steps'][2]['eval_training']['epochs']=[]
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 1.5420687198638916})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 1.5147619247436523})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 1.413586139678955})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 1.3857412338256836})
store['active_learning_steps'][2]['eval_training']['best_epoch']=4
store['active_learning_steps'][2]['acquisition']={'indices': [['id', 20098], ['id', 38132], ['id', 12784], ['id', 41478], ['id', 36456]], 'labels': [-1, -1, -1, -1, 6], 'scores': [1.002517811368326, 1.7713449459961146, 2.2483920736235365, 2.5648565742294815, 2.75918804775945]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.5888671875, 'crossentropy': 2.472691297531128})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 2.7173399925231934})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 3.4049556255340576})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6005859375, 'crossentropy': 3.223938465118408})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 3.613142967224121})
store['active_learning_steps'][3]['training']['best_epoch']=2
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.6093, 'crossentropy': 3.024375390625}
store['active_learning_steps'][3]['eval_training']={}
store['active_learning_steps'][3]['eval_training']['epochs']=[]
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 1.641495943069458})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 1.7845425605773926})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 1.656524896621704})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 1.6068788766860962})
store['active_learning_steps'][3]['eval_training']['best_epoch']=1
store['active_learning_steps'][3]['acquisition']={'indices': [['id', 40031], ['id', 57414], ['id', 44491], ['id', 46677], ['id', 9633]], 'labels': [-1, 5, 5, 2, -1], 'scores': [0.9686671614391514, 1.5918480800245383, 2.096484695872327, 2.4465740490998265, 2.638840165048119]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.5810546875, 'crossentropy': 2.3067126274108887})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.595703125, 'crossentropy': 2.7552573680877686})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6005859375, 'crossentropy': 2.935391664505005})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 3.031919479370117})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 2.7862634658813477})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.59375, 'crossentropy': 3.2045793533325195})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.5869140625, 'crossentropy': 3.1560468673706055})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6005859375, 'crossentropy': 3.485912322998047})
store['active_learning_steps'][4]['training']['best_epoch']=5
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.6096, 'crossentropy': 3.0099412109375}
store['active_learning_steps'][4]['eval_training']={}
store['active_learning_steps'][4]['eval_training']['epochs']=[]
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.591796875, 'crossentropy': 1.7618536949157715})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 1.5626298189163208})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 1.5731724500656128})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 1.494119644165039})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 1.5950615406036377})
store['active_learning_steps'][4]['eval_training']['best_epoch']=2
store['active_learning_steps'][4]['acquisition']={'indices': [['id', 58626], ['id', 44901], ['id', 13343], ['id', 57538], ['id', 22718]], 'labels': [-1, -1, -1, 3, 0], 'scores': [1.1821231944370303, 2.010443125728349, 2.514683761821777, 2.845723795110408, 3.0654614836773404]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.5810546875, 'crossentropy': 2.014958620071411})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.578125, 'crossentropy': 3.0222926139831543})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.5615234375, 'crossentropy': 3.4739186763763428})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.56640625, 'crossentropy': 3.5978317260742188})
store['active_learning_steps'][5]['training']['best_epoch']=1
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.5653, 'crossentropy': 2.2441990234375}
store['active_learning_steps'][5]['eval_training']={}
store['active_learning_steps'][5]['eval_training']['epochs']=[]
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.58203125, 'crossentropy': 1.3304808139801025})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.580078125, 'crossentropy': 1.3383007049560547})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.5703125, 'crossentropy': 1.3172767162322998})
store['active_learning_steps'][5]['eval_training']['best_epoch']=1
store['active_learning_steps'][5]['acquisition']={'indices': [['id', 31233], ['id', 39527], ['id', 50703], ['id', 50307], ['id', 19531]], 'labels': [-1, -1, -1, -1, 5], 'scores': [0.8466854633272928, 1.4972166646836067, 1.9689597390312303, 2.292064351065906, 2.4660407668380655]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.5888671875, 'crossentropy': 2.1432361602783203})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.5908203125, 'crossentropy': 2.760258197784424})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.5810546875, 'crossentropy': 3.531510829925537})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.5986328125, 'crossentropy': 3.1958839893341064})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.5849609375, 'crossentropy': 3.6156959533691406})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.59375, 'crossentropy': 3.4583141803741455})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.5859375, 'crossentropy': 3.903456687927246})
store['active_learning_steps'][6]['training']['best_epoch']=4
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.5752, 'crossentropy': 3.68543125}
store['active_learning_steps'][6]['eval_training']={}
store['active_learning_steps'][6]['eval_training']['epochs']=[]
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.5771484375, 'crossentropy': 1.7287484407424927})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.5810546875, 'crossentropy': 1.8180110454559326})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.5986328125, 'crossentropy': 1.7156472206115723})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 1.7719404697418213})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 1.7095247507095337})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 1.6979594230651855})
store['active_learning_steps'][6]['eval_training']['best_epoch']=4
store['active_learning_steps'][6]['acquisition']={'indices': [['id', 15466], ['id', 49693], ['id', 46975], ['id', 6545], ['id', 6848]], 'labels': [-1, -1, 7, -1, -1], 'scores': [1.0501810647386076, 1.8464543549695984, 2.404082139287693, 2.8334013961638993, 3.0930253355358404]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.591796875, 'crossentropy': 2.102720260620117})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.5849609375, 'crossentropy': 3.022481918334961})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.5888671875, 'crossentropy': 3.5011305809020996})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.5869140625, 'crossentropy': 3.4283809661865234})
store['active_learning_steps'][7]['training']['best_epoch']=1
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.5764, 'crossentropy': 2.159945703125}
store['active_learning_steps'][7]['eval_training']={}
store['active_learning_steps'][7]['eval_training']['epochs']=[]
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.5693359375, 'crossentropy': 1.5014525651931763})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 1.3578286170959473})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.58984375, 'crossentropy': 1.424561619758606})
store['active_learning_steps'][7]['eval_training']['best_epoch']=2
store['active_learning_steps'][7]['acquisition']={'indices': [['id', 8043], ['id', 36343], ['id', 31624], ['id', 57139], ['id', 2879]], 'labels': [-1, 5, -1, 3, -1], 'scores': [0.8359003104904361, 1.4734192085182087, 1.9846915667723342, 2.3597909608339642, 2.6474044827901713]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.5615234375, 'crossentropy': 2.197587251663208})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.59375, 'crossentropy': 2.893711566925049})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.5927734375, 'crossentropy': 3.1150434017181396})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.5771484375, 'crossentropy': 3.5708398818969727})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.5849609375, 'crossentropy': 3.6101279258728027})
store['active_learning_steps'][8]['training']['best_epoch']=2
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.5831, 'crossentropy': 2.9176125}
store['active_learning_steps'][8]['eval_training']={}
store['active_learning_steps'][8]['eval_training']['epochs']=[]
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.5673828125, 'crossentropy': 1.720694661140442})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.572265625, 'crossentropy': 1.8523213863372803})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.5888671875, 'crossentropy': 1.654671311378479})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.595703125, 'crossentropy': 1.6907422542572021})
store['active_learning_steps'][8]['eval_training']['best_epoch']=4
store['active_learning_steps'][8]['acquisition']={'indices': [['id', 28713], ['id', 21720], ['id', 39958], ['id', 39793], ['id', 7829]], 'labels': [-1, -1, -1, -1, 5], 'scores': [1.018404609209747, 1.683380947855737, 2.153375777876007, 2.48556821532627, 2.7015714585156987]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 1.9262301921844482})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.59375, 'crossentropy': 2.584258556365967})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.5986328125, 'crossentropy': 2.7751529216766357})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 3.044098377227783})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.59765625, 'crossentropy': 3.61393404006958})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.595703125, 'crossentropy': 3.8529233932495117})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 3.1532392501831055})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.59765625, 'crossentropy': 3.6049580574035645})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 3.559290885925293})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.603515625, 'crossentropy': 4.030869483947754})
store['active_learning_steps'][9]['training']['best_epoch']=7
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.596, 'crossentropy': 3.30179375}
store['active_learning_steps'][9]['eval_training']={}
store['active_learning_steps'][9]['eval_training']['epochs']=[]
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.5419921875, 'crossentropy': 1.80926513671875})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.568359375, 'crossentropy': 1.8108881711959839})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.580078125, 'crossentropy': 1.9387742280960083})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.5771484375, 'crossentropy': 1.9680428504943848})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.58203125, 'crossentropy': 1.934373378753662})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.58203125, 'crossentropy': 2.0066416263580322})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.580078125, 'crossentropy': 1.8663439750671387})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.5849609375, 'crossentropy': 1.901973009109497})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.580078125, 'crossentropy': 1.9767911434173584})
store['active_learning_steps'][9]['eval_training']['best_epoch']=8
store['active_learning_steps'][9]['acquisition']={'indices': [['id', 3058], ['id', 18729], ['id', 38815], ['id', 43998], ['id', 30067]], 'labels': [-1, 3, -1, -1, -1], 'scores': [1.1663218180694759, 2.0805294461592716, 2.7744429927575367, 3.2481309774844167, 3.553943929043199]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.576171875, 'crossentropy': 2.027759075164795})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.556640625, 'crossentropy': 2.8554515838623047})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.5732421875, 'crossentropy': 3.540106773376465})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.5888671875, 'crossentropy': 3.576724052429199})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.5673828125, 'crossentropy': 3.754096508026123})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.5947265625, 'crossentropy': 3.941969871520996})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 3.5565710067749023})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 3.221022605895996})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.5810546875, 'crossentropy': 4.0764970779418945})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.5859375, 'crossentropy': 4.37388801574707})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.58203125, 'crossentropy': 4.210781097412109})
store['active_learning_steps'][10]['training']['best_epoch']=8
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.5887, 'crossentropy': 3.620487890625}
store['active_learning_steps'][10]['eval_training']={}
store['active_learning_steps'][10]['eval_training']['epochs']=[]
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.5771484375, 'crossentropy': 1.7658793926239014})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.58203125, 'crossentropy': 1.895775318145752})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.578125, 'crossentropy': 1.9078367948532104})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.587890625, 'crossentropy': 1.87644624710083})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.5947265625, 'crossentropy': 1.8473960161209106})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.591796875, 'crossentropy': 1.7595183849334717})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.59765625, 'crossentropy': 1.770185112953186})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.5830078125, 'crossentropy': 2.054414749145508})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.5859375, 'crossentropy': 1.848311185836792})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.57421875, 'crossentropy': 2.0102219581604004})
store['active_learning_steps'][10]['eval_training']['best_epoch']=7
store['active_learning_steps'][10]['acquisition']={'indices': [['id', 1764], ['id', 45657], ['id', 8628], ['id', 21633], ['id', 18845]], 'labels': [-1, -1, 5, -1, -1], 'scores': [1.074395919608041, 1.9481603521414659, 2.551261874464953, 2.8752251644349913, 3.039271625860526]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.572265625, 'crossentropy': 1.9098564386367798})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.5771484375, 'crossentropy': 2.9377291202545166})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.5859375, 'crossentropy': 3.150923728942871})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.57421875, 'crossentropy': 3.72834849357605})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.5947265625, 'crossentropy': 3.195915699005127})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.58984375, 'crossentropy': 3.6523938179016113})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.583984375, 'crossentropy': 3.4153060913085938})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.552734375, 'crossentropy': 3.689749002456665})
store['active_learning_steps'][11]['training']['best_epoch']=5
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.5841, 'crossentropy': 3.386538671875}
store['active_learning_steps'][11]['eval_training']={}
store['active_learning_steps'][11]['eval_training']['epochs']=[]
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.5771484375, 'crossentropy': 1.731325387954712})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.5966796875, 'crossentropy': 1.9668421745300293})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.583984375, 'crossentropy': 1.920830488204956})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.58984375, 'crossentropy': 1.9190800189971924})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.5986328125, 'crossentropy': 1.9977736473083496})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.591796875, 'crossentropy': 1.9032814502716064})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.5927734375, 'crossentropy': 1.9869434833526611})
store['active_learning_steps'][11]['eval_training']['best_epoch']=5
store['active_learning_steps'][11]['acquisition']={'indices': [['id', 11640], ['id', 25318], ['id', 23785], ['id', 23684], ['id', 15602]], 'labels': [-1, -1, -1, 8, 1], 'scores': [1.10127764737092, 1.8753512151407405, 2.4339966659522583, 2.822389324441498, 3.075065811533451]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 1.704031229019165})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 2.2894818782806396})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 2.322270393371582})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 2.555579662322998})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 2.973339557647705})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 2.7566871643066406})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 2.8373630046844482})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 2.666384696960449})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 2.9657411575317383})
store['active_learning_steps'][12]['training']['best_epoch']=6
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.6282, 'crossentropy': 2.8814}
store['active_learning_steps'][12]['eval_training']={}
store['active_learning_steps'][12]['eval_training']['epochs']=[]
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 1.5481178760528564})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 1.502239465713501})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 1.464536190032959})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 1.460170030593872})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 1.5044699907302856})
store['active_learning_steps'][12]['eval_training']['best_epoch']=2
store['active_learning_steps'][12]['acquisition']={'indices': [['id', 25295], ['id', 28422], ['id', 19456], ['id', 36783], ['id', 57166]], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.9754098588965404, 1.6794015022666229, 2.2616721842546728, 2.6118779029274997, 2.8370383869560953]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.5986328125, 'crossentropy': 1.7140319347381592})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 2.236508369445801})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 2.86073637008667})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 2.8327584266662598})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 3.160344123840332})
store['active_learning_steps'][13]['training']['best_epoch']=2
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.6189, 'crossentropy': 2.336923828125}
store['active_learning_steps'][13]['eval_training']={}
store['active_learning_steps'][13]['eval_training']['epochs']=[]
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 1.3432629108428955})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 1.3859660625457764})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 1.331737756729126})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 1.3216577768325806})
store['active_learning_steps'][13]['eval_training']['best_epoch']=4
store['active_learning_steps'][13]['acquisition']={'indices': [['id', 47625], ['id', 56298], ['id', 20050], ['id', 12017], ['id', 8951]], 'labels': [-1, -1, -1, -1, 0], 'scores': [0.7829841437100451, 1.4380032145914265, 1.9723380023653458, 2.303491681499815, 2.5272304629855284]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.5859375, 'crossentropy': 1.7207852602005005})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 2.535088062286377})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 2.5103774070739746})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 2.709641218185425})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 2.877351999282837})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 2.94802188873291})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 3.0586705207824707})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 3.036804676055908})
store['active_learning_steps'][14]['training']['best_epoch']=5
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.6153, 'crossentropy': 3.1076802734375}
store['active_learning_steps'][14]['eval_training']={}
store['active_learning_steps'][14]['eval_training']['epochs']=[]
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 1.5659148693084717})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 1.6688625812530518})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 1.5998103618621826})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 1.6661162376403809})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 1.6491751670837402})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 1.660479187965393})
store['active_learning_steps'][14]['eval_training']['best_epoch']=3
store['active_learning_steps'][14]['acquisition']={'indices': [['id', 56705], ['id', 23682], ['id', 26412], ['id', 25662], ['id', 46271]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.245599019594235, 2.1640169704925873, 2.801420260482919, 3.1671835632589103, 3.3700391176243314]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 1.6861343383789062})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 2.0596933364868164})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 2.249318838119507})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 2.467498302459717})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 2.7498390674591064})
store['active_learning_steps'][15]['training']['best_epoch']=2
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.6181, 'crossentropy': 2.279153515625}
store['active_learning_steps'][15]['eval_training']={}
store['active_learning_steps'][15]['eval_training']['epochs']=[]
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 1.358259916305542})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 1.4335689544677734})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 1.4554469585418701})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 1.3929870128631592})
store['active_learning_steps'][15]['eval_training']['best_epoch']=3
store['active_learning_steps'][15]['acquisition']={'indices': [['id', 55438], ['id', 28], ['id', 12086], ['id', 40241], ['id', 31684]], 'labels': [-1, -1, -1, 2, 0], 'scores': [0.9085030186528901, 1.6224988153453277, 2.111432961165324, 2.442336698660535, 2.6349480897434274]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 1.5861756801605225})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 2.106841564178467})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 2.3671345710754395})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 2.286921262741089})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 2.5157861709594727})
store['active_learning_steps'][16]['training']['best_epoch']=2
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.6159, 'crossentropy': 2.185983203125}
store['active_learning_steps'][16]['eval_training']={}
store['active_learning_steps'][16]['eval_training']['epochs']=[]
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 1.5075275897979736})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 1.4099438190460205})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 1.4337809085845947})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 1.3283870220184326})
store['active_learning_steps'][16]['eval_training']['best_epoch']=3
store['active_learning_steps'][16]['acquisition']={'indices': [['id', 45757], ['id', 55642], ['id', 15242], ['id', 34429], ['id', 45560]], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.9224277137505468, 1.6588461016328628, 2.1486821830723395, 2.4706713596608756, 2.6735796879682177]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 1.5818591117858887})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 2.054183006286621})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 2.1443541049957275})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 2.5855801105499268})
store['active_learning_steps'][17]['training']['best_epoch']=1
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.6066, 'crossentropy': 1.6515044921875}
store['active_learning_steps'][17]['eval_training']={}
store['active_learning_steps'][17]['eval_training']['epochs']=[]
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 1.2931420803070068})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 1.2443268299102783})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 1.2135019302368164})
store['active_learning_steps'][17]['eval_training']['best_epoch']=3
store['active_learning_steps'][17]['acquisition']={'indices': [['id', 42919], ['id', 55318], ['id', 25365], ['id', 54813], ['id', 50776]], 'labels': [-1, -1, -1, 8, -1], 'scores': [0.8006259970199914, 1.4061950483247863, 1.923437638785269, 2.2802575108410323, 2.4988945231569275]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.603515625, 'crossentropy': 1.7635619640350342})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 2.151909828186035})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 2.495283603668213})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 2.4642014503479004})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 2.8308939933776855})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 3.147052049636841})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 3.019843578338623})
store['active_learning_steps'][18]['training']['best_epoch']=4
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.614, 'crossentropy': 2.7406150390625}
store['active_learning_steps'][18]['eval_training']={}
store['active_learning_steps'][18]['eval_training']['epochs']=[]
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 1.613753080368042})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 1.837629795074463})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 1.6995704174041748})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 1.7746634483337402})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 1.6204564571380615})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 1.6804828643798828})
store['active_learning_steps'][18]['eval_training']['best_epoch']=3
store['active_learning_steps'][18]['acquisition']={'indices': [['id', 8890], ['id', 6672], ['id', 15384], ['id', 43898], ['id', 1885]], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.9053234557396881, 1.6305151766299204, 2.1652686787154765, 2.4384384109336583, 2.606678508700072]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 1.5052424669265747})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 2.277087688446045})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 2.4008383750915527})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 2.6121435165405273})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 2.8145577907562256})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 2.8745241165161133})
store['active_learning_steps'][19]['training']['best_epoch']=3
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.6228, 'crossentropy': 2.51541640625}
store['active_learning_steps'][19]['eval_training']={}
store['active_learning_steps'][19]['eval_training']['epochs']=[]
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 1.3651657104492188})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 1.6580439805984497})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 1.5224385261535645})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 1.4402132034301758})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 1.4429757595062256})
store['active_learning_steps'][19]['eval_training']['best_epoch']=5
store['active_learning_steps'][19]['acquisition']={'indices': [['id', 38214], ['id', 45268], ['id', 39267], ['id', 20894], ['id', 25566]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.1137501750098533, 1.9060431608132862, 2.4283315759894526, 2.807517000746905, 3.0125993950708843]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 1.5296001434326172})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 1.9193187952041626})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 2.4831442832946777})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 2.651798725128174})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 2.9320337772369385})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 2.9170937538146973})
store['active_learning_steps'][20]['training']['best_epoch']=3
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.6181, 'crossentropy': 2.5467708984375}
store['active_learning_steps'][20]['eval_training']={}
store['active_learning_steps'][20]['eval_training']['epochs']=[]
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.5986328125, 'crossentropy': 1.38459050655365})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 1.490748405456543})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 1.4827675819396973})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 1.4557902812957764})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 1.5028051137924194})
store['active_learning_steps'][20]['eval_training']['best_epoch']=5
store['active_learning_steps'][20]['acquisition']={'indices': [['id', 49434], ['id', 50796], ['id', 53000], ['id', 15946], ['id', 10992]], 'labels': [-1, -1, -1, -1, 5], 'scores': [0.950855527407131, 1.7342968171813224, 2.243747404001891, 2.61089765673922, 2.831891115828472]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 1.5564793348312378})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 2.250919818878174})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 2.5398426055908203})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 2.8045215606689453})
store['active_learning_steps'][21]['training']['best_epoch']=1
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.627, 'crossentropy': 1.61637578125}
store['active_learning_steps'][21]['eval_training']={}
store['active_learning_steps'][21]['eval_training']['epochs']=[]
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 1.2212430238723755})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 1.1950520277023315})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 1.1677311658859253})
store['active_learning_steps'][21]['eval_training']['best_epoch']=2
store['active_learning_steps'][21]['acquisition']={'indices': [['id', 9091], ['id', 55997], ['id', 21983], ['id', 42454], ['id', 57645]], 'labels': [-1, -1, -1, -1, 2], 'scores': [0.8095863277778061, 1.3578283518789247, 1.749388431364543, 2.021882929141065, 2.1999876128181555]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 1.4379489421844482})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 1.9989781379699707})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 2.650496482849121})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 2.534191370010376})
store['active_learning_steps'][22]['training']['best_epoch']=1
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.6365, 'crossentropy': 1.52323876953125}
store['active_learning_steps'][22]['eval_training']={}
store['active_learning_steps'][22]['eval_training']['epochs']=[]
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 1.1950771808624268})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 1.165362000465393})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 1.16749107837677})
store['active_learning_steps'][22]['eval_training']['best_epoch']=1
store['active_learning_steps'][22]['acquisition']={'indices': [['id', 21844], ['id', 8387], ['id', 10956], ['id', 33877], ['id', 21901]], 'labels': [-1, 2, 8, -1, 0], 'scores': [0.6682566107830332, 1.1939600071257699, 1.5400394268131317, 1.7885497173702056, 1.9598807426597222]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 1.4887244701385498})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 1.732848048210144})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 2.123659133911133})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 2.0028138160705566})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 2.2684133052825928})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 2.498709201812744})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 2.487290859222412})
store['active_learning_steps'][23]['training']['best_epoch']=4
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.6589, 'crossentropy': 2.1165080078125}
store['active_learning_steps'][23]['eval_training']={}
store['active_learning_steps'][23]['eval_training']['epochs']=[]
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 1.49152672290802})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 1.4880329370498657})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 1.5005269050598145})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 1.4190418720245361})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 1.462912678718567})
store['active_learning_steps'][23]['eval_training']['best_epoch']=2
store['active_learning_steps'][23]['acquisition']={'indices': [['id', 23352], ['id', 29900], ['id', 20226], ['id', 12482], ['id', 25216]], 'labels': [-1, -1, -1, 0, 0], 'scores': [0.8392679154665093, 1.446486821580913, 1.9483508791829343, 2.351027869101139, 2.597761242540636]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 1.336991548538208})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 1.929499626159668})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 2.093113899230957})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 2.207240581512451})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 2.206099510192871})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 2.4175455570220947})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 2.503018856048584})
store['active_learning_steps'][24]['training']['best_epoch']=4
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.6462, 'crossentropy': 2.3944875}
store['active_learning_steps'][24]['eval_training']={}
store['active_learning_steps'][24]['eval_training']['epochs']=[]
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 1.2731856107711792})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 1.2535068988800049})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 1.3474788665771484})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 1.3534555435180664})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 1.3909112215042114})
store['active_learning_steps'][24]['eval_training']['best_epoch']=2
store['active_learning_steps'][24]['acquisition']={'indices': [['id', 35051], ['id', 28512], ['id', 46730], ['id', 42476], ['id', 50904]], 'labels': [-1, -1, 2, -1, -1], 'scores': [0.9021874466352808, 1.6514422231850485, 2.1959507592414758, 2.50509255844352, 2.631238626562606]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 1.4237189292907715})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 2.0068929195404053})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 2.1469082832336426})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 2.5707592964172363})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 2.350311279296875})
store['active_learning_steps'][25]['training']['best_epoch']=2
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.6594, 'crossentropy': 2.113204296875}
store['active_learning_steps'][25]['eval_training']={}
store['active_learning_steps'][25]['eval_training']['epochs']=[]
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 1.3674423694610596})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 1.314692735671997})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 1.2053409814834595})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 1.22812819480896})
store['active_learning_steps'][25]['eval_training']['best_epoch']=3
store['active_learning_steps'][25]['acquisition']={'indices': [['id', 15734], ['id', 166], ['id', 23372], ['id', 24275], ['id', 4729]], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.9112368086599145, 1.6421942129967784, 2.078090982597962, 2.311522125118763, 2.450038740570273]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 1.3884488344192505})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 1.6519020795822144})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 1.929717779159546})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 1.9999594688415527})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 2.1035261154174805})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 2.3353147506713867})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 2.6215426921844482})
store['active_learning_steps'][26]['training']['best_epoch']=4
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.6679, 'crossentropy': 2.22167109375}
store['active_learning_steps'][26]['eval_training']={}
store['active_learning_steps'][26]['eval_training']['epochs']=[]
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 1.4353737831115723})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 1.2943915128707886})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 1.3727425336837769})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 1.312964916229248})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 1.283799409866333})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 1.268215298652649})
store['active_learning_steps'][26]['eval_training']['best_epoch']=3
store['active_learning_steps'][26]['acquisition']={'indices': [['id', 37083], ['id', 20320], ['id', 40874], ['id', 13495], ['id', 42737]], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.8367754876488989, 1.4841065377269653, 1.9682127193128294, 2.310826306842949, 2.5455011325683685]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 1.4293463230133057})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 1.991995096206665})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 1.990539789199829})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 2.2281672954559326})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 2.4418556690216064})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 2.3337388038635254})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 2.610978603363037})
store['active_learning_steps'][27]['training']['best_epoch']=4
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.6621, 'crossentropy': 2.26639765625}
store['active_learning_steps'][27]['eval_training']={}
store['active_learning_steps'][27]['eval_training']['epochs']=[]
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 1.4405412673950195})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 1.393334150314331})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 1.3815271854400635})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 1.4551842212677002})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 1.523442268371582})
store['active_learning_steps'][27]['eval_training']['best_epoch']=2
store['active_learning_steps'][27]['acquisition']={'indices': [['id', 42390], ['id', 51568], ['id', 59383], ['id', 51974], ['id', 9565]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.0609173797579032, 1.8539516830086296, 2.3745408607982337, 2.70396528852394, 2.8675030601619187]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 1.6203172206878662})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 1.8259165287017822})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 2.181020736694336})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 2.4571452140808105})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 2.543740749359131})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 2.985565185546875})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 3.3128933906555176})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 2.7564728260040283})
store['active_learning_steps'][28]['training']['best_epoch']=5
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.658, 'crossentropy': 2.6101072265625}
store['active_learning_steps'][28]['eval_training']={}
store['active_learning_steps'][28]['eval_training']['epochs']=[]
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 1.328033208847046})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 1.5122783184051514})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 1.4898004531860352})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 1.5650193691253662})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 1.4533978700637817})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 1.4583256244659424})
store['active_learning_steps'][28]['eval_training']['best_epoch']=3
store['active_learning_steps'][28]['acquisition']={'indices': [['id', 1314], ['id', 27194], ['id', 41224], ['id', 39008], ['id', 7720]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.0445712663037783, 1.83627356901829, 2.3723552969922124, 2.6946635177699516, 2.86146427527792]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 1.5353351831436157})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 1.9817181825637817})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 2.236793279647827})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 2.5493712425231934})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 2.787020206451416})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 2.6031532287597656})
store['active_learning_steps'][29]['training']['best_epoch']=3
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.6472, 'crossentropy': 2.1982728515625}
store['active_learning_steps'][29]['eval_training']={}
store['active_learning_steps'][29]['eval_training']['epochs']=[]
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 1.4616165161132812})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 1.2658321857452393})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 1.3083882331848145})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 1.2160190343856812})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 1.1645843982696533})
store['active_learning_steps'][29]['eval_training']['best_epoch']=3
store['active_learning_steps'][29]['acquisition']={'indices': [['id', 29434], ['id', 24896], ['id', 4033], ['id', 12418], ['id', 20328]], 'labels': [-1, -1, -1, 2, 0], 'scores': [0.832573828356916, 1.4474410584813882, 1.83666856712063, 2.0681914096797565, 2.187944519494466]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 1.417801856994629})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 1.7495462894439697})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 2.1506271362304688})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 2.2094857692718506})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 2.3177053928375244})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 2.487912178039551})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 2.304220676422119})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 2.49851131439209})
store['active_learning_steps'][30]['training']['best_epoch']=5
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.6779, 'crossentropy': 2.612973828125}
store['active_learning_steps'][30]['eval_training']={}
store['active_learning_steps'][30]['eval_training']['epochs']=[]
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 1.3057788610458374})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 1.5819586515426636})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 1.6003247499465942})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 1.700958251953125})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 1.4950623512268066})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 1.559969186782837})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 1.5689464807510376})
store['active_learning_steps'][30]['eval_training']['best_epoch']=6
store['active_learning_steps'][30]['acquisition']={'indices': [['id', 55268], ['id', 13912], ['id', 45466], ['id', 18183], ['id', 45026]], 'labels': [-1, -1, -1, 0, -1], 'scores': [0.7873003532814602, 1.4472648019633398, 1.9716445768362871, 2.354759254627856, 2.567977205203271]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 1.431041955947876})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 1.8464279174804688})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 2.2481517791748047})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 2.289398193359375})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 2.72400164604187})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 2.6126482486724854})
store['active_learning_steps'][31]['training']['best_epoch']=3
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.6591, 'crossentropy': 2.3500572265625}
store['active_learning_steps'][31]['eval_training']={}
store['active_learning_steps'][31]['eval_training']['epochs']=[]
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 1.3703460693359375})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 1.4435489177703857})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 1.3965078592300415})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 1.3312147855758667})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 1.4161086082458496})
store['active_learning_steps'][31]['eval_training']['best_epoch']=3
store['active_learning_steps'][31]['acquisition']={'indices': [['id', 20276], ['id', 45422], ['id', 28773], ['id', 15716], ['id', 40518]], 'labels': [-1, -1, -1, 6, -1], 'scores': [0.7213605507914822, 1.2384485342693248, 1.6048470629465035, 1.8565214949823723, 2.0052595083545928]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 1.649510383605957})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 1.9368116855621338})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 2.240466833114624})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 2.74159836769104})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 2.9512879848480225})
store['active_learning_steps'][32]['training']['best_epoch']=2
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.6564, 'crossentropy': 2.09121015625}
store['active_learning_steps'][32]['eval_training']={}
store['active_learning_steps'][32]['eval_training']['epochs']=[]
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 1.315306305885315})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 1.359449863433838})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 1.2819902896881104})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 1.3272480964660645})
store['active_learning_steps'][32]['eval_training']['best_epoch']=3
store['active_learning_steps'][32]['acquisition']={'indices': [['id', 28931], ['id', 44066], ['id', 9022], ['id', 22112], ['id', 30903]], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.974862563768558, 1.7233478567472624, 2.19817249652601, 2.479209238471393, 2.640166078496839]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 1.6297178268432617})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 1.767232894897461})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 2.171003818511963})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 2.2629358768463135})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 2.304666042327881})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 2.3374850749969482})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 2.590085029602051})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 2.668595790863037})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 2.438215732574463})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 2.5919299125671387})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 2.611191749572754})
store['active_learning_steps'][33]['training']['best_epoch']=8
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.6685, 'crossentropy': 2.737598828125}
store['active_learning_steps'][33]['eval_training']={}
store['active_learning_steps'][33]['eval_training']['epochs']=[]
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 1.490321397781372})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 1.8280079364776611})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 1.8427969217300415})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 1.9775259494781494})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 1.9189492464065552})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 1.8388340473175049})
store['active_learning_steps'][33]['eval_training']['best_epoch']=3
store['active_learning_steps'][33]['acquisition']={'indices': [['id', 47463], ['id', 59368], ['id', 8489], ['id', 30322], ['id', 4968]], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.8842269283705483, 1.657012593468877, 2.2474645255709502, 2.663527395874373, 2.916948697562446]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 1.499607801437378})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 1.8540737628936768})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 2.1644532680511475})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 2.5049352645874023})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 2.3128042221069336})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 2.6590476036071777})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 2.7595300674438477})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 2.752272605895996})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 2.90631365776062})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 2.999427318572998})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 2.9736790657043457})
store['active_learning_steps'][34]['training']['best_epoch']=8
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.6612, 'crossentropy': 2.9719150390625}
store['active_learning_steps'][34]['eval_training']={}
store['active_learning_steps'][34]['eval_training']['epochs']=[]
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 1.3837578296661377})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 1.6225230693817139})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 1.7048304080963135})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 1.669951319694519})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 1.5708799362182617})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 1.6536614894866943})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 1.676215648651123})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 1.4975481033325195})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 1.6426390409469604})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 1.6563048362731934})
store['active_learning_steps'][34]['eval_training']['best_epoch']=8
store['active_learning_steps'][34]['acquisition']={'indices': [['id', 22364], ['id', 19574], ['id', 325], ['id', 5430], ['id', 9396]], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.9711398526362054, 1.76606709335813, 2.3313443401912224, 2.7052785563914945, 2.936068951638107]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 1.396585464477539})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 1.7433621883392334})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 2.3052337169647217})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 2.3985390663146973})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 2.3534553050994873})
store['active_learning_steps'][35]['training']['best_epoch']=2
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.6495, 'crossentropy': 1.8670091796875}
store['active_learning_steps'][35]['eval_training']={}
store['active_learning_steps'][35]['eval_training']['epochs']=[]
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 1.3085877895355225})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 1.1752634048461914})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 1.171555519104004})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 1.1706910133361816})
store['active_learning_steps'][35]['eval_training']['best_epoch']=1
store['active_learning_steps'][35]['acquisition']={'indices': [['id', 41998], ['id', 37707], ['id', 18598], ['id', 14771], ['id', 36062]], 'labels': [-1, -1, -1, -1, 9], 'scores': [0.7762387561028163, 1.3101904896206125, 1.664874919399991, 1.8713050784996126, 1.977258761197504]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 1.5535321235656738})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 2.189635992050171})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 2.274202346801758})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 2.5617237091064453})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 2.721026659011841})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 2.7948553562164307})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 2.8901641368865967})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 2.822519302368164})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 2.6880836486816406})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 2.959758758544922})
store['active_learning_steps'][36]['training']['best_epoch']=7
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.6573, 'crossentropy': 2.9972298828125}
store['active_learning_steps'][36]['eval_training']={}
store['active_learning_steps'][36]['eval_training']['epochs']=[]
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 1.4619436264038086})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 1.6369459629058838})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 1.7516919374465942})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 1.712888479232788})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 1.8075155019760132})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 1.6563160419464111})
store['active_learning_steps'][36]['eval_training']['best_epoch']=3
store['active_learning_steps'][36]['acquisition']={'indices': [['id', 31988], ['id', 33634], ['id', 59100], ['id', 46775], ['id', 34322]], 'labels': [-1, -1, 1, 8, -1], 'scores': [0.877401725145601, 1.5350655726785343, 2.039908398871149, 2.385695186054181, 2.6091744363993143]}
store['active_learning_steps'].append({})
store['active_learning_steps'][37]['training']={}
store['active_learning_steps'][37]['training']['epochs']=[]
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 1.5046885013580322})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 1.5301856994628906})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 2.3117308616638184})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 2.1366896629333496})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 2.502617120742798})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 2.76497745513916})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 2.6378133296966553})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 2.6072452068328857})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 3.086240530014038})
store['active_learning_steps'][37]['training']['best_epoch']=6
store['active_learning_steps'][37]['evaluation_metrics']={'accuracy': 0.6731, 'crossentropy': 2.6322201171875}
store['active_learning_steps'][37]['eval_training']={}
store['active_learning_steps'][37]['eval_training']['epochs']=[]
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 1.5457723140716553})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 1.5631203651428223})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 1.5234167575836182})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 1.583129644393921})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 1.6038098335266113})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 1.4990625381469727})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 1.5432852506637573})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 1.575137972831726})
store['active_learning_steps'][37]['eval_training']['best_epoch']=5
store['active_learning_steps'][37]['acquisition']={'indices': [['id', 36227], ['id', 39655], ['id', 58611], ['id', 40427], ['id', 22643]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.0736645323757237, 1.812883429025914, 2.3488872679532715, 2.684353472884954, 2.8726140844600017]}
store['active_learning_steps'].append({})
store['active_learning_steps'][38]['training']={}
store['active_learning_steps'][38]['training']['epochs']=[]
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 1.5226554870605469})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 1.777018666267395})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 1.8835078477859497})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 2.3489203453063965})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 2.522984266281128})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 2.4170656204223633})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 2.6871252059936523})
store['active_learning_steps'][38]['training']['best_epoch']=4
store['active_learning_steps'][38]['evaluation_metrics']={'accuracy': 0.6676, 'crossentropy': 2.4805654296875}
store['active_learning_steps'][38]['eval_training']={}
store['active_learning_steps'][38]['eval_training']['epochs']=[]
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 1.3874493837356567})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 1.5661370754241943})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 1.4765353202819824})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 1.488377571105957})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 1.4736216068267822})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 1.4162874221801758})
store['active_learning_steps'][38]['eval_training']['best_epoch']=3
store['active_learning_steps'][38]['acquisition']={'indices': [['id', 5759], ['id', 25026], ['id', 48323], ['id', 37358], ['id', 17415]], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.8628771377761442, 1.5393224764778726, 2.030206886659636, 2.341800815196571, 2.4952004075733365]}
store['active_learning_steps'].append({})
store['active_learning_steps'][39]['training']={}
store['active_learning_steps'][39]['training']['epochs']=[]
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 1.3388869762420654})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 1.8232073783874512})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 2.230703830718994})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 2.251260280609131})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 2.3464343547821045})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 2.555518865585327})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 2.592015266418457})
store['active_learning_steps'][39]['training']['best_epoch']=4
store['active_learning_steps'][39]['evaluation_metrics']={'accuracy': 0.6853, 'crossentropy': 2.3669953125}
store['active_learning_steps'][39]['eval_training']={}
store['active_learning_steps'][39]['eval_training']['epochs']=[]
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 1.462153673171997})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 1.5136761665344238})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 1.4598966836929321})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 1.4414114952087402})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 1.4011611938476562})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 1.5366406440734863})
store['active_learning_steps'][39]['eval_training']['best_epoch']=5
store['active_learning_steps'][39]['acquisition']={'indices': [['id', 56805], ['id', 55139], ['id', 22041], ['id', 6846], ['id', 13685]], 'labels': [-1, -1, -1, 5, -1], 'scores': [0.9406899520914904, 1.6354926874367637, 2.1121064915489085, 2.4283824765798125, 2.6263937430062194]}
store['active_learning_steps'].append({})
store['active_learning_steps'][40]['training']={}
store['active_learning_steps'][40]['training']['epochs']=[]
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 1.3454792499542236})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 1.654581069946289})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 2.136892318725586})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 2.1699705123901367})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 2.0899479389190674})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 2.7208051681518555})
store['active_learning_steps'][40]['training']['best_epoch']=3
store['active_learning_steps'][40]['evaluation_metrics']={'accuracy': 0.6726, 'crossentropy': 2.1485787109375}
store['active_learning_steps'][40]['eval_training']={}
store['active_learning_steps'][40]['eval_training']['epochs']=[]
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 1.4295506477355957})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 1.3769136667251587})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 1.3863952159881592})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 1.3029018640518188})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 1.3385902643203735})
store['active_learning_steps'][40]['eval_training']['best_epoch']=5
store['active_learning_steps'][40]['acquisition']={'indices': [['id', 40883], ['id', 59652], ['id', 5893], ['id', 34557], ['id', 17654]], 'labels': [-1, -1, 8, -1, 6], 'scores': [0.9424147142629185, 1.6148339499794657, 2.0886428515288014, 2.3805980678945176, 2.5651401036293278]}
store['active_learning_steps'].append({})
store['active_learning_steps'][41]['training']={}
store['active_learning_steps'][41]['training']['epochs']=[]
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 1.397728443145752})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 1.7697160243988037})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 2.011145830154419})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 2.2010698318481445})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 2.2933287620544434})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 2.251786708831787})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 2.6007649898529053})
store['active_learning_steps'][41]['training']['best_epoch']=4
store['active_learning_steps'][41]['evaluation_metrics']={'accuracy': 0.6709, 'crossentropy': 2.209087890625}
store['active_learning_steps'][41]['eval_training']={}
store['active_learning_steps'][41]['eval_training']['epochs']=[]
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 1.3870452642440796})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 1.3424266576766968})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 1.3746999502182007})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 1.370342493057251})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 1.2811169624328613})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 1.2642532587051392})
store['active_learning_steps'][41]['eval_training']['best_epoch']=4
store['active_learning_steps'][41]['acquisition']={'indices': [['id', 44983], ['id', 10676], ['id', 41913], ['id', 1306], ['id', 15054]], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.9333349136344686, 1.6723583877829957, 2.2411083241127305, 2.5735198144678, 2.7359392767758077]}
store['active_learning_steps'].append({})
store['active_learning_steps'][42]['training']={}
store['active_learning_steps'][42]['training']['epochs']=[]
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 1.5538263320922852})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 1.8855681419372559})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 1.905776023864746})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 2.3486063480377197})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 2.2793426513671875})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 2.461920738220215})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 2.4602131843566895})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 2.7501320838928223})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 2.4819223880767822})
store['active_learning_steps'][42]['training']['best_epoch']=6
store['active_learning_steps'][42]['evaluation_metrics']={'accuracy': 0.6809, 'crossentropy': 2.562902734375}
store['active_learning_steps'][42]['eval_training']={}
store['active_learning_steps'][42]['eval_training']['epochs']=[]
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 1.4228153228759766})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 1.4980931282043457})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 1.4951261281967163})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 1.5555427074432373})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 1.4395594596862793})
store['active_learning_steps'][42]['eval_training']['best_epoch']=2
store['active_learning_steps'][42]['acquisition']={'indices': [['id', 36471], ['id', 20752], ['id', 51231], ['id', 52981], ['id', 30442]], 'labels': [-1, -1, 5, 0, 6], 'scores': [0.8332265090864286, 1.476041640337499, 1.9151118477332307, 2.16608186531817, 2.2966250623815716]}
store['active_learning_steps'].append({})
store['active_learning_steps'][43]['training']={}
store['active_learning_steps'][43]['training']['epochs']=[]
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 1.538593053817749})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 1.729491114616394})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 2.0559263229370117})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 2.2496137619018555})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 2.503122568130493})
store['active_learning_steps'][43]['training']['best_epoch']=2
store['active_learning_steps'][43]['evaluation_metrics']={'accuracy': 0.6728, 'crossentropy': 1.8980650390625}
store['active_learning_steps'][43]['eval_training']={}
store['active_learning_steps'][43]['eval_training']['epochs']=[]
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 1.4394245147705078})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 1.2666802406311035})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 1.2396504878997803})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 1.1829661130905151})
store['active_learning_steps'][43]['eval_training']['best_epoch']=4
store['active_learning_steps'][43]['acquisition']={'indices': [['id', 21493], ['id', 8047], ['id', 21896], ['id', 19390], ['id', 30247]], 'labels': [-1, -1, -1, -1, 8], 'scores': [0.7774743952053571, 1.4353327712875483, 1.9270361001172738, 2.1953386513044677, 2.389277804714709]}
store['active_learning_steps'].append({})
store['active_learning_steps'][44]['training']={}
store['active_learning_steps'][44]['training']['epochs']=[]
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 1.5391149520874023})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 1.7745997905731201})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 1.9707140922546387})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 2.0946757793426514})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 2.145869255065918})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 2.619842052459717})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 2.4079160690307617})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 2.455810546875})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 2.346452474594116})
store['active_learning_steps'][44]['training']['best_epoch']=6
store['active_learning_steps'][44]['evaluation_metrics']={'accuracy': 0.68, 'crossentropy': 2.6203947265625}
store['active_learning_steps'][44]['eval_training']={}
store['active_learning_steps'][44]['eval_training']['epochs']=[]
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 1.4718906879425049})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 1.509199619293213})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 1.4907951354980469})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 1.6392003297805786})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 1.541776418685913})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 1.5208191871643066})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.5569112300872803})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 1.5531466007232666})
store['active_learning_steps'][44]['eval_training']['best_epoch']=6
store['active_learning_steps'][44]['acquisition']={'indices': [['id', 39655], ['id', 27113], ['id', 48221], ['id', 25624], ['id', 21504]], 'labels': [-1, -1, -1, 5, -1], 'scores': [0.8961807218192013, 1.7178415540095298, 2.256256117404406, 2.6025861448211254, 2.8065111085784697]}
store['active_learning_steps'].append({})
store['active_learning_steps'][45]['training']={}
store['active_learning_steps'][45]['training']['epochs']=[]
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 1.461101770401001})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 1.877586007118225})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 2.2114462852478027})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 2.290703296661377})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 2.497378349304199})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 2.276746988296509})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 2.446739912033081})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 2.5701637268066406})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 2.934657096862793})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 2.8860368728637695})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 2.5163381099700928})
store['active_learning_steps'][45]['training']['best_epoch']=8
store['active_learning_steps'][45]['evaluation_metrics']={'accuracy': 0.6805, 'crossentropy': 2.705435546875}
store['active_learning_steps'][45]['eval_training']={}
store['active_learning_steps'][45]['eval_training']['epochs']=[]
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 1.264840841293335})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 1.3627004623413086})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 1.4998226165771484})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 1.4811415672302246})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 1.3779706954956055})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 1.4953389167785645})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 1.3998782634735107})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 1.3764864206314087})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.460869312286377})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 1.4499841928482056})
store['active_learning_steps'][45]['eval_training']['best_epoch']=8
store['active_learning_steps'][45]['acquisition']={'indices': [['id', 55278], ['id', 5943], ['id', 7782], ['id', 27591], ['id', 39414]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.1451993061236552, 2.0906141783275425, 2.674653381451795, 3.0483576800797003, 3.2963749380334906]}
store['active_learning_steps'].append({})
store['active_learning_steps'][46]['training']={}
store['active_learning_steps'][46]['training']['epochs']=[]
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 1.4195153713226318})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 1.6819720268249512})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 2.0785083770751953})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 2.127657413482666})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 2.1133391857147217})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 2.3518340587615967})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 2.554771900177002})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 2.5503058433532715})
store['active_learning_steps'][46]['training']['best_epoch']=5
store['active_learning_steps'][46]['evaluation_metrics']={'accuracy': 0.678, 'crossentropy': 2.120694921875}
store['active_learning_steps'][46]['eval_training']={}
store['active_learning_steps'][46]['eval_training']['epochs']=[]
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 1.4850637912750244})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 1.39854097366333})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 1.4323173761367798})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 1.3459917306900024})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 1.320814847946167})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.2916259765625})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 1.2368770837783813})
store['active_learning_steps'][46]['eval_training']['best_epoch']=7
store['active_learning_steps'][46]['acquisition']={'indices': [['id', 27655], ['id', 55659], ['id', 13018], ['id', 37318], ['id', 12188]], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.9255749421654222, 1.6787526943490088, 2.1909634372989872, 2.538879696641924, 2.7339378522628577]}
store['active_learning_steps'].append({})
store['active_learning_steps'][47]['training']={}
store['active_learning_steps'][47]['training']['epochs']=[]
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 1.2968873977661133})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 1.6809018850326538})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 1.7477142810821533})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 1.9738678932189941})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 2.02117919921875})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 2.1743650436401367})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 2.3336920738220215})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 2.436917304992676})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 2.3353347778320312})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 2.3232076168060303})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 2.286735773086548})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 2.2869160175323486})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 2.606313943862915})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 2.50529408454895})
store['active_learning_steps'][47]['training']['best_epoch']=11
store['active_learning_steps'][47]['evaluation_metrics']={'accuracy': 0.6881, 'crossentropy': 2.581524609375}
store['active_learning_steps'][47]['eval_training']={}
store['active_learning_steps'][47]['eval_training']['epochs']=[]
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 1.4721888303756714})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 1.616504192352295})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 1.6587570905685425})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 1.5306490659713745})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 1.69968843460083})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 1.612030029296875})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 1.7052545547485352})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 1.8070783615112305})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 1.528637170791626})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 1.5202041864395142})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 1.5303618907928467})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 1.5046055316925049})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 1.5860297679901123})
store['active_learning_steps'][47]['eval_training']['best_epoch']=12
store['active_learning_steps'][47]['acquisition']={'indices': [['id', 19231], ['id', 19782], ['id', 34591], ['id', 29488], ['id', 50389]], 'labels': [-1, -1, -1, 9, 0], 'scores': [1.0813006164323276, 1.8935443005725427, 2.415669777353698, 2.7241772484852143, 2.9126064498490862]}
store['active_learning_steps'].append({})
store['active_learning_steps'][48]['training']={}
store['active_learning_steps'][48]['training']['epochs']=[]
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 1.4512252807617188})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 1.7142868041992188})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 1.8882858753204346})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 2.1141250133514404})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 2.374203681945801})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 2.545053005218506})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 2.527912139892578})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 2.5912201404571533})
store['active_learning_steps'][48]['training']['best_epoch']=5
store['active_learning_steps'][48]['evaluation_metrics']={'accuracy': 0.6799, 'crossentropy': 2.4120009765625}
store['active_learning_steps'][48]['eval_training']={}
store['active_learning_steps'][48]['eval_training']['epochs']=[]
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 1.3197710514068604})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 1.3807463645935059})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 1.3500393629074097})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 1.259976863861084})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 1.2742598056793213})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 1.2620999813079834})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 1.3195801973342896})
store['active_learning_steps'][48]['eval_training']['best_epoch']=6
store['active_learning_steps'][48]['acquisition']={'indices': [['id', 45089], ['id', 9552], ['id', 28211], ['id', 47895], ['id', 24533]], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.881980389407921, 1.6455774290962664, 2.2133899961804575, 2.5772606621598815, 2.838747671459739]}
store['active_learning_steps'].append({})
store['active_learning_steps'][49]['training']={}
store['active_learning_steps'][49]['training']['epochs']=[]
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 1.299701452255249})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 1.6227519512176514})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 2.038792371749878})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 2.3143422603607178})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 2.184067487716675})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 2.553439140319824})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 2.574103832244873})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 2.626406192779541})
store['active_learning_steps'][49]['training']['best_epoch']=5
store['active_learning_steps'][49]['evaluation_metrics']={'accuracy': 0.6831, 'crossentropy': 2.2794462890625}
store['active_learning_steps'][49]['eval_training']={}
store['active_learning_steps'][49]['eval_training']['epochs']=[]
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 1.365614414215088})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 1.3208826780319214})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.3534564971923828})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 1.3635838031768799})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 1.2764647006988525})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 1.2685577869415283})
store['active_learning_steps'][49]['eval_training']['best_epoch']=3
store['active_learning_steps'][49]['acquisition']={'indices': [['id', 25260], ['id', 45148], ['id', 22115], ['id', 37383], ['id', 27449]], 'labels': [-1, -1, -1, -1, 8], 'scores': [1.1257149630236218, 1.80537267006795, 2.3595858340556384, 2.6941715133616397, 2.887882935686992]}
store['active_learning_steps'].append({})
store['active_learning_steps'][50]['training']={}
store['active_learning_steps'][50]['training']['epochs']=[]
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 1.454000473022461})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 1.5484962463378906})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 1.9855291843414307})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 2.413623809814453})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 2.1776485443115234})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 2.572350025177002})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 2.535551071166992})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 2.59026837348938})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 2.550938606262207})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 2.8757171630859375})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 2.2378175258636475})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 2.9533462524414062})
store['active_learning_steps'][50]['training']['best_epoch']=9
store['active_learning_steps'][50]['evaluation_metrics']={'accuracy': 0.6842, 'crossentropy': 2.6461865234375}
store['active_learning_steps'][50]['eval_training']={}
store['active_learning_steps'][50]['eval_training']['epochs']=[]
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 1.4666996002197266})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 1.3895597457885742})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 1.548682451248169})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 1.4042450189590454})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 1.4227403402328491})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 1.4216924905776978})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 1.306384801864624})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 1.4127658605575562})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 1.372241497039795})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 1.3052397966384888})
store['active_learning_steps'][50]['eval_training']['best_epoch']=7
store['active_learning_steps'][50]['acquisition']={'indices': [['id', 45952], ['id', 20671], ['id', 44286], ['id', 770], ['id', 43211]], 'labels': [-1, -1, -1, -1, 7], 'scores': [0.9524214467844931, 1.70225481816603, 2.2049028576574354, 2.5023555047751316, 2.669895781229703]}
store['active_learning_steps'].append({})
store['active_learning_steps'][51]['training']={}
store['active_learning_steps'][51]['training']['epochs']=[]
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 1.5053846836090088})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 1.558821439743042})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 1.8932766914367676})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 2.181583881378174})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 2.199575424194336})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 2.432401657104492})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 2.5406479835510254})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 2.2650084495544434})
store['active_learning_steps'][51]['training']['best_epoch']=5
store['active_learning_steps'][51]['evaluation_metrics']={'accuracy': 0.6759, 'crossentropy': 2.404347265625}
store['active_learning_steps'][51]['eval_training']={}
store['active_learning_steps'][51]['eval_training']['epochs']=[]
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 1.2725275754928589})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 1.386554479598999})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 1.4810404777526855})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 1.2426568269729614})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 1.3820271492004395})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 1.352646827697754})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 1.321601390838623})
store['active_learning_steps'][51]['eval_training']['best_epoch']=5
store['active_learning_steps'][51]['acquisition']={'indices': [['id', 16774], ['id', 14829], ['id', 26636], ['id', 29772], ['id', 26624]], 'labels': [-1, -1, 9, -1, -1], 'scores': [0.8482013718322992, 1.5977084274779125, 2.1487247119946726, 2.5225430041681602, 2.755505864219878]}
store['active_learning_steps'].append({})
store['active_learning_steps'][52]['training']={}
store['active_learning_steps'][52]['training']['epochs']=[]
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 1.5353487730026245})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 1.5307080745697021})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 1.8925726413726807})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 2.0627031326293945})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 2.4850993156433105})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 2.297941207885742})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 2.5065386295318604})
store['active_learning_steps'][52]['training']['best_epoch']=4
store['active_learning_steps'][52]['evaluation_metrics']={'accuracy': 0.6814, 'crossentropy': 2.164198046875}
store['active_learning_steps'][52]['eval_training']={}
store['active_learning_steps'][52]['eval_training']['epochs']=[]
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 1.2582148313522339})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 1.405548334121704})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 1.2816035747528076})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 1.3099429607391357})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 1.29859459400177})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 1.2777676582336426})
store['active_learning_steps'][52]['eval_training']['best_epoch']=5
store['active_learning_steps'][52]['acquisition']={'indices': [['id', 45137], ['id', 40376], ['id', 31396], ['id', 26509], ['id', 41020]], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.9674354312837079, 1.680514009601823, 2.158318246438859, 2.4805498699826702, 2.6782585462434207]}
store['active_learning_steps'].append({})
store['active_learning_steps'][53]['training']={}
store['active_learning_steps'][53]['training']['epochs']=[]
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 1.386446237564087})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 1.637148380279541})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 1.76828932762146})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 1.8657796382904053})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 2.111018657684326})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 2.2799127101898193})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 2.2637553215026855})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 2.2765932083129883})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 2.281029224395752})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 2.3150649070739746})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 2.6555864810943604})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 2.187373161315918})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 2.4656314849853516})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 2.746192455291748})
store['active_learning_steps'][53]['training']['best_epoch']=11
store['active_learning_steps'][53]['evaluation_metrics']={'accuracy': 0.6943, 'crossentropy': 2.56070859375}
store['active_learning_steps'][53]['eval_training']={}
store['active_learning_steps'][53]['eval_training']['epochs']=[]
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 1.3251008987426758})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 1.5012985467910767})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.5446159839630127})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 1.5808110237121582})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 1.4221348762512207})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 1.6081691980361938})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 1.5037832260131836})
store['active_learning_steps'][53]['eval_training']['best_epoch']=4
store['active_learning_steps'][53]['acquisition']={'indices': [['id', 38268], ['id', 5153], ['id', 40644], ['id', 11929], ['id', 5413]], 'labels': [-1, -1, -1, -1, 2], 'scores': [1.0414706077210796, 1.824591075182248, 2.4173632508871963, 2.776841799703567, 3.0084943375970945]}
store['active_learning_steps'].append({})
store['active_learning_steps'][54]['training']={}
store['active_learning_steps'][54]['training']['epochs']=[]
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 1.371012806892395})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 1.6919090747833252})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 1.8161261081695557})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 2.10410737991333})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 2.2612462043762207})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 2.255908489227295})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 2.52797269821167})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 2.347075939178467})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 2.623084545135498})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 2.4084625244140625})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 2.478048324584961})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 2.814382791519165})
store['active_learning_steps'][54]['training']['best_epoch']=9
store['active_learning_steps'][54]['evaluation_metrics']={'accuracy': 0.6857, 'crossentropy': 2.8629044921875}
