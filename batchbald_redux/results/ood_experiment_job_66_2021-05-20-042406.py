store = {}
store['timestamp']=1621481046
store['cmdline']=['/home/kell4989/git/active_learning_redux/batchbald_redux/ood_experiment.py', '--id=66']
store['commit']='8a2cf4fb40ce306533b4e439b08268c53f009a3b'
store['github_url']='8a2cf4fb40ce306533b4e439b08268c53f009a3b'
store['experiment']='/home/kell4989/git/active_learning_redux/batchbald_redux/ood_experiment.py'
store['job_id']=66
store['worker_id']=66
store['num_workers']=80
store['config']={'seed': 1304, 'uniform_ood': False, 'id_dataset_type': 'batchbald_redux.fast_mnist.FastMNIST', 'ood_dataset_type': 'batchbald_redux.fast_mnist.FastFashionMNIST', 'initial_training_set_size': 20, 'validation_set_size': 1024, 'evaluation_set_size': 16, 'id_repetitions': 1, 'ood_repetitions': 1, 'add_dataset_noise': False, 'validation_split_random_state': 0, 'acquisition_size': 5, 'max_training_set': 200, 'num_pool_samples': 100, 'num_validation_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'min_samples_per_epoch': 5056, 'acquisition_function': 'batchbald_redux.acquisition_functions.BatchEvalBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationEvalModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 8}
store['log']={}
store['dataset_info']={'training': "(FastMNIST (train; 58976 samples)) + ('FastFashionMNIST Train (60000 samples)' | constant_target{'target': tensor(-1, device='cuda:0'), 'num_classes': 10})", 'test': "'FastMNIST Test (10000 samples)'"}
store['initial_training_set_indices']=[53434, 8533, 14640, 39579, 30392, 58125, 37915, 3091, 57520, 43803, 44119, 52296, 58226, 40334, 46037, 22015, 22304, 43812, 12640, 53689]
store['evaluation_set_indices']=[29974, 3792, 5573, 45567, 10508, 2728, 21423, 396, 49512, 31444]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 2.353126049041748})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 2.570887804031372})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 2.7903099060058594})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 3.0579166412353516})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 3.126091957092285})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 2.9777228832244873})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 3.0736961364746094})
store['active_learning_steps'][0]['training']['best_epoch']=4
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.6703, 'crossentropy': 2.6224712890625}
store['active_learning_steps'][0]['eval_training']={}
store['active_learning_steps'][0]['eval_training']['epochs']=[]
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 1.40083909034729})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 1.4870386123657227})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 1.4479894638061523})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 1.4058727025985718})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 1.559831976890564})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 1.5719965696334839})
store['active_learning_steps'][0]['eval_training']['best_epoch']=4
store['active_learning_steps'][0]['acquisition']={'indices': [['id', 34678], ['id', 10025], ['id', 22304], ['id', 54757], ['id', 9749]], 'labels': [8, 0, 3, 8, 8], 'scores': [1.0189865091911672, 1.7637421572582013, 2.3601058439079043, 2.748775643912185, 2.9746706141425587]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 1.9717128276824951})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 2.0054264068603516})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 2.559365749359131})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 2.5123653411865234})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 2.488250494003296})
store['active_learning_steps'][1]['training']['best_epoch']=2
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.7269, 'crossentropy': 1.9528466796875}
store['active_learning_steps'][1]['eval_training']={}
store['active_learning_steps'][1]['eval_training']['epochs']=[]
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 1.4558711051940918})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 1.3994529247283936})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 1.4449177980422974})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 1.4616034030914307})
store['active_learning_steps'][1]['eval_training']['best_epoch']=1
store['active_learning_steps'][1]['acquisition']={'indices': [['id', 8632], ['id', 14607], ['id', 33792], ['id', 8009], ['id', 39006]], 'labels': [2, 9, 4, 6, 2], 'scores': [0.7632509966806345, 1.4125196414269312, 1.8107631584289736, 2.0950142154065228, 2.295142012597916]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 2.173177719116211})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 2.461735248565674})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 2.4473350048065186})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 3.13478422164917})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 2.959134578704834})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 2.8868021965026855})
store['active_learning_steps'][2]['training']['best_epoch']=3
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.7018, 'crossentropy': 2.32672265625}
store['active_learning_steps'][2]['eval_training']={}
store['active_learning_steps'][2]['eval_training']['epochs']=[]
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 1.4325051307678223})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 1.468757152557373})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 1.5197696685791016})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 1.4501711130142212})
store['active_learning_steps'][2]['eval_training']['best_epoch']=1
store['active_learning_steps'][2]['acquisition']={'indices': [['id', 12188], ['id', 1405], ['id', 44836], ['id', 12603], ['id', 30339]], 'labels': [7, 1, 7, 2, 7], 'scores': [0.7701663421279756, 1.3781240556129033, 1.8711138131138165, 2.1661984870538227, 2.3057726174454354]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 2.013481378555298})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 2.3689677715301514})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 2.7370758056640625})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 3.045302391052246})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 2.995755910873413})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 3.188377618789673})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 2.857236862182617})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 3.071593761444092})
store['active_learning_steps'][3]['training']['best_epoch']=5
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.712, 'crossentropy': 2.797689453125}
store['active_learning_steps'][3]['eval_training']={}
store['active_learning_steps'][3]['eval_training']['epochs']=[]
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 1.5178945064544678})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 1.470844030380249})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 1.6093003749847412})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 1.581681489944458})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 1.4807796478271484})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 1.5004806518554688})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 1.5749753713607788})
store['active_learning_steps'][3]['eval_training']['best_epoch']=6
store['active_learning_steps'][3]['acquisition']={'indices': [['id', 44882], ['id', 37817], ['id', 25315], ['id', 12085], ['id', 32550]], 'labels': [9, 5, 5, 8, 0], 'scores': [0.9546319540963379, 1.7853607728608902, 2.3657144893445476, 2.7844573655822273, 3.07418751853308]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 1.622713565826416})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 2.009077548980713})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 2.226856231689453})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 2.2298102378845215})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.716796875, 'crossentropy': 2.3565618991851807})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.71484375, 'crossentropy': 2.3679168224334717})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7333984375, 'crossentropy': 2.343986988067627})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.712890625, 'crossentropy': 2.4374074935913086})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 2.556224822998047})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 2.879411220550537})
store['active_learning_steps'][4]['training']['best_epoch']=7
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.7431, 'crossentropy': 2.141621484375}
store['active_learning_steps'][4]['eval_training']={}
store['active_learning_steps'][4]['eval_training']['epochs']=[]
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.7216796875, 'crossentropy': 1.2944389581680298})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.7412109375, 'crossentropy': 1.205918788909912})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.7333984375, 'crossentropy': 1.3695893287658691})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.7236328125, 'crossentropy': 1.4377340078353882})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.7333984375, 'crossentropy': 1.2947101593017578})
store['active_learning_steps'][4]['eval_training']['best_epoch']=2
store['active_learning_steps'][4]['acquisition']={'indices': [['id', 20124], ['id', 9222], ['id', 2017], ['id', 59359], ['id', 32625]], 'labels': [6, 0, 2, 6, 0], 'scores': [0.8745999289357236, 1.650309181905178, 2.1503424567644314, 2.50625970895795, 2.7024412203987027]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7255859375, 'crossentropy': 1.5356695652008057})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7265625, 'crossentropy': 2.005014419555664})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.716796875, 'crossentropy': 2.211301326751709})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.73828125, 'crossentropy': 2.3705246448516846})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 2.4571385383605957})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7255859375, 'crossentropy': 2.2876899242401123})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 2.617954969406128})
store['active_learning_steps'][5]['training']['best_epoch']=4
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.7645, 'crossentropy': 1.976278125}
store['active_learning_steps'][5]['eval_training']={}
store['active_learning_steps'][5]['eval_training']['epochs']=[]
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 1.3281066417694092})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.7578125, 'crossentropy': 1.1921043395996094})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.728515625, 'crossentropy': 1.3061511516571045})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.73828125, 'crossentropy': 1.3066790103912354})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.73828125, 'crossentropy': 1.2601271867752075})
store['active_learning_steps'][5]['eval_training']['best_epoch']=2
store['active_learning_steps'][5]['acquisition']={'indices': [['id', 54191], ['id', 18249], ['id', 26629], ['id', 28135], ['id', 23104]], 'labels': [3, 3, 3, 2, 0], 'scores': [0.8124930200371965, 1.4742755514097186, 1.9870045494533368, 2.298546914446698, 2.4750631434673274]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 1.575890302658081})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 1.801821231842041})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.736328125, 'crossentropy': 1.936144471168518})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 2.2432055473327637})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.734375, 'crossentropy': 2.130887746810913})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 2.3299202919006348})
store['active_learning_steps'][6]['training']['best_epoch']=3
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.7697, 'crossentropy': 1.7081380859375}
store['active_learning_steps'][6]['eval_training']={}
store['active_learning_steps'][6]['eval_training']['epochs']=[]
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 1.3538663387298584})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.7265625, 'crossentropy': 1.2399158477783203})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.7412109375, 'crossentropy': 1.2734224796295166})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.7373046875, 'crossentropy': 1.1578785181045532})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.75, 'crossentropy': 1.072351098060608})
store['active_learning_steps'][6]['eval_training']['best_epoch']=5
store['active_learning_steps'][6]['acquisition']={'indices': [['id', 10038], ['id', 53754], ['id', 36818], ['id', 43899], ['id', 6314]], 'labels': [9, 6, 7, 2, 4], 'scores': [0.899717289132075, 1.5849724125675375, 2.144687427257994, 2.531194521790182, 2.776690327714671]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7822265625, 'crossentropy': 1.2259060144424438})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7734375, 'crossentropy': 1.4945154190063477})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.771484375, 'crossentropy': 1.6660076379776})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7763671875, 'crossentropy': 1.7012181282043457})
store['active_learning_steps'][7]['training']['best_epoch']=1
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.7857, 'crossentropy': 1.1653212890625}
store['active_learning_steps'][7]['eval_training']={}
store['active_learning_steps'][7]['eval_training']['epochs']=[]
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.73046875, 'crossentropy': 1.077228307723999})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.7421875, 'crossentropy': 1.0140174627304077})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.7529296875, 'crossentropy': 0.9353141188621521})
store['active_learning_steps'][7]['eval_training']['best_epoch']=3
store['active_learning_steps'][7]['acquisition']={'indices': [['id', 22661], ['id', 44383], ['id', 17756], ['id', 56286], ['id', 857]], 'labels': [2, 5, 8, 8, 3], 'scores': [0.8079163812765047, 1.4770739412026361, 1.9692431613250543, 2.338621507203772, 2.5846221128902904]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7958984375, 'crossentropy': 1.0898256301879883})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7978515625, 'crossentropy': 1.2209210395812988})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.79296875, 'crossentropy': 1.4226806163787842})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8017578125, 'crossentropy': 1.4635982513427734})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.78125, 'crossentropy': 1.58643639087677})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 1.369781255722046})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8056640625, 'crossentropy': 1.6149649620056152})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8046875, 'crossentropy': 1.4755351543426514})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7919921875, 'crossentropy': 1.5933597087860107})
store['active_learning_steps'][8]['training']['best_epoch']=6
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.8165, 'crossentropy': 1.34100888671875}
store['active_learning_steps'][8]['eval_training']={}
store['active_learning_steps'][8]['eval_training']['epochs']=[]
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.787109375, 'crossentropy': 1.0634486675262451})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.8017578125, 'crossentropy': 1.0356695652008057})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 0.9738651514053345})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 1.0034688711166382})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.791015625, 'crossentropy': 0.9412736892700195})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.8037109375, 'crossentropy': 0.9232165813446045})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.7763671875, 'crossentropy': 0.9938819408416748})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.7978515625, 'crossentropy': 0.9913374185562134})
store['active_learning_steps'][8]['eval_training']['best_epoch']=6
store['active_learning_steps'][8]['acquisition']={'indices': [['id', 17247], ['id', 48349], ['id', 7833], ['id', 45553], ['id', 21199]], 'labels': [5, 2, 5, 8, 0], 'scores': [0.750814640449374, 1.4218855267992934, 1.9908137666304282, 2.38685115968455, 2.6747851310628885]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8017578125, 'crossentropy': 1.008236289024353})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 1.1123216152191162})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 1.2195388078689575})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 1.2786813974380493})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 1.4088475704193115})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 1.37991201877594})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 1.387329339981079})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 1.427278995513916})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 1.612449049949646})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 1.3863084316253662})
store['active_learning_steps'][9]['training']['best_epoch']=7
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.8445, 'crossentropy': 1.24668466796875}
store['active_learning_steps'][9]['eval_training']={}
store['active_learning_steps'][9]['eval_training']['epochs']=[]
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.7890625, 'crossentropy': 1.001390814781189})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 0.8780644536018372})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 0.8066632151603699})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 0.821412980556488})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.8076171875, 'crossentropy': 0.8163237571716309})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 0.7849798202514648})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 0.8018759489059448})
store['active_learning_steps'][9]['eval_training']['best_epoch']=4
store['active_learning_steps'][9]['acquisition']={'indices': [['id', 41933], ['id', 39951], ['id', 21040], ['id', 5258], ['id', 55683]], 'labels': [5, -1, 9, 2, 8], 'scores': [0.8440021659297572, 1.513028349407466, 2.050069547338807, 2.413727721118155, 2.6031112392715263]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.794921875, 'crossentropy': 1.0918452739715576})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 1.048633098602295})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 1.180232286453247})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 1.2200837135314941})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 1.35892915725708})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 1.2700202465057373})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 1.3992908000946045})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 1.515609622001648})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8046875, 'crossentropy': 1.5833804607391357})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 1.3745346069335938})
store['active_learning_steps'][10]['training']['best_epoch']=7
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.8394, 'crossentropy': 1.313594921875}
store['active_learning_steps'][10]['eval_training']={}
store['active_learning_steps'][10]['eval_training']['epochs']=[]
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.7705078125, 'crossentropy': 1.0940029621124268})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.787109375, 'crossentropy': 1.0565216541290283})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.7939453125, 'crossentropy': 0.9999417662620544})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.796875, 'crossentropy': 1.058142900466919})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.7978515625, 'crossentropy': 0.9643356204032898})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.7919921875, 'crossentropy': 1.0068577527999878})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.7958984375, 'crossentropy': 0.9781382083892822})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 0.930340051651001})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.7861328125, 'crossentropy': 0.9732755422592163})
store['active_learning_steps'][10]['eval_training']['best_epoch']=8
store['active_learning_steps'][10]['acquisition']={'indices': [['id', 12687], ['id', 47568], ['id', 11127], ['id', 45439], ['id', 54258]], 'labels': [4, 7, 4, 2, 3], 'scores': [0.8198572381222854, 1.578275802126881, 2.13552333191052, 2.5359786694244466, 2.7744082126788037]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 0.9869556427001953})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 1.1570580005645752})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 1.2359882593154907})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 1.2487680912017822})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 1.21432626247406})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 1.2576004266738892})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 1.2803213596343994})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 1.3025789260864258})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 1.4940366744995117})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 1.6428484916687012})
store['active_learning_steps'][11]['training']['best_epoch']=7
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.8629, 'crossentropy': 1.18097314453125}
store['active_learning_steps'][11]['eval_training']={}
store['active_learning_steps'][11]['eval_training']['epochs']=[]
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.7890625, 'crossentropy': 1.0575072765350342})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 0.9618186354637146})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 0.8468327522277832})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 0.8254538774490356})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.811408281326294})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 0.7724494934082031})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.741594135761261})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.7517308592796326})
store['active_learning_steps'][11]['eval_training']['best_epoch']=5
store['active_learning_steps'][11]['acquisition']={'indices': [['id', 18106], ['id', 18279], ['id', 24457], ['id', 6962], ['id', 31200]], 'labels': [9, -1, 8, 8, 9], 'scores': [0.7528151931175548, 1.4294852992121738, 1.9438369486281513, 2.297408395120013, 2.511241218015221]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.783203125, 'crossentropy': 1.0480146408081055})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 1.0794633626937866})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 1.1927895545959473})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 1.3016571998596191})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 1.2867282629013062})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 1.4252912998199463})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 1.345461368560791})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 1.3022444248199463})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 1.522636890411377})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 1.6450119018554688})
store['active_learning_steps'][12]['training']['best_epoch']=7
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.8615, 'crossentropy': 1.103115234375}
store['active_learning_steps'][12]['eval_training']={}
store['active_learning_steps'][12]['eval_training']['epochs']=[]
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.7841796875, 'crossentropy': 1.0925379991531372})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.8144345283508301})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 0.7941703796386719})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 0.8705025911331177})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 0.8082360029220581})
store['active_learning_steps'][12]['eval_training']['best_epoch']=2
store['active_learning_steps'][12]['acquisition']={'indices': [['id', 5891], ['id', 53946], ['id', 28209], ['id', 2000], ['id', 8002]], 'labels': [4, 5, 5, 5, -1], 'scores': [0.7110825130309102, 1.3288525281135586, 1.8124291804453287, 2.196741327450757, 2.4178084610272164]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 0.9947502017021179})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 0.9311946630477905})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.9161510467529297})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 1.0461770296096802})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.9795019030570984})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 1.0586225986480713})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 1.1894158124923706})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 1.2175838947296143})
store['active_learning_steps'][13]['training']['best_epoch']=5
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.8856, 'crossentropy': 0.90365126953125}
store['active_learning_steps'][13]['eval_training']={}
store['active_learning_steps'][13]['eval_training']['epochs']=[]
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.8046875, 'crossentropy': 0.9624595642089844})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.7677673101425171})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 0.764881432056427})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.7097246050834656})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.7052432298660278})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.685706377029419})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.6485949754714966})
store['active_learning_steps'][13]['eval_training']['best_epoch']=7
store['active_learning_steps'][13]['acquisition']={'indices': [['id', 11515], ['id', 60], ['id', 30704], ['id', 39304], ['id', 46338]], 'labels': [-1, 4, 9, 4, 8], 'scores': [0.7710328848536797, 1.4725867386672173, 2.0204476069734882, 2.4310044866192198, 2.647009035067919]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 0.9227994084358215})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 0.9721451997756958})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 1.0270826816558838})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 1.058721661567688})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 1.1350308656692505})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 1.1472270488739014})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 1.2077810764312744})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 1.0748369693756104})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 1.2533882856369019})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 1.3194293975830078})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 1.2983877658843994})
store['active_learning_steps'][14]['training']['best_epoch']=8
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.8911, 'crossentropy': 0.8738140625}
store['active_learning_steps'][14]['eval_training']={}
store['active_learning_steps'][14]['eval_training']['epochs']=[]
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 0.8390043377876282})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.7414966821670532})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.72281813621521})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.7091790437698364})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.668646514415741})
store['active_learning_steps'][14]['eval_training']['best_epoch']=2
store['active_learning_steps'][14]['acquisition']={'indices': [['id', 48665], ['id', 47062], ['id', 5062], ['id', 1001], ['id', 44337]], 'labels': [2, 7, 9, 7, 6], 'scores': [0.6985461393075496, 1.2628418872116312, 1.704697243633332, 2.0338517250347135, 2.234267199766606]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 0.9211983680725098})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.8698017001152039})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.9038906693458557})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.9149930477142334})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.9993878602981567})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.9479742050170898})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 1.0605077743530273})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.9781746864318848})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 1.0859897136688232})
store['active_learning_steps'][15]['training']['best_epoch']=6
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.8951, 'crossentropy': 0.8018345703125}
store['active_learning_steps'][15]['eval_training']={}
store['active_learning_steps'][15]['eval_training']['epochs']=[]
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 0.9852057695388794})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.6888245344161987})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.6938432455062866})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.6896582841873169})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.6331056356430054})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.6241497993469238})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.6375974416732788})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.5940190553665161})
store['active_learning_steps'][15]['eval_training']['best_epoch']=5
store['active_learning_steps'][15]['acquisition']={'indices': [['id', 40012], ['id', 8680], ['id', 11406], ['id', 15717], ['id', 50902]], 'labels': [8, 8, 8, 3, 8], 'scores': [0.7543205681054104, 1.4106692012293305, 1.941596045163263, 2.3384216517153282, 2.6452901547025696]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.7971248626708984})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.7285208702087402})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.8121393918991089})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.7739202976226807})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.8647780418395996})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.8772026896476746})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.998874306678772})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.9085716009140015})
store['active_learning_steps'][16]['training']['best_epoch']=5
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.9069, 'crossentropy': 0.708821044921875}
store['active_learning_steps'][16]['eval_training']={}
store['active_learning_steps'][16]['eval_training']['epochs']=[]
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 0.9578002691268921})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.8023989200592041})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.6609679460525513})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.6488274931907654})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.6293125748634338})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.6257131099700928})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.616784393787384})
store['active_learning_steps'][16]['eval_training']['best_epoch']=7
store['active_learning_steps'][16]['acquisition']={'indices': [['id', 21636], ['id', 14355], ['id', 23560], ['id', 8976], ['id', 44642]], 'labels': [2, 2, 8, -1, 5], 'scores': [0.7842473493179949, 1.433172093103686, 1.9532962107164482, 2.37266144321772, 2.66597127924212]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 0.9062440395355225})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.7740458846092224})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.8424108028411865})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.8694174289703369})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.8213386535644531})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.8772904872894287})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.9502609372138977})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.9867644309997559})
store['active_learning_steps'][17]['training']['best_epoch']=5
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.906, 'crossentropy': 0.703833349609375}
store['active_learning_steps'][17]['eval_training']={}
store['active_learning_steps'][17]['eval_training']['epochs']=[]
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 0.9115879535675049})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.7017738223075867})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6665436625480652})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.6100249290466309})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.6008262634277344})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.5771670341491699})
store['active_learning_steps'][17]['eval_training']['best_epoch']=3
store['active_learning_steps'][17]['acquisition']={'indices': [['id', 11661], ['id', 42515], ['id', 35232], ['id', 55415], ['id', 32276]], 'labels': [0, 8, 8, -1, 3], 'scores': [0.7179805691761677, 1.3411419291217768, 1.8551461567059073, 2.227086140690056, 2.513976396913967]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 0.8390612006187439})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.7584764957427979})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.780624508857727})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.8170071244239807})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.8470458984375})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.8644922375679016})
store['active_learning_steps'][18]['training']['best_epoch']=3
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.9012, 'crossentropy': 0.671242431640625}
store['active_learning_steps'][18]['eval_training']={}
store['active_learning_steps'][18]['eval_training']['epochs']=[]
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 0.9084150791168213})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.7158898711204529})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.6280925273895264})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.6080275774002075})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.5850424766540527})
store['active_learning_steps'][18]['eval_training']['best_epoch']=4
store['active_learning_steps'][18]['acquisition']={'indices': [['id', 24424], ['id', 11482], ['id', 23490], ['id', 37226], ['id', 43952]], 'labels': [1, 8, 3, 5, -1], 'scores': [0.717574996306086, 1.2887173216923076, 1.6867883556856516, 1.9443900198047945, 2.0928892082858273]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 0.9049516320228577})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.7891417741775513})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.7294489145278931})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.8331582546234131})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.8993688225746155})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.9371359348297119})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.8507793545722961})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.9021828174591064})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.9236474633216858})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.8347361087799072})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.9639468193054199})
store['active_learning_steps'][19]['training']['best_epoch']=8
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.9078, 'crossentropy': 0.747378125}
store['active_learning_steps'][19]['eval_training']={}
store['active_learning_steps'][19]['eval_training']['epochs']=[]
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 0.9158668518066406})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.6843862533569336})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.6609524488449097})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.6178433895111084})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.616623044013977})
store['active_learning_steps'][19]['eval_training']['best_epoch']=2
store['active_learning_steps'][19]['acquisition']={'indices': [['id', 15899], ['id', 13816], ['id', 36950], ['id', 21674], ['id', 46619]], 'labels': [9, 0, 2, 2, -1], 'scores': [0.7855996586748126, 1.4534507477866414, 1.9977400462882295, 2.4078850189532557, 2.647766621598507]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 0.9045817852020264})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.7373488545417786})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.7696506977081299})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.8321805000305176})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.8102750182151794})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.8541678190231323})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.9494731426239014})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.9436618089675903})
store['active_learning_steps'][20]['training']['best_epoch']=5
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.9118, 'crossentropy': 0.68007685546875}
store['active_learning_steps'][20]['eval_training']={}
store['active_learning_steps'][20]['eval_training']['epochs']=[]
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 0.8468525409698486})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6462996006011963})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6082237362861633})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.585608959197998})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.5173779726028442})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.5256350040435791})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.47443556785583496})
store['active_learning_steps'][20]['eval_training']['best_epoch']=7
store['active_learning_steps'][20]['acquisition']={'indices': [['id', 11154], ['id', 24412], ['id', 3765], ['id', 47601], ['id', 1674]], 'labels': [5, 7, 2, 1, 9], 'scores': [0.7325601488140012, 1.3507117408177707, 1.8361298241741335, 2.1857981347919235, 2.3930713243184085]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.76953125, 'crossentropy': 1.0783151388168335})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.7887188196182251})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.7761746644973755})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.8890406489372253})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.8357478380203247})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.8769217133522034})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.962867796421051})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.8629225492477417})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.954984188079834})
store['active_learning_steps'][21]['training']['best_epoch']=6
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.9137, 'crossentropy': 0.701108642578125}
store['active_learning_steps'][21]['eval_training']={}
store['active_learning_steps'][21]['eval_training']['epochs']=[]
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 0.9055507183074951})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.5633028745651245})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.5671714544296265})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.554348349571228})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.5312806367874146})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5162904858589172})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5078427791595459})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5040439367294312})
store['active_learning_steps'][21]['eval_training']['best_epoch']=7
store['active_learning_steps'][21]['acquisition']={'indices': [['id', 31404], ['id', 20072], ['id', 30123], ['id', 9664], ['id', 23696]], 'labels': [3, 3, 0, 3, 4], 'scores': [0.8678383881309002, 1.5564459459423032, 2.068950814392929, 2.365251278708538, 2.528226553658337]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 0.9181073307991028})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.7033432722091675})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.798846960067749})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.7678419947624207})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.7393609881401062})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.7897965312004089})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.7158066630363464})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.9364787340164185})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.7901620864868164})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.7531874179840088})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.8658991456031799})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.9217267632484436})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.854082465171814})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.8880618810653687})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.881257951259613})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.7350916862487793})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.8817760944366455})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.8965166807174683})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.9725170135498047})
store['active_learning_steps'][22]['training']['best_epoch']=16
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.9287, 'crossentropy': 0.608953466796875}
store['active_learning_steps'][22]['eval_training']={}
store['active_learning_steps'][22]['eval_training']['epochs']=[]
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 0.9499053359031677})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.6607956886291504})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.6314754486083984})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6072215437889099})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.5910338163375854})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.5809025168418884})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.563565194606781})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.5524184703826904})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.5469834208488464})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.49904465675354004})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5285272002220154})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.5110597610473633})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5219588279724121})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.5059909820556641})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.49825620651245117})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.5156327486038208})
store['active_learning_steps'][22]['eval_training']['best_epoch']=13
store['active_learning_steps'][22]['acquisition']={'indices': [['id', 52087], ['id', 18680], ['id', 5545], ['id', 3693], ['id', 46068]], 'labels': [4, 9, 2, 0, 3], 'scores': [0.7605084825812791, 1.4006974531577008, 1.9292119684944478, 2.324133566893498, 2.6063771841105]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 0.9371374845504761})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6935991048812866})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.7312484979629517})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.740138590335846})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.7534111738204956})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.9021989107131958})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.816590428352356})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.8637440800666809})
store['active_learning_steps'][23]['training']['best_epoch']=5
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.9157, 'crossentropy': 0.621380517578125}
store['active_learning_steps'][23]['eval_training']={}
store['active_learning_steps'][23]['eval_training']['epochs']=[]
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 0.9276131391525269})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.6210784912109375})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.5782961845397949})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.5569651126861572})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.5212903022766113})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.5320876240730286})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.5278374552726746})
store['active_learning_steps'][23]['eval_training']['best_epoch']=5
store['active_learning_steps'][23]['acquisition']={'indices': [['id', 7033], ['id', 12950], ['id', 1453], ['id', 33612], ['id', 49779]], 'labels': [7, 2, 8, 7, 6], 'scores': [0.7598263601288622, 1.4287846414247447, 1.9207970522614177, 2.2194942513183458, 2.3941419933053503]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.7880859375, 'crossentropy': 1.0007603168487549})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6911728382110596})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6847837567329407})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6359055042266846})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.7219732999801636})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.7036697268486023})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.7298370003700256})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.7665480375289917})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.7862738370895386})
store['active_learning_steps'][24]['training']['best_epoch']=6
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.9245, 'crossentropy': 0.619513671875}
store['active_learning_steps'][24]['eval_training']={}
store['active_learning_steps'][24]['eval_training']['epochs']=[]
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.8175331354141235})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6016660928726196})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5408360958099365})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5229259729385376})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.5499559640884399})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.48478394746780396})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.5039815902709961})
store['active_learning_steps'][24]['eval_training']['best_epoch']=4
store['active_learning_steps'][24]['acquisition']={'indices': [['id', 34303], ['id', 45502], ['id', 26766], ['id', 8447], ['id', 16951]], 'labels': [4, 1, 6, 3, 8], 'scores': [0.7095075435253858, 1.3321748734771521, 1.8270617243545182, 2.17699299180952, 2.355428620727123]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.8573307394981384})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5867134928703308})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5925945043563843})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.641440749168396})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.6208313703536987})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.7072902917861938})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.6034919023513794})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.6505324840545654})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.66081702709198})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.6874300837516785})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.6752357482910156})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.7923528552055359})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.7055554986000061})
store['active_learning_steps'][25]['training']['best_epoch']=10
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.9333, 'crossentropy': 0.6031748046875}
store['active_learning_steps'][25]['eval_training']={}
store['active_learning_steps'][25]['eval_training']['epochs']=[]
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.8759691715240479})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5464316606521606})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5208895206451416})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.4542495012283325})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.4486533999443054})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.467421293258667})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.4234781861305237})
store['active_learning_steps'][25]['eval_training']['best_epoch']=4
store['active_learning_steps'][25]['acquisition']={'indices': [['id', 44753], ['id', 16884], ['id', 3494], ['id', 52048], ['id', 10910]], 'labels': [5, 9, 7, 0, 6], 'scores': [0.7945608088749305, 1.4533017509443331, 1.9614889367445798, 2.240475828650112, 2.3812634305821287]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.8363077044487})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.6203742623329163})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5379292964935303})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.645991325378418})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.6025840640068054})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.6705937385559082})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.6587953567504883})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.634322464466095})
store['active_learning_steps'][26]['training']['best_epoch']=5
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.9352, 'crossentropy': 0.503321875}
store['active_learning_steps'][26]['eval_training']={}
store['active_learning_steps'][26]['eval_training']['epochs']=[]
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.8064535856246948})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.5778905153274536})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.49063119292259216})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.4609307050704956})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.48755359649658203})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.4289470911026001})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.44166386127471924})
store['active_learning_steps'][26]['eval_training']['best_epoch']=6
store['active_learning_steps'][26]['acquisition']={'indices': [['id', 31], ['id', 20636], ['id', 55218], ['id', 18245], ['id', 59363]], 'labels': [8, 9, -1, -1, -1], 'scores': [0.7123823715866195, 1.2784475611349437, 1.7733237959650463, 2.140408321817919, 2.3955996678584803]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 0.9605042934417725})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6935754418373108})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5657236576080322})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.6109472513198853})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5991491079330444})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5565006136894226})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.6018581390380859})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.6675807237625122})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.6138725876808167})
store['active_learning_steps'][27]['training']['best_epoch']=6
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.9336, 'crossentropy': 0.5362296875}
store['active_learning_steps'][27]['eval_training']={}
store['active_learning_steps'][27]['eval_training']['epochs']=[]
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 0.8796300888061523})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5751222372055054})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5063357353210449})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.4596334397792816})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.49344977736473083})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.43483108282089233})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.4481828510761261})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.4311293065547943})
store['active_learning_steps'][27]['eval_training']['best_epoch']=7
store['active_learning_steps'][27]['acquisition']={'indices': [['id', 24219], ['id', 8861], ['id', 32747], ['id', 55788], ['id', 26763]], 'labels': [3, -1, 8, -1, -1], 'scores': [0.7556192751292423, 1.4200394907073814, 2.000415433034825, 2.387833998943858, 2.6378242739889046]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.8160542249679565})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5379509925842285})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5987919569015503})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.603355884552002})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.564389169216156})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5960349440574646})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5576460361480713})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5628734230995178})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5749821662902832})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.6233960390090942})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.6350560188293457})
store['active_learning_steps'][28]['training']['best_epoch']=8
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.9397, 'crossentropy': 0.480917822265625}
store['active_learning_steps'][28]['eval_training']={}
store['active_learning_steps'][28]['eval_training']['epochs']=[]
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.8265125751495361})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5533751249313354})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.45910561084747314})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.46035292744636536})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.40080875158309937})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.40904444456100464})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.3974161744117737})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.3879392147064209})
store['active_learning_steps'][28]['eval_training']['best_epoch']=5
store['active_learning_steps'][28]['acquisition']={'indices': [['id', 43282], ['id', 7140], ['id', 58829], ['id', 52149], ['id', 36758]], 'labels': [9, -1, 0, 7, 7], 'scores': [0.68381258520269, 1.2960392736167319, 1.8010676640247048, 2.155239620248305, 2.3855164106275533]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 0.8801926374435425})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.615900993347168})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5349947810173035})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5984997749328613})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5131964683532715})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.555691123008728})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5748327970504761})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.6075663566589355})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6621214151382446})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.622469961643219})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5597740411758423})
store['active_learning_steps'][29]['training']['best_epoch']=8
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.9386, 'crossentropy': 0.49814443359375}
store['active_learning_steps'][29]['eval_training']={}
store['active_learning_steps'][29]['eval_training']['epochs']=[]
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 0.914580225944519})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5883302688598633})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5079189538955688})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.4487289786338806})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.44993409514427185})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.42881807684898376})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.4115721583366394})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.43482932448387146})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.38727256655693054})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.38983696699142456})
store['active_learning_steps'][29]['eval_training']['best_epoch']=7
store['active_learning_steps'][29]['acquisition']={'indices': [['id', 10032], ['id', 40576], ['id', 2137], ['id', 31011], ['id', 43998]], 'labels': [6, 4, 9, 3, 7], 'scores': [0.6523805043827696, 1.2406968785042292, 1.7364616559069743, 2.123135738327322, 2.366279245262284]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 0.877885103225708})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5757068395614624})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5285816192626953})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.5068660974502563})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.5499392747879028})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.5210024118423462})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.567426323890686})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.6078096032142639})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.6753125190734863})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.613006055355072})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.6021294593811035})
store['active_learning_steps'][30]['training']['best_epoch']=8
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.9328, 'crossentropy': 0.558541455078125}
store['active_learning_steps'][30]['eval_training']={}
store['active_learning_steps'][30]['eval_training']['epochs']=[]
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 0.9250109791755676})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.5847627520561218})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5225687026977539})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.4884481430053711})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.4656759202480316})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.4757547974586487})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.4502207636833191})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.45801058411598206})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.43305131793022156})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.41863757371902466})
store['active_learning_steps'][30]['eval_training']['best_epoch']=10
store['active_learning_steps'][30]['acquisition']={'indices': [['id', 20287], ['id', 32453], ['id', 37339], ['id', 54646], ['id', 28050]], 'labels': [4, 8, 4, 6, -1], 'scores': [0.8002063013715343, 1.4703653815979603, 1.9741985688789332, 2.3124098158988557, 2.5368378734757]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 0.9150017499923706})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5967153310775757})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5847994089126587})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6238992214202881})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.6441450715065002})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5977909564971924})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.6359574794769287})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.6639243364334106})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.641577422618866})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.603096604347229})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.6228904724121094})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.660163402557373})
store['active_learning_steps'][31]['training']['best_epoch']=9
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.9376, 'crossentropy': 0.512243994140625}
store['active_learning_steps'][31]['eval_training']={}
store['active_learning_steps'][31]['eval_training']['epochs']=[]
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.8037109375, 'crossentropy': 0.9720094799995422})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6409831047058105})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5048111081123352})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.48319369554519653})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.45656538009643555})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.4069044589996338})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.4096280634403229})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.41224533319473267})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.3881964087486267})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.37253302335739136})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.3702881932258606})
store['active_learning_steps'][31]['eval_training']['best_epoch']=9
store['active_learning_steps'][31]['acquisition']={'indices': [['id', 48630], ['id', 10251], ['id', 25332], ['id', 48781], ['id', 30454]], 'labels': [6, -1, 2, -1, 6], 'scores': [0.7673928627696405, 1.4395763652430498, 1.9924527531446392, 2.3334232042486303, 2.560083456560948]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 0.9193907976150513})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.6003520488739014})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5306892395019531})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.548086941242218})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.5494846701622009})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5395422577857971})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5533685684204102})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.6429058909416199})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.633314847946167})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.6110560894012451})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5896985530853271})
store['active_learning_steps'][32]['training']['best_epoch']=8
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.9454, 'crossentropy': 0.50257958984375}
store['active_learning_steps'][32]['eval_training']={}
store['active_learning_steps'][32]['eval_training']['epochs']=[]
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 0.9119393825531006})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5616641044616699})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5056802034378052})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.45380181074142456})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.39925453066825867})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.43364715576171875})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.37520185112953186})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.42709881067276})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.36119329929351807})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.38053739070892334})
store['active_learning_steps'][32]['eval_training']['best_epoch']=7
store['active_learning_steps'][32]['acquisition']={'indices': [['id', 20226], ['id', 59303], ['id', 13025], ['id', 34199], ['id', 9885]], 'labels': [7, 8, 1, -1, -1], 'scores': [0.736864426534249, 1.4052260987187486, 1.9300633075303995, 2.265597621519543, 2.4715079695444855]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.8800249099731445})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5525600910186768})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6006207466125488})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5407284498214722})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5918518304824829})
store['active_learning_steps'][33]['training']['best_epoch']=2
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.922, 'crossentropy': 0.520013720703125}
store['active_learning_steps'][33]['eval_training']={}
store['active_learning_steps'][33]['eval_training']['epochs']=[]
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 0.900589108467102})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6303319334983826})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5739419460296631})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5232104659080505})
store['active_learning_steps'][33]['eval_training']['best_epoch']=4
store['active_learning_steps'][33]['acquisition']={'indices': [['id', 32445], ['id', 51144], ['id', 2148], ['id', 31802], ['id', 15362]], 'labels': [5, 5, 6, 2, 5], 'scores': [0.5285129343827843, 1.0097823264573638, 1.4100919842017987, 1.740549831264655, 1.982742296999894]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 1.0336225032806396})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.6260086297988892})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5578597187995911})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5544028878211975})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.5391941070556641})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.585905134677887})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.6236189007759094})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5425658226013184})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.6832817792892456})
store['active_learning_steps'][34]['training']['best_epoch']=6
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.9377, 'crossentropy': 0.504556201171875}
store['active_learning_steps'][34]['eval_training']={}
store['active_learning_steps'][34]['eval_training']['epochs']=[]
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.9413396120071411})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.577460527420044})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5202068090438843})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.4545222222805023})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.43847617506980896})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.4377123713493347})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.4250345826148987})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.415152907371521})
store['active_learning_steps'][34]['eval_training']['best_epoch']=7
store['active_learning_steps'][34]['acquisition']={'indices': [['id', 13156], ['id', 48280], ['id', 38698], ['id', 5700], ['id', 9417]], 'labels': [2, 8, 5, 2, -1], 'scores': [0.7820450878834564, 1.4460841134217675, 1.9914347403698693, 2.395786346544137, 2.6439220697014436]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.7607421875, 'crossentropy': 1.0340639352798462})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5765789747238159})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5984774827957153})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5598585605621338})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5676965713500977})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5867162346839905})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5251975059509277})
store['active_learning_steps'][35]['training']['best_epoch']=4
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.9371, 'crossentropy': 0.47765126953125}
store['active_learning_steps'][35]['eval_training']={}
store['active_learning_steps'][35]['eval_training']['epochs']=[]
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 0.9514637589454651})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6072044372558594})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.45348161458969116})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.4501919150352478})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.4371721148490906})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.4204162359237671})
store['active_learning_steps'][35]['eval_training']['best_epoch']=6
store['active_learning_steps'][35]['acquisition']={'indices': [['id', 41108], ['id', 47506], ['id', 12937], ['id', 10251], ['id', 31587]], 'labels': [0, 8, 5, -1, -1], 'scores': [0.7046727138226463, 1.3209251839885656, 1.8275962291606573, 2.1640141803699047, 2.3951669306464716]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.8637106418609619})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5100800395011902})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5027978420257568})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.51123046875})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5625792741775513})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5369861125946045})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5693431496620178})
store['active_learning_steps'][36]['training']['best_epoch']=4
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.9388, 'crossentropy': 0.42646767578125}
store['active_learning_steps'][36]['eval_training']={}
store['active_learning_steps'][36]['eval_training']['epochs']=[]
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.9389232397079468})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.6113767623901367})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5083703994750977})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.4867706298828125})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.4767695665359497})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.4391530156135559})
store['active_learning_steps'][36]['eval_training']['best_epoch']=3
store['active_learning_steps'][36]['acquisition']={'indices': [['id', 5553], ['id', 18739], ['id', 46432], ['id', 52740], ['id', 22989]], 'labels': [-1, 3, 6, -1, 3], 'scores': [0.6531703162667484, 1.217566947406536, 1.6790345174896921, 2.0122300431369364, 2.2056361355911367]}
store['active_learning_steps'].append({})
store['active_learning_steps'][37]['training']={}
store['active_learning_steps'][37]['training']['epochs']=[]
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 0.9758513569831848})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5781206488609314})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5780634880065918})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5356561541557312})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.45760881900787354})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5531338453292847})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5424804091453552})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5649216175079346})
store['active_learning_steps'][37]['training']['best_epoch']=5
store['active_learning_steps'][37]['evaluation_metrics']={'accuracy': 0.9472, 'crossentropy': 0.42286357421875}
store['active_learning_steps'][37]['eval_training']={}
store['active_learning_steps'][37]['eval_training']['epochs']=[]
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.9013985395431519})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5278968811035156})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.4755546748638153})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.41587620973587036})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.4409157931804657})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.42396581172943115})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.36959487199783325})
store['active_learning_steps'][37]['eval_training']['best_epoch']=4
store['active_learning_steps'][37]['acquisition']={'indices': [['id', 58931], ['id', 21692], ['id', 27793], ['id', 34976], ['id', 17764]], 'labels': [3, 2, 1, 2, 6], 'scores': [0.5777740750977534, 1.1030888305186421, 1.550999000673945, 1.8791329289952605, 2.11416425592687]}
store['active_learning_steps'].append({})
store['active_learning_steps'][38]['training']={}
store['active_learning_steps'][38]['training']['epochs']=[]
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.8273642063140869})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5010843276977539})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.542078971862793})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5372217297554016})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5263125896453857})
store['active_learning_steps'][38]['training']['best_epoch']=2
store['active_learning_steps'][38]['evaluation_metrics']={'accuracy': 0.934, 'crossentropy': 0.463354638671875}
store['active_learning_steps'][38]['eval_training']={}
store['active_learning_steps'][38]['eval_training']['epochs']=[]
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 1.0177019834518433})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.670152485370636})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6276500225067139})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5368052124977112})
store['active_learning_steps'][38]['eval_training']['best_epoch']=4
store['active_learning_steps'][38]['acquisition']={'indices': [['id', 424], ['id', 37048], ['id', 14749], ['id', 39457], ['id', 5355]], 'labels': [9, 9, 0, 0, -1], 'scores': [0.5624621751719914, 1.0683544594662786, 1.52287536890441, 1.8613497607479914, 2.1148291408694497]}
store['active_learning_steps'].append({})
store['active_learning_steps'][39]['training']={}
store['active_learning_steps'][39]['training']['epochs']=[]
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 1.0019623041152954})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5976466536521912})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.4908244013786316})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5407332181930542})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.5153746008872986})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5278365015983582})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.5330235958099365})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.5415023565292358})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5686324834823608})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5664036273956299})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5683150291442871})
store['active_learning_steps'][39]['training']['best_epoch']=8
store['active_learning_steps'][39]['evaluation_metrics']={'accuracy': 0.9429, 'crossentropy': 0.4674859375}
store['active_learning_steps'][39]['eval_training']={}
store['active_learning_steps'][39]['eval_training']['epochs']=[]
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.7900390625, 'crossentropy': 1.0154796838760376})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.6425331234931946})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.4731765389442444})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.4727431535720825})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.4262840449810028})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.4592079520225525})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.405719131231308})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.39610105752944946})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.40327075123786926})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.4025557041168213})
store['active_learning_steps'][39]['eval_training']['best_epoch']=7
store['active_learning_steps'][39]['acquisition']={'indices': [['id', 36244], ['id', 28293], ['id', 12426], ['id', 31738], ['id', 22573]], 'labels': [5, 2, 2, 8, 2], 'scores': [0.7644129861322695, 1.440404451032405, 1.9964692768887073, 2.382598512852166, 2.6057011777352095]}
store['active_learning_steps'].append({})
store['active_learning_steps'][40]['training']={}
store['active_learning_steps'][40]['training']['epochs']=[]
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 0.9956912994384766})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5607262849807739})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.48896828293800354})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.46302521228790283})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5046903491020203})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5629737377166748})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.549341082572937})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.605254054069519})
store['active_learning_steps'][40]['training']['best_epoch']=5
store['active_learning_steps'][40]['evaluation_metrics']={'accuracy': 0.9434, 'crossentropy': 0.428166162109375}
store['active_learning_steps'][40]['eval_training']={}
store['active_learning_steps'][40]['eval_training']['epochs']=[]
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.7998046875, 'crossentropy': 1.0609432458877563})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5626684427261353})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.4650447368621826})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.44161075353622437})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.4292222261428833})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.43213117122650146})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.3752197325229645})
store['active_learning_steps'][40]['eval_training']['best_epoch']=5
store['active_learning_steps'][40]['acquisition']={'indices': [['id', 39031], ['id', 37583], ['id', 15185], ['id', 1254], ['id', 17849]], 'labels': [2, -1, 2, -1, 7], 'scores': [0.6131017845467912, 1.1508388559957106, 1.601573560252774, 1.93512942159178, 2.1614319187960103]}
store['active_learning_steps'].append({})
store['active_learning_steps'][41]['training']={}
store['active_learning_steps'][41]['training']['epochs']=[]
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 0.9787012338638306})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5971266031265259})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5670300722122192})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.4415462017059326})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.4479331374168396})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5206854343414307})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5132322311401367})
store['active_learning_steps'][41]['training']['best_epoch']=4
store['active_learning_steps'][41]['evaluation_metrics']={'accuracy': 0.9466, 'crossentropy': 0.413249169921875}
store['active_learning_steps'][41]['eval_training']={}
store['active_learning_steps'][41]['eval_training']['epochs']=[]
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.816986083984375})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5190843343734741})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.44187068939208984})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.3913428783416748})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.4145335555076599})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.40615302324295044})
store['active_learning_steps'][41]['eval_training']['best_epoch']=5
store['active_learning_steps'][41]['acquisition']={'indices': [['id', 51432], ['id', 8093], ['id', 17110], ['id', 48735], ['id', 10520]], 'labels': [1, 0, -1, -1, -1], 'scores': [0.6344003285510988, 1.1964921930284849, 1.6750620366435758, 2.0385330266890103, 2.282927169922643]}
store['active_learning_steps'].append({})
store['active_learning_steps'][42]['training']={}
store['active_learning_steps'][42]['training']['epochs']=[]
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.9039267301559448})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.49391400814056396})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.47390666604042053})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.5184502005577087})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.46170979738235474})
store['active_learning_steps'][42]['training']['best_epoch']=2
store['active_learning_steps'][42]['evaluation_metrics']={'accuracy': 0.9317, 'crossentropy': 0.4878806640625}
store['active_learning_steps'][42]['eval_training']={}
store['active_learning_steps'][42]['eval_training']['epochs']=[]
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 0.876810610294342})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6563829183578491})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5981343984603882})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.585643470287323})
store['active_learning_steps'][42]['eval_training']['best_epoch']=4
store['active_learning_steps'][42]['acquisition']={'indices': [['id', 33593], ['id', 28136], ['id', 16756], ['id', 32519], ['id', 32522]], 'labels': [2, 8, 7, 5, -1], 'scores': [0.5306494519077858, 1.0057900102849784, 1.407598283037049, 1.737926372647923, 1.979119723252369]}
store['active_learning_steps'].append({})
store['active_learning_steps'][43]['training']={}
store['active_learning_steps'][43]['training']['epochs']=[]
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 0.9837164282798767})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6210178136825562})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5314486026763916})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.47649097442626953})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5028162002563477})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.45164138078689575})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5651230812072754})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.494437038898468})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.5278191566467285})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.5075258612632751})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.5288688540458679})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.519848108291626})
store['active_learning_steps'][43]['training']['best_epoch']=9
store['active_learning_steps'][43]['evaluation_metrics']={'accuracy': 0.9485, 'crossentropy': 0.443156005859375}
