store = {}
store['timestamp']=1621471709
store['cmdline']=['/home/kell4989/git/active_learning_redux/batchbald_redux/ood_experiment.py', '--id=18']
store['commit']='8a2cf4fb40ce306533b4e439b08268c53f009a3b'
store['github_url']='8a2cf4fb40ce306533b4e439b08268c53f009a3b'
store['experiment']='/home/kell4989/git/active_learning_redux/batchbald_redux/ood_experiment.py'
store['job_id']=18
store['worker_id']=18
store['num_workers']=80
store['config']={'seed': 1253, 'uniform_ood': False, 'id_dataset_type': 'batchbald_redux.fast_mnist.FastMNIST', 'ood_dataset_type': 'batchbald_redux.fast_mnist.FastFashionMNIST', 'initial_training_set_size': 20, 'validation_set_size': 1024, 'evaluation_set_size': 16, 'id_repetitions': 1, 'ood_repetitions': 1, 'add_dataset_noise': False, 'validation_split_random_state': 0, 'acquisition_size': 5, 'max_training_set': 200, 'num_pool_samples': 100, 'num_validation_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'min_samples_per_epoch': 5056, 'acquisition_function': 'batchbald_redux.acquisition_functions.BatchEvalBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationEvalModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 8}
store['log']={}
store['dataset_info']={'training': "(FastMNIST (train; 58976 samples)) + ('FastFashionMNIST Train (60000 samples)' | constant_target{'target': tensor(-1, device='cuda:0'), 'num_classes': 10})", 'test': "'FastMNIST Test (10000 samples)'"}
store['initial_training_set_indices']=[53434, 8533, 14640, 39579, 30392, 58125, 37915, 3091, 57520, 43803, 44119, 52296, 58226, 40334, 46037, 22015, 22304, 43812, 12640, 53689]
store['evaluation_set_indices']=[29974, 3792, 5573, 45567, 10508, 2728, 21423, 396, 49512, 31444]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 1.8473808765411377})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 2.1904821395874023})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 2.450857639312744})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 2.259488105773926})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 2.4438467025756836})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 2.6662120819091797})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 2.47312331199646})
store['active_learning_steps'][0]['training']['best_epoch']=4
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.7063, 'crossentropy': 2.1737583984375}
store['active_learning_steps'][0]['eval_training']={}
store['active_learning_steps'][0]['eval_training']['epochs']=[]
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 1.4636155366897583})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 1.3979547023773193})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.364556074142456})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 1.3969650268554688})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 1.4207041263580322})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 1.3709352016448975})
store['active_learning_steps'][0]['eval_training']['best_epoch']=3
store['active_learning_steps'][0]['acquisition']={'indices': [['id', 28838], ['id', 31558], ['id', 30782], ['id', 15938], ['id', 35043]], 'labels': [9, 7, 9, -1, 3], 'scores': [1.054981183873641, 1.7188468335069431, 2.2512307290035736, 2.6235218729398238, 2.860435883338911]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 2.4050121307373047})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 2.500535249710083})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 2.7673768997192383})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 2.881560802459717})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 3.2646055221557617})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 3.3820629119873047})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 3.207975387573242})
store['active_learning_steps'][1]['training']['best_epoch']=4
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.6591, 'crossentropy': 2.6748544921875}
store['active_learning_steps'][1]['eval_training']={}
store['active_learning_steps'][1]['eval_training']['epochs']=[]
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 1.7207412719726562})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 1.6777477264404297})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 1.6418088674545288})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 1.6040323972702026})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 1.5825449228286743})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 1.6389515399932861})
store['active_learning_steps'][1]['eval_training']['best_epoch']=4
store['active_learning_steps'][1]['acquisition']={'indices': [['id', 38256], ['id', 47707], ['id', 24968], ['id', 49119], ['id', 48143]], 'labels': [2, 5, 2, 7, 5], 'scores': [0.8996969994645714, 1.6480051610571564, 2.1486546605804238, 2.4985565336947486, 2.712744353025866]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 1.9955708980560303})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 2.317539691925049})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 2.8642358779907227})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 3.0172157287597656})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 3.487978458404541})
store['active_learning_steps'][2]['training']['best_epoch']=2
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.7052, 'crossentropy': 2.0432525390625}
store['active_learning_steps'][2]['eval_training']={}
store['active_learning_steps'][2]['eval_training']['epochs']=[]
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 1.4556663036346436})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 1.4594640731811523})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 1.440248966217041})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 1.4332048892974854})
store['active_learning_steps'][2]['eval_training']['best_epoch']=3
store['active_learning_steps'][2]['acquisition']={'indices': [['id', 22583], ['id', 39442], ['id', 54487], ['id', 26529], ['id', 19590]], 'labels': [0, 8, 3, 7, 5], 'scores': [0.8699074396052913, 1.52278641110142, 2.026965680765289, 2.3401254264814364, 2.5631509645053416]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 1.8906259536743164})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 2.062262773513794})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 2.1226868629455566})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 2.4771831035614014})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.71484375, 'crossentropy': 2.292555809020996})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 2.524160861968994})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 2.598391056060791})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 2.6191020011901855})
store['active_learning_steps'][3]['training']['best_epoch']=5
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.7483, 'crossentropy': 1.8925646484375}
store['active_learning_steps'][3]['eval_training']={}
store['active_learning_steps'][3]['eval_training']['epochs']=[]
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 1.4843366146087646})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 1.4168236255645752})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 1.3529890775680542})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 1.4258489608764648})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 1.447973370552063})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 1.4711060523986816})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 1.5052196979522705})
store['active_learning_steps'][3]['eval_training']['best_epoch']=4
store['active_learning_steps'][3]['acquisition']={'indices': [['id', 58114], ['id', 19369], ['id', 14645], ['id', 57602], ['id', 33830]], 'labels': [2, 0, 8, 8, 7], 'scores': [0.8459818102300103, 1.5555117476782931, 2.0604906378187864, 2.3772708862968943, 2.584861199047923]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.724609375, 'crossentropy': 1.3896758556365967})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7509765625, 'crossentropy': 1.6340770721435547})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.744140625, 'crossentropy': 1.7432315349578857})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7265625, 'crossentropy': 2.012908458709717})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7275390625, 'crossentropy': 1.8100650310516357})
store['active_learning_steps'][4]['training']['best_epoch']=2
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.7894, 'crossentropy': 1.3766890625}
store['active_learning_steps'][4]['eval_training']={}
store['active_learning_steps'][4]['eval_training']['epochs']=[]
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 1.2000153064727783})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.728515625, 'crossentropy': 1.1570651531219482})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.72265625, 'crossentropy': 1.1608753204345703})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.740234375, 'crossentropy': 1.1102287769317627})
store['active_learning_steps'][4]['eval_training']['best_epoch']=4
store['active_learning_steps'][4]['acquisition']={'indices': [['id', 57994], ['id', 3694], ['id', 34040], ['id', 53426], ['id', 30332]], 'labels': [6, 4, 8, 4, 6], 'scores': [0.8219047812972831, 1.4292819201621896, 1.927819851816401, 2.2497283125323557, 2.477208057077495]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 1.5302519798278809})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.73828125, 'crossentropy': 1.8241848945617676})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7353515625, 'crossentropy': 2.0160574913024902})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.755859375, 'crossentropy': 1.783851146697998})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7421875, 'crossentropy': 1.8045985698699951})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.748046875, 'crossentropy': 2.3489809036254883})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.73828125, 'crossentropy': 2.2399325370788574})
store['active_learning_steps'][5]['training']['best_epoch']=4
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.789, 'crossentropy': 1.561190234375}
store['active_learning_steps'][5]['eval_training']={}
store['active_learning_steps'][5]['eval_training']['epochs']=[]
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.7314453125, 'crossentropy': 1.2598438262939453})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.740234375, 'crossentropy': 1.2703044414520264})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.7490234375, 'crossentropy': 1.1982580423355103})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.7373046875, 'crossentropy': 1.1532235145568848})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.7470703125, 'crossentropy': 1.0929685831069946})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.75, 'crossentropy': 1.127276062965393})
store['active_learning_steps'][5]['eval_training']['best_epoch']=6
store['active_learning_steps'][5]['acquisition']={'indices': [['id', 20820], ['id', 4066], ['id', 27177], ['id', 22772], ['id', 38319]], 'labels': [9, 1, 8, 9, 2], 'scores': [0.8401717845468124, 1.5400564896039897, 2.0600711812784733, 2.3842110700719976, 2.53313034289192]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7333984375, 'crossentropy': 1.4549628496170044})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.736328125, 'crossentropy': 1.7004727125167847})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.73828125, 'crossentropy': 1.8330012559890747})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7353515625, 'crossentropy': 2.02410626411438})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7431640625, 'crossentropy': 2.2325878143310547})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7548828125, 'crossentropy': 1.9050637483596802})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.728515625, 'crossentropy': 2.266892910003662})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.755859375, 'crossentropy': 2.1689505577087402})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7548828125, 'crossentropy': 1.959252119064331})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7421875, 'crossentropy': 2.3843190670013428})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7421875, 'crossentropy': 2.1646063327789307})
store['active_learning_steps'][6]['training']['best_epoch']=8
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.7804, 'crossentropy': 1.8279322265625}
store['active_learning_steps'][6]['eval_training']={}
store['active_learning_steps'][6]['eval_training']['epochs']=[]
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.7275390625, 'crossentropy': 1.233351707458496})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.7431640625, 'crossentropy': 1.3061549663543701})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.75, 'crossentropy': 1.2457889318466187})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.75, 'crossentropy': 1.3753288984298706})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.744140625, 'crossentropy': 1.4261300563812256})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.7412109375, 'crossentropy': 1.457322597503662})
store['active_learning_steps'][6]['eval_training']['best_epoch']=3
store['active_learning_steps'][6]['acquisition']={'indices': [['id', 38989], ['id', 244], ['id', 20171], ['id', 14819], ['id', 34833]], 'labels': [3, 5, 5, 2, 2], 'scores': [0.8371800484589964, 1.5773762635180169, 2.180153414968016, 2.540392024882779, 2.777877388338779]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 1.4331426620483398})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7431640625, 'crossentropy': 1.7545018196105957})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7333984375, 'crossentropy': 2.0322108268737793})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7529296875, 'crossentropy': 1.9098844528198242})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7548828125, 'crossentropy': 2.116283655166626})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7568359375, 'crossentropy': 2.2379984855651855})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7578125, 'crossentropy': 2.225027561187744})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7490234375, 'crossentropy': 2.456512451171875})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7568359375, 'crossentropy': 2.6314899921417236})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7587890625, 'crossentropy': 2.3834829330444336})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7578125, 'crossentropy': 2.3843796253204346})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7587890625, 'crossentropy': 2.442653179168701})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7412109375, 'crossentropy': 2.6013455390930176})
store['active_learning_steps'][7]['training']['best_epoch']=10
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.7916, 'crossentropy': 1.9618390625}
store['active_learning_steps'][7]['eval_training']={}
store['active_learning_steps'][7]['eval_training']['epochs']=[]
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.7353515625, 'crossentropy': 1.3496060371398926})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.7587890625, 'crossentropy': 1.320185899734497})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.7587890625, 'crossentropy': 1.3822065591812134})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.771484375, 'crossentropy': 1.3122353553771973})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.7685546875, 'crossentropy': 1.347745418548584})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.7744140625, 'crossentropy': 1.3765757083892822})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.767578125, 'crossentropy': 1.321052074432373})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.78515625, 'crossentropy': 1.3493292331695557})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.775390625, 'crossentropy': 1.294846773147583})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.76953125, 'crossentropy': 1.2740626335144043})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.7724609375, 'crossentropy': 1.2211155891418457})
store['active_learning_steps'][7]['eval_training']['best_epoch']=8
store['active_learning_steps'][7]['acquisition']={'indices': [['id', 35161], ['id', 21529], ['id', 17545], ['id', 25960], ['id', 14797]], 'labels': [2, 8, 8, 4, 2], 'scores': [0.8583926843524678, 1.605662495363425, 2.178160866167584, 2.507883977619788, 2.7057226810833352]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 1.4118595123291016})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7216796875, 'crossentropy': 1.8663389682769775})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.736328125, 'crossentropy': 2.10272479057312})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.734375, 'crossentropy': 2.293236255645752})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7216796875, 'crossentropy': 2.612149715423584})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 2.5331711769104004})
store['active_learning_steps'][8]['training']['best_epoch']=3
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.7696, 'crossentropy': 1.7516267578125}
store['active_learning_steps'][8]['eval_training']={}
store['active_learning_steps'][8]['eval_training']['epochs']=[]
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.724609375, 'crossentropy': 1.3730926513671875})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.7529296875, 'crossentropy': 1.3019258975982666})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.763671875, 'crossentropy': 1.246311902999878})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.7490234375, 'crossentropy': 1.3492964506149292})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.76953125, 'crossentropy': 1.1494814157485962})
store['active_learning_steps'][8]['eval_training']['best_epoch']=5
store['active_learning_steps'][8]['acquisition']={'indices': [['id', 9390], ['id', 11758], ['id', 5422], ['id', 23877], ['id', 5525]], 'labels': [9, 0, 7, 3, 0], 'scores': [0.7226186788706417, 1.354225499313341, 1.8846581944581842, 2.2376307160603948, 2.5283378401372483]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 1.6437643766403198})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.728515625, 'crossentropy': 2.0148348808288574})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7373046875, 'crossentropy': 2.384267807006836})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.734375, 'crossentropy': 2.211970806121826})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.736328125, 'crossentropy': 2.623152017593384})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.73046875, 'crossentropy': 2.54227876663208})
store['active_learning_steps'][9]['training']['best_epoch']=3
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.7748, 'crossentropy': 1.88235625}
store['active_learning_steps'][9]['eval_training']={}
store['active_learning_steps'][9]['eval_training']['epochs']=[]
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.7646484375, 'crossentropy': 1.0753605365753174})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.7666015625, 'crossentropy': 1.115360975265503})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.748046875, 'crossentropy': 1.204775333404541})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.767578125, 'crossentropy': 1.1181371212005615})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.755859375, 'crossentropy': 1.1095789670944214})
store['active_learning_steps'][9]['eval_training']['best_epoch']=4
store['active_learning_steps'][9]['acquisition']={'indices': [['id', 34881], ['id', 26184], ['id', 57690], ['id', 41516], ['id', 18713]], 'labels': [7, 0, 4, 2, 2], 'scores': [0.7335335997026027, 1.3525955647673933, 1.793977034369922, 2.089006671319696, 2.2632947867377924]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 1.3533403873443604})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7666015625, 'crossentropy': 1.4775307178497314})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.767578125, 'crossentropy': 1.6146252155303955})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.76953125, 'crossentropy': 1.607818603515625})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.783203125, 'crossentropy': 1.776639461517334})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7783203125, 'crossentropy': 1.7414441108703613})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7607421875, 'crossentropy': 2.0143983364105225})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.775390625, 'crossentropy': 2.026811361312866})
store['active_learning_steps'][10]['training']['best_epoch']=5
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.8114, 'crossentropy': 1.5129873046875}
store['active_learning_steps'][10]['eval_training']={}
store['active_learning_steps'][10]['eval_training']['epochs']=[]
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.755859375, 'crossentropy': 1.134516716003418})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.7783203125, 'crossentropy': 1.042289137840271})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.7607421875, 'crossentropy': 1.141462802886963})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.78125, 'crossentropy': 1.0060076713562012})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.7841796875, 'crossentropy': 1.0044338703155518})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.7802734375, 'crossentropy': 0.9740597009658813})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.78125, 'crossentropy': 0.9470034837722778})
store['active_learning_steps'][10]['eval_training']['best_epoch']=5
store['active_learning_steps'][10]['acquisition']={'indices': [['id', 27420], ['id', 21642], ['id', 49826], ['id', 13942], ['id', 30690]], 'labels': [3, 4, 3, 4, 2], 'scores': [0.8059270245037204, 1.4473887214442356, 1.9365830071877772, 2.301190930995484, 2.5444939846647854]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.7646484375, 'crossentropy': 1.1214816570281982})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 1.2064110040664673})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8046875, 'crossentropy': 1.249070405960083})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8076171875, 'crossentropy': 1.3019671440124512})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 1.3806157112121582})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.806640625, 'crossentropy': 1.4236090183258057})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.806640625, 'crossentropy': 1.4638087749481201})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 1.6741724014282227})
store['active_learning_steps'][11]['training']['best_epoch']=5
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.838, 'crossentropy': 1.23212275390625}
store['active_learning_steps'][11]['eval_training']={}
store['active_learning_steps'][11]['eval_training']['epochs']=[]
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.716796875, 'crossentropy': 1.3651764392852783})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.771484375, 'crossentropy': 1.3973218202590942})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.7568359375, 'crossentropy': 1.3655580282211304})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.7685546875, 'crossentropy': 1.300925612449646})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.7607421875, 'crossentropy': 1.311550498008728})
store['active_learning_steps'][11]['eval_training']['best_epoch']=2
store['active_learning_steps'][11]['acquisition']={'indices': [['id', 37643], ['id', 40475], ['id', 45073], ['id', 47560], ['id', 37450]], 'labels': [3, 6, 2, 7, 4], 'scores': [0.7517858504418382, 1.435571758449881, 1.9572132353321083, 2.3432897494626523, 2.6132214647012906]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.7939453125, 'crossentropy': 0.9661228656768799})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 0.9880771636962891})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.806640625, 'crossentropy': 1.3802287578582764})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 1.0685195922851562})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 1.1229329109191895})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 1.2474775314331055})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 1.3566887378692627})
store['active_learning_steps'][12]['training']['best_epoch']=4
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.8555, 'crossentropy': 0.92537568359375}
store['active_learning_steps'][12]['eval_training']={}
store['active_learning_steps'][12]['eval_training']['epochs']=[]
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 0.9618288278579712})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 0.8880682587623596})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 0.7747554779052734})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 0.7695330381393433})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 0.7558530569076538})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 0.7259682416915894})
store['active_learning_steps'][12]['eval_training']['best_epoch']=6
store['active_learning_steps'][12]['acquisition']={'indices': [['id', 42415], ['id', 29239], ['id', 14836], ['id', 27150], ['id', 29418]], 'labels': [7, 1, 2, 2, 4], 'scores': [0.7126605371968144, 1.304877572159512, 1.7571552319160944, 2.0834624661858694, 2.2903045668924795]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.7958984375, 'crossentropy': 0.9671317338943481})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 0.9259376525878906})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.8964166641235352})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 1.068792700767517})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 1.043262004852295})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 1.152580738067627})
store['active_learning_steps'][13]['training']['best_epoch']=3
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.8725, 'crossentropy': 0.776583349609375}
store['active_learning_steps'][13]['eval_training']={}
store['active_learning_steps'][13]['eval_training']['epochs']=[]
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 0.9032391309738159})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 0.7814191579818726})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.6936097741127014})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.6759517192840576})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.6470414400100708})
store['active_learning_steps'][13]['eval_training']['best_epoch']=5
store['active_learning_steps'][13]['acquisition']={'indices': [['id', 37596], ['id', 59361], ['id', 37574], ['id', 9379], ['id', 39222]], 'labels': [7, 8, 5, 6, 3], 'scores': [0.5794410068098022, 1.102251700638222, 1.544782394024418, 1.8858419261575428, 2.1202551267275025]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 0.9545891284942627})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 0.8983702659606934})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 1.03719162940979})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 1.105159878730774})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 1.1150532960891724})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 1.178748369216919})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 1.0885863304138184})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 1.1703752279281616})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 1.114645004272461})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 1.3291852474212646})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 1.0861964225769043})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 1.1972001791000366})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 1.1491823196411133})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 1.098978042602539})
store['active_learning_steps'][14]['training']['best_epoch']=11
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.8816, 'crossentropy': 0.9154953125}
store['active_learning_steps'][14]['eval_training']={}
store['active_learning_steps'][14]['eval_training']['epochs']=[]
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 0.9259195327758789})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.8058182001113892})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.7954453229904175})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 0.8475102186203003})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.7644312381744385})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.816941499710083})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.7601224184036255})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.7083930373191833})
store['active_learning_steps'][14]['eval_training']['best_epoch']=5
store['active_learning_steps'][14]['acquisition']={'indices': [['id', 3106], ['id', 39355], ['id', 48579], ['id', 28669], ['id', 40089]], 'labels': [0, 8, 3, 4, 8], 'scores': [0.8181439076711028, 1.4746147521426987, 1.9745725493316195, 2.353418959615879, 2.627156083523473]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 0.8492971658706665})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.7785791158676147})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.7540317177772522})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.8110023140907288})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.8572361469268799})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.8174963593482971})
store['active_learning_steps'][15]['training']['best_epoch']=3
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.9049, 'crossentropy': 0.638625830078125}
store['active_learning_steps'][15]['eval_training']={}
store['active_learning_steps'][15]['eval_training']['epochs']=[]
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.798828125, 'crossentropy': 0.8966250419616699})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.6533316373825073})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.6445533633232117})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.6327840685844421})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.6122839450836182})
store['active_learning_steps'][15]['eval_training']['best_epoch']=5
store['active_learning_steps'][15]['acquisition']={'indices': [['id', 23434], ['id', 34551], ['id', 6819], ['id', 38321], ['id', 54562]], 'labels': [5, 3, -1, 3, -1], 'scores': [0.6584852192017139, 1.2510661777142449, 1.737903827498723, 2.066462405336125, 2.266258988576891]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.76953125, 'crossentropy': 1.0088891983032227})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.8018190860748291})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.7694646120071411})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.8054821491241455})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.9284787178039551})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.9146950244903564})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.8704719543457031})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 1.1448960304260254})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 1.0714894533157349})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 1.006237506866455})
store['active_learning_steps'][16]['training']['best_epoch']=7
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.8869, 'crossentropy': 0.78515166015625}
store['active_learning_steps'][16]['eval_training']={}
store['active_learning_steps'][16]['eval_training']['epochs']=[]
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.798828125, 'crossentropy': 0.9366583228111267})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.7105540037155151})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.743618369102478})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.6456989049911499})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.6629142761230469})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.646536111831665})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.6048609018325806})
store['active_learning_steps'][16]['eval_training']['best_epoch']=4
store['active_learning_steps'][16]['acquisition']={'indices': [['id', 35644], ['id', 25416], ['id', 55288], ['id', 30955], ['id', 29422]], 'labels': [2, 1, 0, 0, 8], 'scores': [0.6115376510488834, 1.1519217966050896, 1.6104675356081462, 1.9287801066347336, 2.1638350617283475]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.783203125, 'crossentropy': 0.9388205409049988})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 0.8878662586212158})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.9507481455802917})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.9044724702835083})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 1.0072779655456543})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 1.0096540451049805})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 1.113356113433838})
store['active_learning_steps'][17]['training']['best_epoch']=4
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.8746, 'crossentropy': 0.79681318359375}
store['active_learning_steps'][17]['eval_training']={}
store['active_learning_steps'][17]['eval_training']['epochs']=[]
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.8056640625, 'crossentropy': 0.8886080384254456})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 0.7674022912979126})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.6600111722946167})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.6106608510017395})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.5797820091247559})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.6354348659515381})
store['active_learning_steps'][17]['eval_training']['best_epoch']=5
store['active_learning_steps'][17]['acquisition']={'indices': [['id', 47870], ['id', 6574], ['id', 22717], ['id', 15832], ['id', 2101]], 'labels': [9, -1, 3, -1, 0], 'scores': [0.6758127314137006, 1.236655144490093, 1.6943315223306348, 2.0299142954078224, 2.269508047075859]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 0.910383939743042})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.8745143413543701})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.9020850658416748})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 1.0251516103744507})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 0.9815189242362976})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.9057997465133667})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.976166307926178})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.9984566569328308})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.9106766581535339})
store['active_learning_steps'][18]['training']['best_epoch']=6
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.8828, 'crossentropy': 0.8079662109375}
store['active_learning_steps'][18]['eval_training']={}
store['active_learning_steps'][18]['eval_training']['epochs']=[]
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.7646484375, 'crossentropy': 0.9619810581207275})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 0.7857098579406738})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.6906040906906128})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.6852422952651978})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.6502681970596313})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.6037096977233887})
store['active_learning_steps'][18]['eval_training']['best_epoch']=3
store['active_learning_steps'][18]['acquisition']={'indices': [['id', 39305], ['id', 23732], ['id', 20402], ['id', 20635], ['id', 26568]], 'labels': [7, 9, 9, 5, -1], 'scores': [0.713814449556277, 1.2775941789005407, 1.7144384168268383, 2.046204759804847, 2.2855047399805946]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 0.8736680746078491})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.7347056865692139})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.7607879638671875})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.7610510587692261})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.8382998704910278})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.8135852813720703})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.8223925828933716})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.9228708744049072})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.9471039772033691})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.9179402589797974})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.9000776410102844})
store['active_learning_steps'][19]['training']['best_epoch']=8
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.9051, 'crossentropy': 0.749921875}
store['active_learning_steps'][19]['eval_training']={}
store['active_learning_steps'][19]['eval_training']['epochs']=[]
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.8069242835044861})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.6548593640327454})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.5876673460006714})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.6403048634529114})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.6040371656417847})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.5860719680786133})
store['active_learning_steps'][19]['eval_training']['best_epoch']=3
store['active_learning_steps'][19]['acquisition']={'indices': [['id', 21219], ['id', 15873], ['id', 17065], ['id', 8403], ['id', 50930]], 'labels': [2, 5, 8, 2, 0], 'scores': [0.7477062180462261, 1.413635736464561, 1.981377362524553, 2.4057578457808617, 2.635824985585181]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 0.8861582279205322})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.7400181293487549})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.7437796592712402})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.7642806768417358})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.7779853343963623})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.8427138328552246})
store['active_learning_steps'][20]['training']['best_epoch']=3
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.9134, 'crossentropy': 0.58581767578125}
store['active_learning_steps'][20]['eval_training']={}
store['active_learning_steps'][20]['eval_training']['epochs']=[]
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 0.8322699069976807})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6109286546707153})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.6098191142082214})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.5610610842704773})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.5640618801116943})
store['active_learning_steps'][20]['eval_training']['best_epoch']=2
store['active_learning_steps'][20]['acquisition']={'indices': [['id', 45017], ['id', 4111], ['id', 34708], ['id', 35336], ['id', 610]], 'labels': [4, 2, 0, -1, 5], 'scores': [0.6236358625467866, 1.125956925818568, 1.5327170816681823, 1.8355302229028112, 2.0395516242283307]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.806640625, 'crossentropy': 0.9443135261535645})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.6947824954986572})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.816895604133606})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.8392034769058228})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.8857407569885254})
store['active_learning_steps'][21]['training']['best_epoch']=2
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.8945, 'crossentropy': 0.630029833984375}
store['active_learning_steps'][21]['eval_training']={}
store['active_learning_steps'][21]['eval_training']['epochs']=[]
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 0.8943299651145935})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.6847944259643555})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.6229026317596436})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.6602755188941956})
store['active_learning_steps'][21]['eval_training']['best_epoch']=4
store['active_learning_steps'][21]['acquisition']={'indices': [['id', 12211], ['id', 38567], ['id', 26733], ['id', 11482], ['id', 760]], 'labels': [3, 4, 2, 8, 3], 'scores': [0.6585013313810644, 1.2462538219041983, 1.7201131078322636, 2.071312664688218, 2.31332287574398]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 0.9816185235977173})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.7025660276412964})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6932405233383179})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.732113242149353})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.7803989052772522})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.8232460618019104})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.7953953146934509})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.8126108646392822})
store['active_learning_steps'][22]['training']['best_epoch']=5
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.9114, 'crossentropy': 0.67819482421875}
store['active_learning_steps'][22]['eval_training']={}
store['active_learning_steps'][22]['eval_training']['epochs']=[]
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 0.9276529550552368})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.6378244161605835})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.6422533988952637})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.603186845779419})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.591444194316864})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.5727080702781677})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.55076664686203})
store['active_learning_steps'][22]['eval_training']['best_epoch']=7
store['active_learning_steps'][22]['acquisition']={'indices': [['id', 48241], ['id', 22879], ['id', 49585], ['id', 53746], ['id', 9468]], 'labels': [7, 1, 3, 1, 6], 'scores': [0.8351868766148033, 1.470540656229041, 1.961382015964217, 2.288113116177662, 2.5246442244042147]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.7998046875, 'crossentropy': 0.8632266521453857})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.6885783076286316})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6925125122070312})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.7739953994750977})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.7776036262512207})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.8435739278793335})
store['active_learning_steps'][23]['training']['best_epoch']=3
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.9045, 'crossentropy': 0.60530029296875}
store['active_learning_steps'][23]['eval_training']={}
store['active_learning_steps'][23]['eval_training']['epochs']=[]
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.8037109375, 'crossentropy': 0.9164398312568665})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.6385986804962158})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.633980393409729})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.5610602498054504})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.6004183292388916})
store['active_learning_steps'][23]['eval_training']['best_epoch']=4
store['active_learning_steps'][23]['acquisition']={'indices': [['id', 21734], ['id', 37529], ['id', 56379], ['id', 47690], ['id', 15130]], 'labels': [5, 0, 4, 0, 0], 'scores': [0.5805517813271077, 1.0841007208754603, 1.5112066234166943, 1.8296359933002764, 2.046710463367549]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 0.8335015773773193})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.6903533935546875})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.7194904088973999})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6985223293304443})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.7200793027877808})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.730643630027771})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.79963219165802})
store['active_learning_steps'][24]['training']['best_epoch']=4
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.9151, 'crossentropy': 0.582574365234375}
store['active_learning_steps'][24]['eval_training']={}
store['active_learning_steps'][24]['eval_training']['epochs']=[]
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.796875, 'crossentropy': 0.8994239568710327})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.6770911812782288})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.5509575009346008})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.5457721948623657})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.5321539044380188})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.5094048380851746})
store['active_learning_steps'][24]['eval_training']['best_epoch']=6
store['active_learning_steps'][24]['acquisition']={'indices': [['id', 1707], ['id', 53885], ['id', 49509], ['id', 27247], ['id', 33574]], 'labels': [-1, -1, 8, -1, -1], 'scores': [0.741151193183313, 1.4077419243834055, 1.9639420745222553, 2.3182978921261395, 2.5424145460748084]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 0.8387516736984253})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.6490610241889954})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6103461384773254})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6902060508728027})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.703778862953186})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.7717602849006653})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.7157018184661865})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.8057562112808228})
store['active_learning_steps'][25]['training']['best_epoch']=5
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.9157, 'crossentropy': 0.597532275390625}
store['active_learning_steps'][25]['eval_training']={}
store['active_learning_steps'][25]['eval_training']['epochs']=[]
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 0.8545488715171814})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.6777156591415405})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.5848092436790466})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.5795125961303711})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.5390915274620056})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.5256709456443787})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.5034629106521606})
store['active_learning_steps'][25]['eval_training']['best_epoch']=7
store['active_learning_steps'][25]['acquisition']={'indices': [['id', 53872], ['id', 11075], ['id', 53019], ['id', 47403], ['id', 32311]], 'labels': [8, 3, 2, 9, -1], 'scores': [0.7035971567334662, 1.320284086010775, 1.8515595985106907, 2.216203813528348, 2.407844782080379]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.7822265625, 'crossentropy': 0.9841940402984619})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.8113899230957031})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.7176626920700073})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.7448471188545227})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.7448530197143555})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.8351575136184692})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.8776229619979858})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.8532013297080994})
store['active_learning_steps'][26]['training']['best_epoch']=5
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.9114, 'crossentropy': 0.64667001953125}
store['active_learning_steps'][26]['eval_training']={}
store['active_learning_steps'][26]['eval_training']['epochs']=[]
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 0.886253297328949})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.6501692533493042})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.5919684767723083})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.5352053642272949})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.5582436323165894})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.5273255109786987})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.5351346135139465})
store['active_learning_steps'][26]['eval_training']['best_epoch']=4
store['active_learning_steps'][26]['acquisition']={'indices': [['id', 37907], ['id', 50202], ['id', 54646], ['id', 828], ['id', 37538]], 'labels': [4, 5, 6, 4, 9], 'scores': [0.7689358132437929, 1.4043242468781583, 1.8897944716591186, 2.25221410676979, 2.488406563979824]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 0.9494082927703857})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.7622727155685425})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.8066359758377075})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.7226704359054565})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.7797644138336182})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.8909547328948975})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.8172774314880371})
store['active_learning_steps'][27]['training']['best_epoch']=4
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.9057, 'crossentropy': 0.602712109375}
store['active_learning_steps'][27]['eval_training']={}
store['active_learning_steps'][27]['eval_training']['epochs']=[]
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 0.9632592797279358})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.7123504281044006})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.590835452079773})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.6003468036651611})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.5669718980789185})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.5531409382820129})
store['active_learning_steps'][27]['eval_training']['best_epoch']=5
store['active_learning_steps'][27]['acquisition']={'indices': [['id', 10716], ['id', 51462], ['id', 13827], ['id', 2910], ['id', 12636]], 'labels': [7, -1, 3, -1, 6], 'scores': [0.6540010102229539, 1.230421735891213, 1.7207290962111532, 2.047053024775999, 2.289389924169466]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 0.957122266292572})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.7007418274879456})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6878317594528198})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.7038216590881348})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.7985977530479431})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.7391961812973022})
store['active_learning_steps'][28]['training']['best_epoch']=3
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.9062, 'crossentropy': 0.586549951171875}
store['active_learning_steps'][28]['eval_training']={}
store['active_learning_steps'][28]['eval_training']['epochs']=[]
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 0.9658761620521545})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.6918956637382507})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.6482349634170532})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.5977627038955688})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.601773202419281})
store['active_learning_steps'][28]['eval_training']['best_epoch']=4
store['active_learning_steps'][28]['acquisition']={'indices': [['id', 6474], ['id', 44006], ['id', 53054], ['id', 57353], ['id', 995]], 'labels': [6, 5, -1, 6, 7], 'scores': [0.6358320416828849, 1.221991012631059, 1.6984326201492421, 2.035062831886478, 2.2464376535762494]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8076171875, 'crossentropy': 0.9616451263427734})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.7529633641242981})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.7340017557144165})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.7699063420295715})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.7697349786758423})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.843848705291748})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.8507208824157715})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.9070748686790466})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.8910924196243286})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.9868240356445312})
store['active_learning_steps'][29]['training']['best_epoch']=7
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.9116, 'crossentropy': 0.65827587890625}
store['active_learning_steps'][29]['eval_training']={}
store['active_learning_steps'][29]['eval_training']['epochs']=[]
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 0.8850355744361877})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.6353574991226196})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.5556849241256714})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.548262894153595})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.5047668218612671})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.5152156949043274})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5026229619979858})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.4797093868255615})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.486094206571579})
store['active_learning_steps'][29]['eval_training']['best_epoch']=8
store['active_learning_steps'][29]['acquisition']={'indices': [['id', 43872], ['id', 18049], ['id', 11885], ['id', 39556], ['id', 23730]], 'labels': [1, 3, 8, 5, 3], 'scores': [0.8226893874882273, 1.4965364683611986, 2.034301698526543, 2.3905589214523353, 2.6055624529277672]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.771484375, 'crossentropy': 1.026440143585205})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.6805825233459473})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.7824890613555908})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.8313820362091064})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.8349161148071289})
store['active_learning_steps'][30]['training']['best_epoch']=2
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.8978, 'crossentropy': 0.58082646484375}
store['active_learning_steps'][30]['eval_training']={}
store['active_learning_steps'][30]['eval_training']['epochs']=[]
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 0.8515709638595581})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.6661422848701477})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.6279891729354858})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.6021548509597778})
store['active_learning_steps'][30]['eval_training']['best_epoch']=2
store['active_learning_steps'][30]['acquisition']={'indices': [['id', 8680], ['id', 12984], ['id', 34847], ['id', 16286], ['id', 23260]], 'labels': [8, 8, 0, 0, 7], 'scores': [0.6514331927739874, 1.1228314894126572, 1.5197536113802261, 1.8426093531596592, 2.070054415865206]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.842807412147522})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6331124305725098})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.7195963859558105})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.6982302665710449})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.7161451578140259})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.8368651866912842})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.7791683673858643})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.8125717639923096})
store['active_learning_steps'][31]['training']['best_epoch']=5
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.9163, 'crossentropy': 0.54780703125}
store['active_learning_steps'][31]['eval_training']={}
store['active_learning_steps'][31]['eval_training']['epochs']=[]
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 0.9495209455490112})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.6149126291275024})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.5792416930198669})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.5599324703216553})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.562519907951355})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.5532002449035645})
store['active_learning_steps'][31]['eval_training']['best_epoch']=3
store['active_learning_steps'][31]['acquisition']={'indices': [['id', 12934], ['id', 26577], ['id', 20037], ['id', 13494], ['id', 27431]], 'labels': [8, 2, 8, 6, 5], 'scores': [0.6471511569698869, 1.1808867235921894, 1.6359774314871478, 1.9630285553450557, 2.222333558567405]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 0.9010969400405884})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.6282966732978821})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.5879511833190918})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.661347508430481})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.7150709629058838})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.7208472490310669})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.717448353767395})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6571451425552368})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.90080726146698})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.7704446315765381})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.8387715220451355})
store['active_learning_steps'][32]['training']['best_epoch']=8
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.9212, 'crossentropy': 0.547098779296875}
store['active_learning_steps'][32]['eval_training']={}
store['active_learning_steps'][32]['eval_training']['epochs']=[]
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 0.9105585813522339})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6267786026000977})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.5958384275436401})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.5483885407447815})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.5126981139183044})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.5242373943328857})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.5071225166320801})
store['active_learning_steps'][32]['eval_training']['best_epoch']=4
store['active_learning_steps'][32]['acquisition']={'indices': [['id', 15948], ['id', 37016], ['id', 3282], ['id', 41572], ['id', 56440]], 'labels': [2, 5, -1, 6, 4], 'scores': [0.6492315245002324, 1.240323359138333, 1.7075012956126678, 2.0362801251170692, 2.2539388424790676]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 0.8662977814674377})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.6019279956817627})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.5910718441009521})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6246613264083862})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.7177259922027588})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.735353410243988})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.7349381446838379})
store['active_learning_steps'][33]['training']['best_epoch']=4
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.9173, 'crossentropy': 0.5403880859375}
store['active_learning_steps'][33]['eval_training']={}
store['active_learning_steps'][33]['eval_training']['epochs']=[]
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 0.8810966610908508})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.6456958651542664})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.556634783744812})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.5386378765106201})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.5279748439788818})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.4957640767097473})
store['active_learning_steps'][33]['eval_training']['best_epoch']=3
store['active_learning_steps'][33]['acquisition']={'indices': [['id', 44143], ['id', 9725], ['id', 11625], ['id', 8443], ['id', 58557]], 'labels': [2, 2, 8, 2, -1], 'scores': [0.698454610473624, 1.2638252247711321, 1.745275861648885, 2.073101372292646, 2.2621876755198578]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.8056640625, 'crossentropy': 0.9831247329711914})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.5975546836853027})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5814095139503479})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5343856811523438})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5679662227630615})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5950341820716858})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6171250343322754})
store['active_learning_steps'][34]['training']['best_epoch']=4
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.9343, 'crossentropy': 0.478953857421875}
store['active_learning_steps'][34]['eval_training']={}
store['active_learning_steps'][34]['eval_training']['epochs']=[]
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 0.9349920749664307})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6035585403442383})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.50822913646698})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.4746728837490082})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.46147045493125916})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.46952593326568604})
store['active_learning_steps'][34]['eval_training']['best_epoch']=6
store['active_learning_steps'][34]['acquisition']={'indices': [['id', 12196], ['id', 57221], ['id', 25420], ['id', 31921], ['id', 37307]], 'labels': [2, -1, -1, 5, 2], 'scores': [0.7952115710695298, 1.4460346609311285, 1.9536222150077842, 2.3172614809903394, 2.561861397438438]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.7900390625, 'crossentropy': 0.8789522051811218})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5927025079727173})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5256785154342651})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5133567452430725})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.5728106498718262})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6014258861541748})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6075263619422913})
store['active_learning_steps'][35]['training']['best_epoch']=4
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.9351, 'crossentropy': 0.431365771484375}
store['active_learning_steps'][35]['eval_training']={}
store['active_learning_steps'][35]['eval_training']['epochs']=[]
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 0.9604858756065369})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.5717656016349792})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.500847339630127})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.4646337926387787})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.4521157741546631})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.4169909656047821})
store['active_learning_steps'][35]['eval_training']['best_epoch']=6
store['active_learning_steps'][35]['acquisition']={'indices': [['id', 33222], ['id', 49890], ['id', 966], ['id', 55153], ['id', 4611]], 'labels': [5, 5, 3, 8, -1], 'scores': [0.6300030635478431, 1.166994967724024, 1.6055334011755704, 1.9498983190836716, 2.156833224433501]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.8056640625, 'crossentropy': 0.8935501575469971})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5479373931884766})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.5791463851928711})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6140116453170776})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6354262828826904})
store['active_learning_steps'][36]['training']['best_epoch']=2
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.9281, 'crossentropy': 0.4985650390625}
store['active_learning_steps'][36]['eval_training']={}
store['active_learning_steps'][36]['eval_training']['epochs']=[]
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.8862549662590027})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.6293264031410217})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6142556667327881})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.5864262580871582})
store['active_learning_steps'][36]['eval_training']['best_epoch']=3
store['active_learning_steps'][36]['acquisition']={'indices': [['id', 25004], ['id', 12497], ['id', 9428], ['id', 31335], ['id', 2574]], 'labels': [2, 0, 9, 5, -1], 'scores': [0.6010404802093867, 1.105751541545927, 1.5349258262195997, 1.853459134525468, 2.0904939456634235]}
store['active_learning_steps'].append({})
store['active_learning_steps'][37]['training']={}
store['active_learning_steps'][37]['training']['epochs']=[]
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 0.9674749374389648})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6159375309944153})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6094121336936951})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6049936413764954})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5239866971969604})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5715724229812622})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6085147857666016})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6237096786499023})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5690219402313232})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.6226323843002319})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6984601020812988})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.7128292322158813})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6343432068824768})
store['active_learning_steps'][37]['training']['best_epoch']=10
store['active_learning_steps'][37]['evaluation_metrics']={'accuracy': 0.9275, 'crossentropy': 0.550420263671875}
store['active_learning_steps'][37]['eval_training']={}
store['active_learning_steps'][37]['eval_training']['epochs']=[]
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 0.8779118061065674})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5481967329978943})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.4692646861076355})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.47309815883636475})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.4534028172492981})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.4311363101005554})
store['active_learning_steps'][37]['eval_training']['best_epoch']=3
store['active_learning_steps'][37]['acquisition']={'indices': [['id', 40334], ['id', 41770], ['id', 36013], ['id', 32198], ['id', 16613]], 'labels': [4, 0, -1, 5, 7], 'scores': [0.7384055198925121, 1.3512274471530734, 1.8661986775727684, 2.2459792198015167, 2.482086413255078]}
store['active_learning_steps'].append({})
store['active_learning_steps'][38]['training']={}
store['active_learning_steps'][38]['training']['epochs']=[]
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 0.8177933692932129})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6447232365608215})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5345686078071594})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5288775563240051})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6341663599014282})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6391289234161377})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6591983437538147})
store['active_learning_steps'][38]['training']['best_epoch']=4
store['active_learning_steps'][38]['evaluation_metrics']={'accuracy': 0.9277, 'crossentropy': 0.469824462890625}
store['active_learning_steps'][38]['eval_training']={}
store['active_learning_steps'][38]['eval_training']['epochs']=[]
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.7900390625, 'crossentropy': 0.9765424132347107})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.596613883972168})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5029275417327881})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.483112633228302})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.5121234655380249})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.45827656984329224})
store['active_learning_steps'][38]['eval_training']['best_epoch']=3
store['active_learning_steps'][38]['acquisition']={'indices': [['id', 9147], ['id', 57154], ['id', 33576], ['id', 11373], ['id', 37281]], 'labels': [4, 0, 9, 9, -1], 'scores': [0.5367572671349721, 1.0070185385032269, 1.4115529434213063, 1.7140763714036416, 1.9102211088513412]}
store['active_learning_steps'].append({})
store['active_learning_steps'][39]['training']={}
store['active_learning_steps'][39]['training']['epochs']=[]
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 0.9291447401046753})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.5712535977363586})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5540651082992554})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5206161141395569})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.48612838983535767})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5457180142402649})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5725536346435547})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6021664142608643})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5926668643951416})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6413811445236206})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5957307815551758})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5871334075927734})
store['active_learning_steps'][39]['training']['best_epoch']=9
store['active_learning_steps'][39]['evaluation_metrics']={'accuracy': 0.9313, 'crossentropy': 0.52893837890625}
store['active_learning_steps'][39]['eval_training']={}
store['active_learning_steps'][39]['eval_training']['epochs']=[]
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 0.9437119364738464})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.582213819026947})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5248419642448425})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.4634643495082855})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.4448341131210327})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.4479559063911438})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.4429580569267273})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.4138679504394531})
store['active_learning_steps'][39]['eval_training']['best_epoch']=5
store['active_learning_steps'][39]['acquisition']={'indices': [['id', 13554], ['id', 13588], ['id', 134], ['id', 10381], ['id', 11884]], 'labels': [8, 8, 1, -1, 9], 'scores': [0.7754837589414851, 1.4266063363969237, 1.927979062275062, 2.246082871406637, 2.441522015093815]}
store['active_learning_steps'].append({})
store['active_learning_steps'][40]['training']={}
store['active_learning_steps'][40]['training']['epochs']=[]
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.9057794809341431})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5613471269607544})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5539872646331787})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5024715065956116})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5182998776435852})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5425118207931519})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5397263765335083})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5496505498886108})
store['active_learning_steps'][40]['training']['best_epoch']=5
store['active_learning_steps'][40]['evaluation_metrics']={'accuracy': 0.9365, 'crossentropy': 0.45660029296875}
store['active_learning_steps'][40]['eval_training']={}
store['active_learning_steps'][40]['eval_training']['epochs']=[]
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.8322967290878296})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5388083457946777})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.43944284319877625})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.4344218373298645})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.3988097608089447})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.4204441010951996})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.397235244512558})
store['active_learning_steps'][40]['eval_training']['best_epoch']=5
store['active_learning_steps'][40]['acquisition']={'indices': [['id', 29832], ['id', 6466], ['id', 24424], ['id', 14521], ['id', 3676]], 'labels': [6, 2, 1, 1, 2], 'scores': [0.6530411024544265, 1.235472662170694, 1.7257720212426535, 2.067462093390108, 2.3091304963027675]}
store['active_learning_steps'].append({})
store['active_learning_steps'][41]['training']={}
store['active_learning_steps'][41]['training']['epochs']=[]
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 0.9995117783546448})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5950484275817871})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5744938850402832})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6047664880752563})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6042360067367554})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.580123245716095})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.7203034162521362})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.667180061340332})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.7611532807350159})
store['active_learning_steps'][41]['training']['best_epoch']=6
store['active_learning_steps'][41]['evaluation_metrics']={'accuracy': 0.9342, 'crossentropy': 0.48108759765625}
