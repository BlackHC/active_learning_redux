store = {}
store['timestamp']=1621480233
store['cmdline']=['/home/kell4989/git/active_learning_redux/batchbald_redux/ood_experiment.py', '--id=58']
store['commit']='8a2cf4fb40ce306533b4e439b08268c53f009a3b'
store['github_url']='8a2cf4fb40ce306533b4e439b08268c53f009a3b'
store['experiment']='/home/kell4989/git/active_learning_redux/batchbald_redux/ood_experiment.py'
store['job_id']=58
store['worker_id']=58
store['num_workers']=80
store['config']={'seed': 1295, 'uniform_ood': False, 'id_dataset_type': 'batchbald_redux.fast_mnist.FastMNIST', 'ood_dataset_type': 'batchbald_redux.fast_mnist.FastFashionMNIST', 'initial_training_set_size': 20, 'validation_set_size': 1024, 'evaluation_set_size': 16, 'id_repetitions': 1, 'ood_repetitions': 1, 'add_dataset_noise': False, 'validation_split_random_state': 0, 'acquisition_size': 5, 'max_training_set': 200, 'num_pool_samples': 100, 'num_validation_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'min_samples_per_epoch': 5056, 'acquisition_function': 'batchbald_redux.acquisition_functions.BatchBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationEvalModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 8}
store['log']={}
store['dataset_info']={'training': "(FastMNIST (train; 58976 samples)) + ('FastFashionMNIST Train (60000 samples)' | constant_target{'target': tensor(-1, device='cuda:0'), 'num_classes': 10})", 'test': "'FastMNIST Test (10000 samples)'"}
store['initial_training_set_indices']=[53434, 8533, 14640, 39579, 30392, 58125, 37915, 3091, 57520, 43803, 44119, 52296, 58226, 40334, 46037, 22015, 22304, 43812, 12640, 53689]
store['evaluation_set_indices']=[29974, 3792, 5573, 45567, 10508, 2728, 21423, 396, 49512, 31444]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 2.632758140563965})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 3.24006986618042})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 3.421391010284424})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 3.1580772399902344})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 2.8749446868896484})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 3.3480677604675293})
store['active_learning_steps'][0]['training']['best_epoch']=3
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.6499, 'crossentropy': 2.78568515625}
store['active_learning_steps'][0]['acquisition']={'indices': [['id', 1193], ['id', 15867], ['id', 47651], ['id', 13271], ['id', 27181]], 'labels': [8, 2, 3, 4, 2], 'scores': [1.279922114239203, 2.411749748080747, 3.2520570531204793, 3.8108662346012645, 4.163136500962866]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 2.0473453998565674})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 2.0580055713653564})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 2.4463677406311035})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 2.492354393005371})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 2.3204188346862793})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 2.6694068908691406})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 2.770472526550293})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 3.022552490234375})
store['active_learning_steps'][1]['training']['best_epoch']=5
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.7315, 'crossentropy': 2.127291796875}
store['active_learning_steps'][1]['acquisition']={'indices': [['id', 25415], ['id', 6846], ['id', 44807], ['id', 33484], ['id', 8886]], 'labels': [8, 2, 7, 6, 2], 'scores': [1.1374832992980122, 2.14927520934183, 3.0498129861116983, 3.666090922617549, 4.064908380820773]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.712890625, 'crossentropy': 1.7415568828582764})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.716796875, 'crossentropy': 1.9746465682983398})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.732421875, 'crossentropy': 2.2439863681793213})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 2.6319189071655273})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.7265625, 'crossentropy': 2.2452282905578613})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 2.5851831436157227})
store['active_learning_steps'][2]['training']['best_epoch']=3
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.7448, 'crossentropy': 2.104919140625}
store['active_learning_steps'][2]['acquisition']={'indices': [['id', 12638], ['id', 25669], ['id', 5106], ['id', 56472], ['id', 27403]], 'labels': [5, 5, 9, 7, 5], 'scores': [1.3154134010936855, 2.400988880915154, 3.2844123688721822, 3.8335880651701277, 4.163665846515778]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 1.5517165660858154})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.724609375, 'crossentropy': 1.8201872110366821})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.73046875, 'crossentropy': 1.8142879009246826})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 2.084084987640381})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 2.207186222076416})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 2.2162435054779053})
store['active_learning_steps'][3]['training']['best_epoch']=3
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.746, 'crossentropy': 1.6651416015625}
store['active_learning_steps'][3]['acquisition']={'indices': [['id', 14367], ['id', 5194], ['id', 4767], ['id', 12963], ['id', 53656]], 'labels': [3, 0, 8, 8, 2], 'scores': [1.2643724048267204, 2.349124954517015, 3.211254832915456, 3.768026565165856, 4.1162041465648445]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 1.594280481338501})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 1.9082989692687988})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 2.1034040451049805})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 1.8881275653839111})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 2.3300538063049316})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7275390625, 'crossentropy': 2.086452007293701})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 2.121608257293701})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.732421875, 'crossentropy': 2.266643524169922})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 2.306556224822998})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7431640625, 'crossentropy': 2.2720251083374023})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7265625, 'crossentropy': 2.323303699493408})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.73046875, 'crossentropy': 2.289267063140869})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 2.5963897705078125})
store['active_learning_steps'][4]['training']['best_epoch']=10
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.7564, 'crossentropy': 2.0386439453125}
store['active_learning_steps'][4]['acquisition']={'indices': [['id', 47707], ['id', 3730], ['id', 51314], ['id', 42763], ['id', 19298]], 'labels': [5, 8, 0, 7, 6], 'scores': [1.3046033809854745, 2.4759619245424958, 3.3678571011268117, 3.9133011139241543, 4.249569531931208]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.73046875, 'crossentropy': 1.2662394046783447})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.76171875, 'crossentropy': 1.52335786819458})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.767578125, 'crossentropy': 1.5442192554473877})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7529296875, 'crossentropy': 1.805281162261963})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7548828125, 'crossentropy': 1.8465347290039062})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7607421875, 'crossentropy': 1.8139595985412598})
store['active_learning_steps'][5]['training']['best_epoch']=3
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.7864, 'crossentropy': 1.39741640625}
store['active_learning_steps'][5]['acquisition']={'indices': [['id', 31335], ['id', 21138], ['id', 31883], ['id', 20025], ['id', 32192]], 'labels': [5, 9, 4, 8, 3], 'scores': [1.1787201718104048, 2.1855626927990537, 3.021945040991329, 3.639473406952659, 4.0360058678215385]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7607421875, 'crossentropy': 1.1870927810668945})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7578125, 'crossentropy': 1.3735897541046143})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.763671875, 'crossentropy': 1.3445740938186646})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.751953125, 'crossentropy': 1.601627230644226})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7783203125, 'crossentropy': 1.6575380563735962})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7783203125, 'crossentropy': 1.5711019039154053})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.783203125, 'crossentropy': 1.6513211727142334})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7861328125, 'crossentropy': 1.7399206161499023})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7587890625, 'crossentropy': 1.6102596521377563})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7783203125, 'crossentropy': 1.6440670490264893})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.77734375, 'crossentropy': 1.6576173305511475})
store['active_learning_steps'][6]['training']['best_epoch']=8
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.811, 'crossentropy': 1.50471669921875}
store['active_learning_steps'][6]['acquisition']={'indices': [['id', 5274], ['id', 54532], ['id', 57876], ['id', 36072], ['id', 35946]], 'labels': [6, 7, 2, 2, 4], 'scores': [1.276924333058005, 2.4153989481943823, 3.3235028174175945, 3.8847914376513994, 4.216644605464668]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.798828125, 'crossentropy': 0.9949468374252319})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 1.1153388023376465})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 1.0334179401397705})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 1.1521953344345093})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 1.1529088020324707})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 1.2267005443572998})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8046875, 'crossentropy': 1.472501516342163})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8037109375, 'crossentropy': 1.468294620513916})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7880859375, 'crossentropy': 1.5639228820800781})
store['active_learning_steps'][7]['training']['best_epoch']=6
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.8498, 'crossentropy': 1.1601865234375}
store['active_learning_steps'][7]['acquisition']={'indices': [['id', 6944], ['id', 46530], ['id', 14623], ['id', 19229], ['id', 37437]], 'labels': [2, 4, 5, 2, 2], 'scores': [1.2493520380540026, 2.29099862852624, 3.1456122517647938, 3.746197369836473, 4.125165467043535]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7880859375, 'crossentropy': 0.9932082891464233})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 0.976610541343689})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 1.0385997295379639})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 1.0485434532165527})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 1.106029748916626})
store['active_learning_steps'][8]['training']['best_epoch']=2
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.8493, 'crossentropy': 0.91472138671875}
store['active_learning_steps'][8]['acquisition']={'indices': [['id', 4360], ['id', 2803], ['id', 7933], ['id', 1423], ['id', 45256]], 'labels': [6, 3, 2, 0, 5], 'scores': [1.0646783426430693, 2.069752622559924, 2.855687320398424, 3.466779408384202, 3.898851380025107]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 0.9390214681625366})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 0.8524324297904968})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.9284443259239197})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.896762490272522})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 1.1079961061477661})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 1.1198406219482422})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 1.056275725364685})
store['active_learning_steps'][9]['training']['best_epoch']=4
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.8674, 'crossentropy': 0.9180333984375}
store['active_learning_steps'][9]['acquisition']={'indices': [['id', 1311], ['id', 134], ['id', 10412], ['id', 37293], ['id', 12497]], 'labels': [5, 1, 5, 3, 0], 'scores': [1.1791235872189492, 2.182698995105553, 2.9986562476504286, 3.5981627573578, 4.001998362767141]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 0.9925398826599121})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 1.0004233121871948})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 0.9936050772666931})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 1.1015489101409912})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 1.0496759414672852})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 1.289414405822754})
store['active_learning_steps'][10]['training']['best_epoch']=3
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.8616, 'crossentropy': 0.948244140625}
store['active_learning_steps'][10]['acquisition']={'indices': [['id', 16951], ['id', 26358], ['id', 11569], ['id', 26733], ['id', 20050]], 'labels': [8, 3, 5, 2, 9], 'scores': [1.090541523783989, 2.084852747243886, 2.9053680445092276, 3.5214913896645896, 3.9369089897658185]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.7734375, 'crossentropy': 1.0561426877975464})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 0.90781569480896})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.9237644672393799})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 1.0474833250045776})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 1.0680197477340698})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 1.1222093105316162})
store['active_learning_steps'][11]['training']['best_epoch']=3
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.872, 'crossentropy': 0.83061748046875}
store['active_learning_steps'][11]['acquisition']={'indices': [['id', 37574], ['id', 14655], ['id', 2856], ['id', 43065], ['id', 29591]], 'labels': [5, 3, 4, 3, 9], 'scores': [1.193870594347863, 2.1840195428634788, 2.972265102970839, 3.5533845061806613, 3.9468334491226997]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 0.9328805208206177})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 0.8318949937820435})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 0.9014711380004883})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.8666754961013794})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 0.9745285511016846})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 1.0125393867492676})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 1.0301040410995483})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.9298150539398193})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.9876914024353027})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 1.0809975862503052})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 1.0998494625091553})
store['active_learning_steps'][12]['training']['best_epoch']=8
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.8814, 'crossentropy': 0.90798115234375}
store['active_learning_steps'][12]['acquisition']={'indices': [['id', 52462], ['id', 9036], ['id', 45954], ['id', 18240], ['id', 26568]], 'labels': [9, 2, 8, 3, -1], 'scores': [1.2677088494701372, 2.3635816530332896, 3.216432837468817, 3.8142294507056587, 4.185004771228671]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.77734375, 'crossentropy': 1.0676820278167725})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 0.9652755856513977})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 1.099491834640503})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 1.1112124919891357})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 1.2261972427368164})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 1.2510002851486206})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 1.2956163883209229})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 1.3064649105072021})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 1.2394723892211914})
store['active_learning_steps'][13]['training']['best_epoch']=6
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.8522, 'crossentropy': 1.187346484375}
store['active_learning_steps'][13]['acquisition']={'indices': [['id', 40704], ['id', 20792], ['id', 18042], ['id', 32323], ['id', 11202]], 'labels': [5, 9, 0, 5, 9], 'scores': [1.167853512966138, 2.205075157323323, 3.0673614074434754, 3.6834390991195995, 4.085661645894793]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.7548828125, 'crossentropy': 1.088419795036316})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 0.926671028137207})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.9466453790664673})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.9203261137008667})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.9548211693763733})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 1.0638000965118408})
store['active_learning_steps'][14]['training']['best_epoch']=3
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.8687, 'crossentropy': 0.85026064453125}
store['active_learning_steps'][14]['acquisition']={'indices': [['id', 24479], ['id', 53872], ['id', 49200], ['id', 7033], ['id', 18598]], 'labels': [8, 8, 0, 7, 9], 'scores': [1.053756450283684, 2.003900530932778, 2.792307676331955, 3.4306507774735575, 3.858727899330016]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.7431640625, 'crossentropy': 1.1270532608032227})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.8563255071640015})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 0.8965553641319275})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.9449476003646851})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 1.103478193283081})
store['active_learning_steps'][15]['training']['best_epoch']=2
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.8696, 'crossentropy': 0.76279912109375}
store['active_learning_steps'][15]['acquisition']={'indices': [['id', 4822], ['id', 27540], ['id', 49064], ['id', 46126], ['id', 23215]], 'labels': [4, 3, 8, 3, 8], 'scores': [0.9942167952256571, 1.8907462308849032, 2.649179011202275, 3.2502444908122268, 3.702591938037685]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.71484375, 'crossentropy': 1.2789808511734009})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 0.9285973310470581})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.8947591781616211})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.9145318269729614})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 1.0021204948425293})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.9224643707275391})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 1.103499174118042})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 1.100414752960205})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 1.1013355255126953})
store['active_learning_steps'][16]['training']['best_epoch']=6
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.8659, 'crossentropy': 0.92596416015625}
store['active_learning_steps'][16]['acquisition']={'indices': [['id', 55834], ['id', 3719], ['id', 21304], ['id', 37962], ['id', 3508]], 'labels': [9, 2, 4, 8, 9], 'scores': [1.133182671131876, 2.1721657467835245, 3.0584940770244096, 3.6816144467941463, 4.085426664048844]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.771484375, 'crossentropy': 1.0734525918960571})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 0.8375497460365295})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.8278928995132446})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.9219944477081299})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.8893886208534241})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.8430578708648682})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.9319803714752197})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 1.082787275314331})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.8726679086685181})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 1.0364763736724854})
store['active_learning_steps'][17]['training']['best_epoch']=7
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.8819, 'crossentropy': 0.9111107421875}
store['active_learning_steps'][17]['acquisition']={'indices': [['id', 36818], ['id', 39818], ['id', 43532], ['id', 37078], ['id', 6604]], 'labels': [7, 1, 8, 8, 8], 'scores': [1.2242650832433073, 2.253205574261859, 3.0878489687005573, 3.721617218374818, 4.122168850669688]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.748046875, 'crossentropy': 1.1723964214324951})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 0.9589376449584961})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 0.93410325050354})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.8673000335693359})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.8762767314910889})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.9082797765731812})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.9927520751953125})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 1.0547152757644653})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.979962944984436})
store['active_learning_steps'][18]['training']['best_epoch']=6
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.8712, 'crossentropy': 0.87377060546875}
store['active_learning_steps'][18]['acquisition']={'indices': [['id', 17855], ['id', 42703], ['id', 34520], ['id', 57728], ['id', 30903]], 'labels': [6, 0, 6, 9, 5], 'scores': [1.1273550579267066, 2.094692400852206, 2.914246869305291, 3.539147542200162, 3.9696542123479652]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8017578125, 'crossentropy': 1.0247524976730347})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.7596185207366943})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.8364467620849609})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.8317676782608032})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.8633074164390564})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.8608812093734741})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.740760087966919})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.9057978391647339})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.9616767168045044})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.9849240183830261})
store['active_learning_steps'][19]['training']['best_epoch']=7
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.89, 'crossentropy': 0.76860048828125}
store['active_learning_steps'][19]['acquisition']={'indices': [['id', 50317], ['id', 47626], ['id', 28183], ['id', 54919], ['id', 2034]], 'labels': [3, -1, 9, 8, 4], 'scores': [1.180907942364237, 2.2110684127317897, 3.0613112382236274, 3.680997759807303, 4.061670669601984]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.77734375, 'crossentropy': 1.0832608938217163})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.8131192922592163})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 0.9048060178756714})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.8319085836410522})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.8928414583206177})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.8733687400817871})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 1.0868492126464844})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.9003174304962158})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.9103866219520569})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 1.024747371673584})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 1.1083670854568481})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.982697606086731})
store['active_learning_steps'][20]['training']['best_epoch']=9
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.8878, 'crossentropy': 0.9077337890625}
store['active_learning_steps'][20]['acquisition']={'indices': [['id', 59726], ['id', 45446], ['id', 59314], ['id', 274], ['id', 55128]], 'labels': [5, 7, 9, 6, 8], 'scores': [1.1974907147969325, 2.2790717942177774, 3.1728144249295305, 3.801497189349223, 4.184685999087241]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.232147216796875})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.8366619348526001})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.7107768654823303})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.7346107959747314})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.882288932800293})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.9021503925323486})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.8395308256149292})
store['active_learning_steps'][21]['training']['best_epoch']=4
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.9063, 'crossentropy': 0.66757119140625}
store['active_learning_steps'][21]['acquisition']={'indices': [['id', 46368], ['id', 52169], ['id', 48040], ['id', 22144], ['id', 41054]], 'labels': [8, 2, 1, 0, 7], 'scores': [1.0578104650395361, 2.020875085462241, 2.85170099629447, 3.479852680942141, 3.931940801207011]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.7822265625, 'crossentropy': 1.1275556087493896})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.684125542640686})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6687554121017456})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6763567924499512})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6845564246177673})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.7086113691329956})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6705247163772583})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.800691545009613})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.6097232103347778})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.8046832084655762})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.7929497957229614})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.7801768779754639})
store['active_learning_steps'][22]['training']['best_epoch']=9
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.9254, 'crossentropy': 0.59421162109375}
store['active_learning_steps'][22]['acquisition']={'indices': [['id', 57211], ['id', 33222], ['id', 4676], ['id', 27176], ['id', 29132]], 'labels': [5, 5, 1, 5, 8], 'scores': [1.1665525352919088, 2.230733327810194, 3.1439629686796344, 3.77291118268492, 4.153843375201108]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 1.074018120765686})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.7039651870727539})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5593266487121582})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6513915061950684})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6952212452888489})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.708224892616272})
store['active_learning_steps'][23]['training']['best_epoch']=3
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.9233, 'crossentropy': 0.539748046875}
store['active_learning_steps'][23]['acquisition']={'indices': [['id', 8559], ['id', 37440], ['id', 49202], ['id', 20641], ['id', 49082]], 'labels': [7, 2, 5, 9, 3], 'scores': [0.9527462978914185, 1.8474046092874983, 2.6402208518610593, 3.270736079154611, 3.7216161339447744]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 0.9690402746200562})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5916614532470703})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5425460338592529})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5906704664230347})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5906118154525757})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5947420001029968})
store['active_learning_steps'][24]['training']['best_epoch']=3
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.926, 'crossentropy': 0.513485595703125}
store['active_learning_steps'][24]['acquisition']={'indices': [['id', 25246], ['id', 45602], ['id', 50320], ['id', 46714], ['id', 25823]], 'labels': [2, 5, 5, 9, 0], 'scores': [0.9892029771726358, 1.8975433406733897, 2.6762248558890223, 3.300742050241105, 3.7377171298480647]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 1.1070839166641235})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6228435039520264})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5496858358383179})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6091963052749634})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6041688919067383})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.7111690044403076})
store['active_learning_steps'][25]['training']['best_epoch']=3
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.9274, 'crossentropy': 0.51409384765625}
store['active_learning_steps'][25]['acquisition']={'indices': [['id', 36852], ['id', 48360], ['id', 8443], ['id', 20169], ['id', 52358]], 'labels': [3, 3, 2, 4, 2], 'scores': [0.9210547888741498, 1.7918434434071622, 2.544954310354477, 3.171693788714178, 3.635717544565627]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.78515625, 'crossentropy': 1.148242712020874})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6619741916656494})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5804401636123657})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6271224021911621})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.598848819732666})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5876576900482178})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6988176107406616})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.6712565422058105})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6986424922943115})
store['active_learning_steps'][26]['training']['best_epoch']=6
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.9308, 'crossentropy': 0.5337458984375}
store['active_learning_steps'][26]['acquisition']={'indices': [['id', 22481], ['id', 36126], ['id', 34481], ['id', 3470], ['id', 41572]], 'labels': [7, 5, 3, 2, 6], 'scores': [1.0449769220697522, 2.0374190812428337, 2.8886401035446836, 3.5280841949111004, 3.9705086447847986]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 1.1565284729003906})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5675076246261597})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5865634679794312})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5162101984024048})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5517793893814087})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5293052792549133})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5327425003051758})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6560583114624023})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5942142605781555})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.6443808078765869})
store['active_learning_steps'][27]['training']['best_epoch']=7
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.9369, 'crossentropy': 0.5017279296875}
store['active_learning_steps'][27]['acquisition']={'indices': [['id', 34328], ['id', 37469], ['id', 10894], ['id', 49576], ['id', 15912]], 'labels': [8, 2, 5, 0, 9], 'scores': [1.1456432736842532, 2.1672404269231498, 3.0058125578258377, 3.620419806308491, 4.029925089498321]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.7587890625, 'crossentropy': 1.1416258811950684})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.7513117790222168})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5511859059333801})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.62403804063797})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5964136123657227})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6649012565612793})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5933061838150024})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6373534798622131})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.6688832640647888})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.7383666038513184})
store['active_learning_steps'][28]['training']['best_epoch']=7
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.9317, 'crossentropy': 0.52489677734375}
store['active_learning_steps'][28]['acquisition']={'indices': [['id', 17055], ['id', 50729], ['id', 46441], ['id', 13827], ['id', 40589]], 'labels': [8, 0, 6, 3, 2], 'scores': [1.0344658676710297, 2.003623047949539, 2.8464073748765113, 3.4718216517782414, 3.9130509486033507]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.7236328125, 'crossentropy': 1.2771050930023193})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6717548966407776})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.539704442024231})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5364065170288086})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5540233850479126})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.6136558651924133})
store['active_learning_steps'][29]['training']['best_epoch']=3
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.9336, 'crossentropy': 0.485134228515625}
store['active_learning_steps'][29]['acquisition']={'indices': [['id', 50930], ['id', 49493], ['id', 40654], ['id', 30478], ['id', 33812]], 'labels': [0, 8, 5, 8, 6], 'scores': [0.9101394498157824, 1.7575307765212997, 2.498658365749435, 3.0970463773458707, 3.5578890917015276]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.7998046875, 'crossentropy': 1.1805753707885742})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.7019728422164917})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.581645131111145})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.5939298868179321})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6159754991531372})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5780864357948303})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6854206919670105})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6905815601348877})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.6207074522972107})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.6073034405708313})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.6415818929672241})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.7088915109634399})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.6325407028198242})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.7711606025695801})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.6494817733764648})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6796324253082275})
store['active_learning_steps'][30]['training']['best_epoch']=13
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.9288, 'crossentropy': 0.59024033203125}
store['active_learning_steps'][30]['acquisition']={'indices': [['id', 22083], ['id', 42673], ['id', 9543], ['id', 33338], ['id', 55758]], 'labels': [2, -1, 8, 8, 3], 'scores': [1.201801773987206, 2.30300513391832, 3.1913467901218766, 3.8007912964583177, 4.170071314469755]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.3751451969146729})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6276958584785461})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5963568687438965})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5432736873626709})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.587771475315094})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6364583969116211})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5536377429962158})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.6202165484428406})
store['active_learning_steps'][31]['training']['best_epoch']=5
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.9361, 'crossentropy': 0.5038482421875}
store['active_learning_steps'][31]['acquisition']={'indices': [['id', 470], ['id', 1075], ['id', 8847], ['id', 44756], ['id', 39668]], 'labels': [1, 7, 9, 7, 8], 'scores': [1.0110820792804585, 1.9750256244848359, 2.762037753325865, 3.4017873124493114, 3.8391864138239065]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.7216796875, 'crossentropy': 1.2228953838348389})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5392452478408813})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5562105774879456})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.4895959496498108})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5008318424224854})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5517576336860657})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5964673757553101})
store['active_learning_steps'][32]['training']['best_epoch']=4
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.9404, 'crossentropy': 0.45246689453125}
store['active_learning_steps'][32]['acquisition']={'indices': [['id', 5170], ['id', 9340], ['id', 44969], ['id', 35441], ['id', 48681]], 'labels': [8, 5, 3, 9, 2], 'scores': [1.047753521697918, 1.9447904581570823, 2.7012185941985694, 3.3163771374989466, 3.7672061226389744]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.7392578125, 'crossentropy': 1.156158447265625})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6218822598457336})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5550841093063354})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5565415620803833})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5420312881469727})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5159119963645935})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.6314263343811035})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5720378160476685})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.6526028513908386})
store['active_learning_steps'][33]['training']['best_epoch']=6
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.9385, 'crossentropy': 0.45570625}
store['active_learning_steps'][33]['acquisition']={'indices': [['id', 32880], ['id', 14935], ['id', 46088], ['id', 9396], ['id', 11292]], 'labels': [0, 3, 6, 2, 1], 'scores': [1.0232691473313107, 1.9907887755596438, 2.8117085327165166, 3.422188962688221, 3.8673258783630002]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.78125, 'crossentropy': 1.2664369344711304})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6046639084815979})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5658295750617981})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.49096250534057617})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.48504963517189026})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.49074363708496094})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.494259238243103})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.547406792640686})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.4919373393058777})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5782215595245361})
store['active_learning_steps'][34]['training']['best_epoch']=7
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.947, 'crossentropy': 0.42776103515625}
store['active_learning_steps'][34]['acquisition']={'indices': [['id', 50090], ['id', 46122], ['id', 18049], ['id', 9118], ['id', 52838]], 'labels': [4, 2, 3, 9, 4], 'scores': [1.1842494076144439, 2.173314359270883, 2.998051255196007, 3.6201053834043186, 4.0202684866564535]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.767578125, 'crossentropy': 1.2836545705795288})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.595009446144104})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5090344548225403})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5223733186721802})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.4814220070838928})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.44843411445617676})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5453144907951355})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.4773241877555847})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5799500942230225})
store['active_learning_steps'][35]['training']['best_epoch']=6
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.9468, 'crossentropy': 0.423968212890625}
store['active_learning_steps'][35]['acquisition']={'indices': [['id', 41453], ['id', 24424], ['id', 13969], ['id', 47626], ['id', 49589]], 'labels': [3, 1, 3, -1, 3], 'scores': [1.0999492290062993, 2.091335891641667, 2.9068771667765985, 3.5162012841665824, 3.9348128425198174]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 1.4849998950958252})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.7056871056556702})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5907593965530396})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6661654710769653})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5575737953186035})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5917341709136963})
store['active_learning_steps'][36]['training']['best_epoch']=3
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.924, 'crossentropy': 0.563868994140625}
store['active_learning_steps'][36]['acquisition']={'indices': [['id', 36268], ['id', 49656], ['id', 19015], ['id', 31014], ['id', 7612]], 'labels': [5, 9, 3, 8, 2], 'scores': [0.8541668170806016, 1.6230364055082256, 2.304014663307739, 2.892795298966191, 3.366644571955413]}
store['active_learning_steps'].append({})
store['active_learning_steps'][37]['training']={}
store['active_learning_steps'][37]['training']['epochs']=[]
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.7333984375, 'crossentropy': 1.2590346336364746})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6677100658416748})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5689519643783569})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.548970639705658})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.527635395526886})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5541062355041504})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5280637145042419})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6258620619773865})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.578015923500061})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.580001950263977})
store['active_learning_steps'][37]['training']['best_epoch']=7
store['active_learning_steps'][37]['evaluation_metrics']={'accuracy': 0.9335, 'crossentropy': 0.515794091796875}
