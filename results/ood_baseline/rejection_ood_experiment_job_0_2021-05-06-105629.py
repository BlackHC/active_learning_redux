store = {}
store['timestamp']=1620294989
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/rejection_ood_experiment.py', '--id=0']
store['commit']='2edd2424ec449a84ea20a7324261784a7627b78d'
store['github_url']='2edd2424ec449a84ea20a7324261784a7627b78d'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/rejection_ood_experiment.py'
store['job_id']=0
store['worker_id']=0
store['num_workers']=40
store['config']={'seed': 0, 'acquisition_size': 5, 'max_training_set': 450, 'num_pool_samples': 100, 'num_eval_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'validation_set_size': 1024, 'validation_split_random_state': 0, 'initial_training_set_size': 20, 'samples_per_epoch': 5056, 'mnist_repetitions': 1, 'add_dataset_noise': False, 'acquisition_function': 'batchbald_redux.acquisition_functions.BALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationPoolModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 0.0}
store['log']={}
store['dataset_info']={'training': "(FastMNIST (train; 58976 samples)) + ('OoD Dataset (60000 samples)' | constant_target{'target': tensor(-1, device='cuda:0'), 'num_classes': 10})", 'test': "'FastMNIST (test, 10000 samples)'"}
store['initial_training_set_indices']=[30392, 53434, 12640, 8533, 22304, 37915, 58226, 44119, 3091, 14640, 58125, 39579, 43812, 53689, 52296, 46037, 22015, 40334, 57520, 43803]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 2.4180450439453125})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 2.85390043258667})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 3.207883358001709})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 3.291226863861084})
store['active_learning_steps'][0]['training']['best_epoch']=1
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.6532, 'crossentropy': 2.250305859375}
store['active_learning_steps'][0]['acquisition']={'indices': [29438, 34775, 39179, 22583, 42245], 'labels': [0, 0, 9, 0, 0], 'scores': [1.303482174873352, 1.2828190326690674, 1.2660528421401978, 1.2463661432266235, 1.240776538848877]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 2.6592540740966797})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.599609375, 'crossentropy': 2.9508962631225586})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.5986328125, 'crossentropy': 3.224501132965088})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.5810546875, 'crossentropy': 3.8292481899261475})
store['active_learning_steps'][1]['training']['best_epoch']=1
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.647, 'crossentropy': 2.34136875}
store['active_learning_steps'][1]['acquisition']={'indices': [885, 13827, 9309, 22677, 5819], 'labels': [8, 3, 8, 4, 8], 'scores': [1.1043131351470947, 1.0799082517623901, 1.0786112546920776, 1.0746398568153381, 1.0742213726043701]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 2.25083065032959})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 2.848525047302246})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 3.0556492805480957})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 3.0146398544311523})
store['active_learning_steps'][2]['training']['best_epoch']=1
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.6472, 'crossentropy': 2.057237890625}
store['active_learning_steps'][2]['acquisition']={'indices': [44963, 39697, 4221, 42530, 13828], 'labels': [6, 6, 6, 6, 6], 'scores': [1.0724838376045227, 1.053804099559784, 1.051371693611145, 1.0476728081703186, 1.0453857779502869]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 2.1069865226745605})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 2.1892409324645996})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 2.8480234146118164})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 2.8631348609924316})
store['active_learning_steps'][3]['training']['best_epoch']=1
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.6891, 'crossentropy': 1.85695546875}
store['active_learning_steps'][3]['acquisition']={'indices': [4727, 25341, 57736, 42687, 14679], 'labels': [8, 8, 8, 5, 8], 'scores': [1.076895296573639, 1.0214194059371948, 1.0094789266586304, 0.994877278804779, 0.9910755753517151]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 2.0749101638793945})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 2.216986656188965})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 2.4906156063079834})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 2.516939640045166})
store['active_learning_steps'][4]['training']['best_epoch']=1
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.6645, 'crossentropy': 1.8306728515625}
store['active_learning_steps'][4]['acquisition']={'indices': [244, 8656, 14761, 37161, 11087], 'labels': [5, 5, 3, 3, 8], 'scores': [1.0075796842575073, 0.9859415888786316, 0.9795917272567749, 0.9769684076309204, 0.9682072997093201]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 1.9040679931640625})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 2.3156793117523193})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 2.341073989868164})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 2.350369453430176})
store['active_learning_steps'][5]['training']['best_epoch']=1
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.6948, 'crossentropy': 1.684555078125}
store['active_learning_steps'][5]['acquisition']={'indices': [22974, 55109, 7965, 43904, 32678], 'labels': [4, 4, 4, 4, 2], 'scores': [1.0447802543640137, 1.027880072593689, 1.02430659532547, 1.0148091316223145, 1.0003136992454529]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 1.7875394821166992})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 2.003971815109253})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7353515625, 'crossentropy': 1.9704220294952393})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7265625, 'crossentropy': 2.1750617027282715})
store['active_learning_steps'][6]['training']['best_epoch']=1
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.7045, 'crossentropy': 1.6019244140625}
store['active_learning_steps'][6]['acquisition']={'indices': [8886, 3868, 4530, 10986, 23114], 'labels': [2, 7, 7, 7, 2], 'scores': [1.1251497268676758, 1.099515438079834, 1.0249271988868713, 1.022890865802765, 1.007405400276184]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.740234375, 'crossentropy': 1.4144766330718994})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7412109375, 'crossentropy': 1.7443972826004028})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7529296875, 'crossentropy': 1.8370380401611328})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.74609375, 'crossentropy': 1.9982249736785889})
store['active_learning_steps'][7]['training']['best_epoch']=1
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.7492, 'crossentropy': 1.32607353515625}
store['active_learning_steps'][7]['acquisition']={'indices': [29681, 14418, 47365, 2278, 35606], 'labels': [2, 6, 4, 0, 2], 'scores': [1.0219151377677917, 1.0046591758728027, 0.986763596534729, 0.985325038433075, 0.984449028968811]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.78515625, 'crossentropy': 1.1075475215911865})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7919921875, 'crossentropy': 1.3288867473602295})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7841796875, 'crossentropy': 1.4782733917236328})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.78125, 'crossentropy': 1.7282428741455078})
store['active_learning_steps'][8]['training']['best_epoch']=1
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.8053, 'crossentropy': 0.9685705078125}
store['active_learning_steps'][8]['acquisition']={'indices': [56065, 45845, 44882, 20473, 47171], 'labels': [2, 2, 9, 2, 2], 'scores': [0.9197913408279419, 0.9023904204368591, 0.8881239891052246, 0.88104248046875, 0.8779079914093018]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7763671875, 'crossentropy': 1.1311471462249756})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.798828125, 'crossentropy': 1.421785593032837})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8046875, 'crossentropy': 1.4430124759674072})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 1.7232003211975098})
store['active_learning_steps'][9]['training']['best_epoch']=1
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.7812, 'crossentropy': 1.0668556640625}
store['active_learning_steps'][9]['acquisition']={'indices': [20641, 59314, 28512, 44948, 27139], 'labels': [9, 9, 5, 9, 5], 'scores': [0.8554493188858032, 0.8125566244125366, 0.8067585229873657, 0.7923203706741333, 0.7818321585655212]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.74609375, 'crossentropy': 1.292952537536621})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.806640625, 'crossentropy': 1.1950154304504395})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7998046875, 'crossentropy': 1.5406662225723267})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 1.4806082248687744})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7978515625, 'crossentropy': 1.4902563095092773})
store['active_learning_steps'][10]['training']['best_epoch']=2
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.819, 'crossentropy': 1.0804689453125}
store['active_learning_steps'][10]['acquisition']={'indices': [12196, 19586, 25309, 8924, 11202], 'labels': [2, 9, 2, 2, 9], 'scores': [1.1157841086387634, 1.0396771430969238, 1.0336151123046875, 1.0310288667678833, 1.0267430543899536]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.775390625, 'crossentropy': 1.1311262845993042})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.7900390625, 'crossentropy': 1.3061015605926514})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 1.3655900955200195})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 1.4184958934783936})
store['active_learning_steps'][11]['training']['best_epoch']=1
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.8074, 'crossentropy': 1.020846484375}
store['active_learning_steps'][11]['acquisition']={'indices': [55503, 41593, 57956, 36229, 51673], 'labels': [0, 2, 2, 2, 2], 'scores': [0.8618482351303101, 0.8395800590515137, 0.8375914096832275, 0.8290941119194031, 0.8276436924934387]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.7568359375, 'crossentropy': 1.237056016921997})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.7724609375, 'crossentropy': 1.4531564712524414})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.76953125, 'crossentropy': 1.5546460151672363})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.79296875, 'crossentropy': 1.6452326774597168})
store['active_learning_steps'][12]['training']['best_epoch']=1
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.776, 'crossentropy': 1.15966123046875}
store['active_learning_steps'][12]['acquisition']={'indices': [36122, 19829, 52169, 14405, 29132], 'labels': [9, 3, 2, 6, 8], 'scores': [0.8334436416625977, 0.8152433037757874, 0.8086127638816833, 0.8027552366256714, 0.798187255859375]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.7998046875, 'crossentropy': 1.0425130128860474})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 1.0443089008331299})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 1.1123154163360596})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 1.0829517841339111})
store['active_learning_steps'][13]['training']['best_epoch']=1
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.8093, 'crossentropy': 0.98246767578125}
store['active_learning_steps'][13]['acquisition']={'indices': [47643, 28413, 51950, 28375, 28477], 'labels': [3, 5, 5, 5, 5], 'scores': [0.7885453104972839, 0.7619225978851318, 0.7531620264053345, 0.7486647963523865, 0.7481217980384827]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.7578125, 'crossentropy': 1.1947810649871826})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.7880859375, 'crossentropy': 1.2525384426116943})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 1.3197336196899414})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.7939453125, 'crossentropy': 1.346203088760376})
store['active_learning_steps'][14]['training']['best_epoch']=1
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.7842, 'crossentropy': 1.122890234375}
store['active_learning_steps'][14]['acquisition']={'indices': [12413, 56121, 38615, 51205, 19869], 'labels': [7, 7, 7, 7, 7], 'scores': [0.8403106331825256, 0.8396427035331726, 0.8393124938011169, 0.8328822255134583, 0.8252837061882019]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 0.9492570161819458})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 0.9480329751968384})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 1.0494234561920166})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 1.0651270151138306})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 1.1862657070159912})
store['active_learning_steps'][15]['training']['best_epoch']=2
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.8552, 'crossentropy': 0.87330380859375}
store['active_learning_steps'][15]['acquisition']={'indices': [8691, 58560, 57510, 34481, 50403], 'labels': [2, 0, 5, 3, -1], 'scores': [0.9975610971450806, 0.9917624592781067, 0.9753413200378418, 0.9737177491188049, 0.967079758644104]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.779296875, 'crossentropy': 1.061464548110962})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 1.1207712888717651})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 1.0434176921844482})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 1.207254409790039})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 1.1214591264724731})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 1.2706600427627563})
store['active_learning_steps'][16]['training']['best_epoch']=3
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.8586, 'crossentropy': 0.873502734375}
store['active_learning_steps'][16]['acquisition']={'indices': [26733, 28666, 4955, 20170, 31090], 'labels': [2, 5, 2, 9, 4], 'scores': [1.0391464829444885, 1.0283443331718445, 1.0090795755386353, 1.0082886219024658, 0.9965733289718628]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 1.0312083959579468})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.8483973741531372})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 1.0398674011230469})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 1.0932857990264893})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 1.3685715198516846})
store['active_learning_steps'][17]['training']['best_epoch']=2
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.8593, 'crossentropy': 0.8394810546875}
store['active_learning_steps'][17]['acquisition']={'indices': [33222, 1024, 50320, 51414, 49316], 'labels': [5, 5, 5, 8, 5], 'scores': [0.9818808436393738, 0.960999608039856, 0.9523869156837463, 0.9179638028144836, 0.916964054107666]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.7470703125, 'crossentropy': 1.0508531332015991})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 0.9217855930328369})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 0.9346487522125244})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 0.9553672075271606})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 1.1049094200134277})
store['active_learning_steps'][18]['training']['best_epoch']=2
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.833, 'crossentropy': 0.88888955078125}
store['active_learning_steps'][18]['acquisition']={'indices': [363, 17756, 40431, 42141, 40489], 'labels': [-1, 8, 5, 5, 5], 'scores': [0.977067768573761, 0.9567369818687439, 0.9519243836402893, 0.9381238222122192, 0.9367323517799377]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.7685546875, 'crossentropy': 1.0475984811782837})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 0.9600474834442139})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 0.9745450615882874})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 1.0708425045013428})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 1.1896770000457764})
store['active_learning_steps'][19]['training']['best_epoch']=2
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.8577, 'crossentropy': 0.82013076171875}
store['active_learning_steps'][19]['acquisition']={'indices': [54688, 37720, 37871, 29900, 16113], 'labels': [7, 8, 7, 7, 7], 'scores': [1.035355269908905, 1.0345857739448547, 1.0196055173873901, 1.017005980014801, 0.992459237575531]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.7919921875, 'crossentropy': 0.9627107381820679})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.7336550354957581})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.8185272216796875})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.9216946959495544})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.8918886184692383})
store['active_learning_steps'][20]['training']['best_epoch']=2
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.8645, 'crossentropy': 0.729978662109375}
store['active_learning_steps'][20]['acquisition']={'indices': [50403, 2118, 50858, 19111, 1674], 'labels': [-1, 7, 4, 4, 9], 'scores': [0.8821516633033752, 0.8791307806968689, 0.8762121200561523, 0.8695463538169861, 0.8682899475097656]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.7470703125, 'crossentropy': 1.0793523788452148})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.8090858459472656})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.9244008660316467})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.8673598170280457})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 1.0820595026016235})
store['active_learning_steps'][21]['training']['best_epoch']=2
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.8697, 'crossentropy': 0.75140615234375}
store['active_learning_steps'][21]['acquisition']={'indices': [28373, 21023, 19942, 46088, 6560], 'labels': [4, 2, 5, 6, 4], 'scores': [0.8899691700935364, 0.887834906578064, 0.8795442581176758, 0.8785768747329712, 0.8707513809204102]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.798828125, 'crossentropy': 0.9480772614479065})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 0.8486236333847046})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 0.9031558036804199})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 1.0873236656188965})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.916449785232544})
store['active_learning_steps'][22]['training']['best_epoch']=2
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.8537, 'crossentropy': 0.815946533203125}
store['active_learning_steps'][22]['acquisition']={'indices': [3268, 9180, 48006, 17129, 33812], 'labels': [6, 3, 6, 1, 6], 'scores': [0.9077887535095215, 0.8989707827568054, 0.8832904696464539, 0.8826871514320374, 0.8810837268829346]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 0.9061367511749268})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.7673779726028442})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.8358943462371826})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.7878806591033936})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.857276439666748})
store['active_learning_steps'][23]['training']['best_epoch']=2
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.88, 'crossentropy': 0.690250732421875}
store['active_learning_steps'][23]['acquisition']={'indices': [35232, 35435, 56212, 49493, 49509], 'labels': [8, 1, 9, 8, 8], 'scores': [0.8287745714187622, 0.8019155859947205, 0.7860051393508911, 0.7771532535552979, 0.7732897996902466]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 0.9159874320030212})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.7266173362731934})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.7501319646835327})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.7924573421478271})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.7071002721786499})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.7117273211479187})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.7394747734069824})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.7540223598480225})
store['active_learning_steps'][24]['training']['best_epoch']=5
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.907, 'crossentropy': 0.631757421875}
store['active_learning_steps'][24]['acquisition']={'indices': [37469, 59747, 47260, 4226, 34829], 'labels': [2, 5, 6, 7, 5], 'scores': [1.0544871091842651, 1.0303590893745422, 1.0176656246185303, 0.9974719285964966, 0.9944296479225159]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.796875, 'crossentropy': 0.9335702657699585})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6762163639068604})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.7194151878356934})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.662276029586792})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.692595899105072})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.7570173740386963})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.8577088117599487})
store['active_learning_steps'][25]['training']['best_epoch']=4
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.9172, 'crossentropy': 0.607317724609375}
store['active_learning_steps'][25]['acquisition']={'indices': [32427, 24722, 33505, 11298, 22053], 'labels': [0, 2, 2, 2, 5], 'scores': [1.0531843900680542, 1.0310607552528381, 1.0303524732589722, 0.9906076788902283, 0.9901934862136841]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 1.0001071691513062})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.6699479818344116})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.7860192060470581})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.659186840057373})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.7779735326766968})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.7650842070579529})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.7288445234298706})
store['active_learning_steps'][26]['training']['best_epoch']=4
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.9003, 'crossentropy': 0.652430712890625}
store['active_learning_steps'][26]['acquisition']={'indices': [16860, 18150, 26072, 24587, 34881], 'labels': [8, 8, 1, 8, 7], 'scores': [1.0530177354812622, 1.0407306551933289, 0.9729487895965576, 0.9659883379936218, 0.9460362195968628]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 1.0142443180084229})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.7466840744018555})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6060312390327454})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6764696836471558})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6167924404144287})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.7488747239112854})
store['active_learning_steps'][27]['training']['best_epoch']=3
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.9171, 'crossentropy': 0.567947216796875}
store['active_learning_steps'][27]['acquisition']={'indices': [39668, 15276, 11711, 59401, 43042], 'labels': [8, 7, 2, 4, 8], 'scores': [0.9742207527160645, 0.9612410664558411, 0.9547019600868225, 0.9336158037185669, 0.9289397597312927]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.740234375, 'crossentropy': 1.1047399044036865})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6634573340415955})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.7010259628295898})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6750741004943848})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6292123794555664})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6682043075561523})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.7737709283828735})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.7075768709182739})
store['active_learning_steps'][28]['training']['best_epoch']=5
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.9151, 'crossentropy': 0.583009033203125}
store['active_learning_steps'][28]['acquisition']={'indices': [49091, 5679, 6604, 5328, 52713], 'labels': [3, 3, 8, 3, 3], 'scores': [1.0312028527259827, 1.0046201348304749, 0.9850773811340332, 0.9821270704269409, 0.9796819686889648]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.775390625, 'crossentropy': 1.0386357307434082})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6401076912879944})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5901284217834473})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.713683009147644})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6672760844230652})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.7077673673629761})
store['active_learning_steps'][29]['training']['best_epoch']=3
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.9135, 'crossentropy': 0.55335009765625}
store['active_learning_steps'][29]['acquisition']={'indices': [29764, 34524, 42313, 39864, 31184], 'labels': [4, 8, 8, 8, 9], 'scores': [0.9728519916534424, 0.9578879475593567, 0.9570689797401428, 0.9568965435028076, 0.9542607069015503]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.8076171875, 'crossentropy': 1.07831609249115})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6674416065216064})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5908350944519043})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5788977742195129})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6644701957702637})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6428704261779785})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6479437351226807})
store['active_learning_steps'][30]['training']['best_epoch']=4
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.915, 'crossentropy': 0.58068486328125}
store['active_learning_steps'][30]['acquisition']={'indices': [57507, 57575, 40457, 5175, 56190], 'labels': [0, 0, 0, 4, 4], 'scores': [1.0348547101020813, 1.0062938332557678, 0.9778968691825867, 0.9754528403282166, 0.9709244966506958]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 1.0447678565979004})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.5986509323120117})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5825597047805786})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5924216508865356})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.546648383140564})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5553984642028809})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5891878008842468})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5710936784744263})
store['active_learning_steps'][31]['training']['best_epoch']=5
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.9237, 'crossentropy': 0.556124072265625}
store['active_learning_steps'][31]['acquisition']={'indices': [42078, 59468, 424, 2548, 16628], 'labels': [4, 7, 9, 4, 9], 'scores': [0.9741820693016052, 0.9633226990699768, 0.9633140563964844, 0.944736897945404, 0.9424066543579102]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.75390625, 'crossentropy': 0.9384083151817322})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5096248388290405})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.45732927322387695})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.49205970764160156})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.4816909730434418})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.5057317018508911})
store['active_learning_steps'][32]['training']['best_epoch']=3
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.9294, 'crossentropy': 0.47859267578125}
store['active_learning_steps'][32]['acquisition']={'indices': [36072, 42004, 12305, 43950, 59418], 'labels': [2, 7, 9, 9, 0], 'scores': [0.9695122241973877, 0.9670069217681885, 0.9583263993263245, 0.932530403137207, 0.9314271807670593]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 0.9652078151702881})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5873419046401978})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6015611886978149})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5959365367889404})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5731412768363953})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5876606106758118})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.652138352394104})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5740591287612915})
store['active_learning_steps'][33]['training']['best_epoch']=5
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.9232, 'crossentropy': 0.52985087890625}
store['active_learning_steps'][33]['acquisition']={'indices': [15899, 41323, 15134, 181, 59339], 'labels': [9, 6, 6, 3, 1], 'scores': [1.0309200286865234, 1.0300339460372925, 1.0228844285011292, 1.0171565413475037, 1.0168421268463135]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.7978515625, 'crossentropy': 1.0771818161010742})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6402861475944519})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5436486601829529})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5462408661842346})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5396952033042908})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5289500951766968})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5834053754806519})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6151056885719299})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5829250812530518})
store['active_learning_steps'][34]['training']['best_epoch']=6
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.9328, 'crossentropy': 0.468832421875}
store['active_learning_steps'][34]['acquisition']={'indices': [10210, 49487, 51863, 641, 35246], 'labels': [3, 8, 9, 9, 8], 'scores': [1.0999757051467896, 1.009852409362793, 0.9863929748535156, 0.9725741744041443, 0.9660598039627075]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.8046875, 'crossentropy': 1.0393744707107544})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5322501063346863})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.521419882774353})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.489027738571167})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5134534239768982})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5382766723632812})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.55535888671875})
store['active_learning_steps'][35]['training']['best_epoch']=4
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.9324, 'crossentropy': 0.482101904296875}
store['active_learning_steps'][35]['acquisition']={'indices': [42559, 40116, 18473, 8744, 21164], 'labels': [-1, 4, 4, 5, 2], 'scores': [0.9036893844604492, 0.9026018977165222, 0.8976710438728333, 0.8941571116447449, 0.8878751993179321]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.7568359375, 'crossentropy': 1.0674381256103516})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5931448936462402})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5061295032501221})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.508671224117279})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5233153700828552})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5467925667762756})
store['active_learning_steps'][36]['training']['best_epoch']=3
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.9364, 'crossentropy': 0.45653681640625}
store['active_learning_steps'][36]['acquisition']={'indices': [10256, 46379, 43711, 8765, 22531], 'labels': [2, 3, 3, 3, 4], 'scores': [0.8373368382453918, 0.8314509391784668, 0.8245452642440796, 0.809490442276001, 0.8072012066841125]}
store['active_learning_steps'].append({})
store['active_learning_steps'][37]['training']={}
store['active_learning_steps'][37]['training']['epochs']=[]
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.76171875, 'crossentropy': 1.0611125230789185})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.636605978012085})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5349040031433105})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5002513527870178})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5051509737968445})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5251538753509521})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5475211143493652})
store['active_learning_steps'][37]['training']['best_epoch']=4
store['active_learning_steps'][37]['evaluation_metrics']={'accuracy': 0.938, 'crossentropy': 0.446092724609375}
store['active_learning_steps'][37]['acquisition']={'indices': [2765, 15191, 29591, 24300, 49364], 'labels': [0, 0, 9, 9, 7], 'scores': [1.024910807609558, 0.9607025384902954, 0.933896005153656, 0.9292911291122437, 0.9283313751220703]}
store['active_learning_steps'].append({})
store['active_learning_steps'][38]['training']={}
store['active_learning_steps'][38]['training']['epochs']=[]
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 1.0531656742095947})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5990768671035767})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.46967798471450806})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.48674917221069336})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.5106629133224487})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.48924440145492554})
store['active_learning_steps'][38]['training']['best_epoch']=3
store['active_learning_steps'][38]['evaluation_metrics']={'accuracy': 0.9313, 'crossentropy': 0.470109375}
store['active_learning_steps'][38]['acquisition']={'indices': [3470, 17491, 11708, 5600, 57523], 'labels': [2, 3, 3, 6, 3], 'scores': [0.8731340169906616, 0.8481611609458923, 0.8362574577331543, 0.8295500874519348, 0.8287314176559448]}
store['active_learning_steps'].append({})
store['active_learning_steps'][39]['training']={}
store['active_learning_steps'][39]['training']['epochs']=[]
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.7626953125, 'crossentropy': 1.1527855396270752})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6858844757080078})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.4809872806072235})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5087472200393677})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.44940823316574097})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5128786563873291})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.4592827558517456})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.516262948513031})
store['active_learning_steps'][39]['training']['best_epoch']=5
store['active_learning_steps'][39]['evaluation_metrics']={'accuracy': 0.9404, 'crossentropy': 0.439639501953125}
store['active_learning_steps'][39]['acquisition']={'indices': [45069, 58390, 12663, 46368, 17478], 'labels': [4, 4, 8, 8, 4], 'scores': [1.01683109998703, 0.9308072328567505, 0.9194772839546204, 0.9191299080848694, 0.9127882719039917]}
store['active_learning_steps'].append({})
store['active_learning_steps'][40]['training']={}
store['active_learning_steps'][40]['training']['epochs']=[]
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.7412109375, 'crossentropy': 1.1248745918273926})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.6021171808242798})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5110487937927246})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.4657408595085144})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.4814825654029846})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4777897596359253})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5374784469604492})
store['active_learning_steps'][40]['training']['best_epoch']=4
store['active_learning_steps'][40]['evaluation_metrics']={'accuracy': 0.9353, 'crossentropy': 0.458243896484375}
store['active_learning_steps'][40]['acquisition']={'indices': [55043, 52889, 44745, 8731, 20402], 'labels': [-1, -1, -1, 5, 9], 'scores': [0.9602019190788269, 0.9499662518501282, 0.9160345196723938, 0.8685224652290344, 0.8678078651428223]}
store['active_learning_steps'].append({})
store['active_learning_steps'][41]['training']={}
store['active_learning_steps'][41]['training']['epochs']=[]
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.7373046875, 'crossentropy': 1.1073154211044312})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.669091522693634})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5526083111763})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.47258317470550537})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5371414422988892})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5345548391342163})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6048020720481873})
store['active_learning_steps'][41]['training']['best_epoch']=4
store['active_learning_steps'][41]['evaluation_metrics']={'accuracy': 0.9315, 'crossentropy': 0.478802978515625}
store['active_learning_steps'][41]['acquisition']={'indices': [46126, 10350, 2381, 56561, 16219], 'labels': [3, -1, 7, -1, 5], 'scores': [0.9560934901237488, 0.9260647296905518, 0.9201121926307678, 0.9201041460037231, 0.9079300165176392]}
store['active_learning_steps'].append({})
store['active_learning_steps'][42]['training']={}
store['active_learning_steps'][42]['training']['epochs']=[]
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.775390625, 'crossentropy': 1.0593429803848267})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5929005742073059})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5328537225723267})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.4338449239730835})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5299617052078247})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.48753076791763306})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.511290967464447})
store['active_learning_steps'][42]['training']['best_epoch']=4
store['active_learning_steps'][42]['evaluation_metrics']={'accuracy': 0.9443, 'crossentropy': 0.429797119140625}
store['active_learning_steps'][42]['acquisition']={'indices': [22083, 57474, 47741, 8447, 15252], 'labels': [2, 3, 5, 3, 1], 'scores': [0.9428248405456543, 0.9159160852432251, 0.8936933279037476, 0.8764396905899048, 0.873245358467102]}
store['active_learning_steps'].append({})
store['active_learning_steps'][43]['training']={}
store['active_learning_steps'][43]['training']['epochs']=[]
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.744140625, 'crossentropy': 1.103644609451294})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5582916140556335})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5129404067993164})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4480728507041931})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.448178768157959})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.3942174017429352})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4586440324783325})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4601267874240875})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.44741225242614746})
store['active_learning_steps'][43]['training']['best_epoch']=6
store['active_learning_steps'][43]['evaluation_metrics']={'accuracy': 0.9448, 'crossentropy': 0.4078565673828125}
store['active_learning_steps'][43]['acquisition']={'indices': [16836, 36878, 30418, 52889, 45602], 'labels': [7, 8, 8, -1, 5], 'scores': [1.0108967423439026, 0.988787829875946, 0.983232319355011, 0.9689579010009766, 0.9617647528648376]}
store['active_learning_steps'].append({})
store['active_learning_steps'][44]['training']={}
store['active_learning_steps'][44]['training']['epochs']=[]
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.771484375, 'crossentropy': 1.1171784400939941})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5925949215888977})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.475455105304718})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.46895188093185425})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.47851574420928955})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.423708438873291})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.44399863481521606})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.4431662857532501})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.42967110872268677})
store['active_learning_steps'][44]['training']['best_epoch']=6
store['active_learning_steps'][44]['evaluation_metrics']={'accuracy': 0.9503, 'crossentropy': 0.419592529296875}
store['active_learning_steps'][44]['acquisition']={'indices': [52889, 56414, 52294, 7829, 16011], 'labels': [-1, -1, 0, -1, 5], 'scores': [1.0030022263526917, 1.0007379651069641, 0.9693573117256165, 0.9622077941894531, 0.9544263482093811]}
store['active_learning_steps'].append({})
store['active_learning_steps'][45]['training']={}
store['active_learning_steps'][45]['training']['epochs']=[]
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.7412109375, 'crossentropy': 1.2423558235168457})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.626217246055603})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.546585202217102})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.4372621178627014})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.4889872074127197})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4426444172859192})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.4653966724872589})
store['active_learning_steps'][45]['training']['best_epoch']=4
store['active_learning_steps'][45]['evaluation_metrics']={'accuracy': 0.9443, 'crossentropy': 0.4426958984375}
store['active_learning_steps'][45]['acquisition']={'indices': [18487, 1075, 41608, 57972, 40066], 'labels': [4, 7, -1, 4, 4], 'scores': [0.9753214120864868, 0.9448865056037903, 0.9411228895187378, 0.9349459409713745, 0.9308155179023743]}
store['active_learning_steps'].append({})
store['active_learning_steps'][46]['training']={}
store['active_learning_steps'][46]['training']['epochs']=[]
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.7392578125, 'crossentropy': 1.1323316097259521})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6148958206176758})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5878413319587708})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5220195651054382})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5205445289611816})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5182529091835022})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4710471034049988})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.4631073474884033})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.4792535603046417})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.49387258291244507})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.535845160484314})
store['active_learning_steps'][46]['training']['best_epoch']=8
store['active_learning_steps'][46]['evaluation_metrics']={'accuracy': 0.9436, 'crossentropy': 0.45035107421875}
store['active_learning_steps'][46]['acquisition']={'indices': [20057, 19868, 32880, 37583, 43560], 'labels': [6, 5, 0, -1, 5], 'scores': [1.1230785250663757, 1.087231159210205, 1.0611540079116821, 1.0304515957832336, 1.0159217715263367]}
store['active_learning_steps'].append({})
store['active_learning_steps'][47]['training']={}
store['active_learning_steps'][47]['training']['epochs']=[]
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 1.128955602645874})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.572034478187561})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.464945912361145})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.42998456954956055})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.4037543535232544})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.4916251003742218})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.4373338222503662})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4421895742416382})
store['active_learning_steps'][47]['training']['best_epoch']=5
store['active_learning_steps'][47]['evaluation_metrics']={'accuracy': 0.9384, 'crossentropy': 0.4328123046875}
store['active_learning_steps'][47]['acquisition']={'indices': [41789, 50930, 15701, 17603, 2803], 'labels': [0, 0, 3, 0, 3], 'scores': [0.9844707548618317, 0.9683703184127808, 0.9661390781402588, 0.9374827742576599, 0.9360390901565552]}
store['active_learning_steps'].append({})
store['active_learning_steps'][48]['training']={}
store['active_learning_steps'][48]['training']['epochs']=[]
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.767578125, 'crossentropy': 1.0409237146377563})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5847654342651367})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.43478065729141235})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.43118858337402344})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.434897780418396})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.42132216691970825})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.45785677433013916})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.4787502884864807})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.4609476327896118})
store['active_learning_steps'][48]['training']['best_epoch']=6
store['active_learning_steps'][48]['evaluation_metrics']={'accuracy': 0.9469, 'crossentropy': 0.3811866455078125}
store['active_learning_steps'][48]['acquisition']={'indices': [35401, 42020, 55496, 59731, 56643], 'labels': [3, 9, 9, 5, 2], 'scores': [1.038603127002716, 1.0078820586204529, 0.9968792200088501, 0.986810028553009, 0.971830427646637]}
store['active_learning_steps'].append({})
store['active_learning_steps'][49]['training']={}
store['active_learning_steps'][49]['training']['epochs']=[]
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 1.26866614818573})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.6335119009017944})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.4556683599948883})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.4322657883167267})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.44807225465774536})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.44165974855422974})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.4875316023826599})
store['active_learning_steps'][49]['training']['best_epoch']=4
store['active_learning_steps'][49]['evaluation_metrics']={'accuracy': 0.9425, 'crossentropy': 0.423690380859375}
store['active_learning_steps'][49]['acquisition']={'indices': [49354, 37696, 36704, 34771, 54880], 'labels': [0, 2, 2, 0, 5], 'scores': [0.8917720317840576, 0.8748573064804077, 0.870783805847168, 0.8517358303070068, 0.8441998958587646]}
store['active_learning_steps'].append({})
store['active_learning_steps'][50]['training']={}
store['active_learning_steps'][50]['training']['epochs']=[]
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.73046875, 'crossentropy': 1.1470646858215332})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.576894998550415})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.5405361652374268})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.4893580675125122})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.46853142976760864})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.43965739011764526})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.4786324203014374})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.5182426571846008})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.4775911569595337})
store['active_learning_steps'][50]['training']['best_epoch']=6
store['active_learning_steps'][50]['evaluation_metrics']={'accuracy': 0.9444, 'crossentropy': 0.417196240234375}
store['active_learning_steps'][50]['acquisition']={'indices': [40466, 32776, 58422, 57718, 48382], 'labels': [8, 4, 9, 7, 8], 'scores': [1.0036888122558594, 0.9775329828262329, 0.9755879044532776, 0.9729064106941223, 0.9510581493377686]}
store['active_learning_steps'].append({})
store['active_learning_steps'][51]['training']={}
store['active_learning_steps'][51]['training']['epochs']=[]
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.7890625, 'crossentropy': 1.1772232055664062})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6343234181404114})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.530916690826416})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.4737072288990021})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.49107831716537476})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4574759602546692})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.4977627992630005})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.490422785282135})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.42712604999542236})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.5136576294898987})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.5366982221603394})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.48093223571777344})
store['active_learning_steps'][51]['training']['best_epoch']=9
store['active_learning_steps'][51]['evaluation_metrics']={'accuracy': 0.9499, 'crossentropy': 0.4030143798828125}
store['active_learning_steps'][51]['acquisition']={'indices': [24479, 36818, 56561, 22029, 11292], 'labels': [8, 7, -1, -1, 1], 'scores': [1.1130585074424744, 1.1007940769195557, 1.0613816976547241, 1.0333802103996277, 1.0259297490119934]}
store['active_learning_steps'].append({})
store['active_learning_steps'][52]['training']={}
store['active_learning_steps'][52]['training']['epochs']=[]
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 1.1667920351028442})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6903424263000488})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5447728633880615})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.49167701601982117})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.5031047463417053})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.523087203502655})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5294386744499207})
store['active_learning_steps'][52]['training']['best_epoch']=4
store['active_learning_steps'][52]['evaluation_metrics']={'accuracy': 0.9247, 'crossentropy': 0.53327275390625}
store['active_learning_steps'][52]['acquisition']={'indices': [20110, 56662, 56561, 45954, 36268], 'labels': [4, 0, -1, 8, 5], 'scores': [0.9396161437034607, 0.8948560357093811, 0.8927423357963562, 0.8789421319961548, 0.8642811179161072]}
store['active_learning_steps'].append({})
store['active_learning_steps'][53]['training']={}
store['active_learning_steps'][53]['training']['epochs']=[]
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 1.154634714126587})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.627439558506012})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.4627527594566345})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.445060133934021})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.608498215675354})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.5007286071777344})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.5075633525848389})
store['active_learning_steps'][53]['training']['best_epoch']=4
store['active_learning_steps'][53]['evaluation_metrics']={'accuracy': 0.9427, 'crossentropy': 0.43742353515625}
store['active_learning_steps'][53]['acquisition']={'indices': [52889, 15510, 29376, 9370, 51986], 'labels': [-1, 2, -1, 4, 2], 'scores': [0.9022762179374695, 0.8249377012252808, 0.823201060295105, 0.8223016262054443, 0.8133211731910706]}
store['active_learning_steps'].append({})
store['active_learning_steps'][54]['training']={}
store['active_learning_steps'][54]['training']['epochs']=[]
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.771484375, 'crossentropy': 1.2637648582458496})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6135141849517822})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.585899829864502})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.44034820795059204})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.434281587600708})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4838981032371521})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.4616098999977112})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4669753313064575})
store['active_learning_steps'][54]['training']['best_epoch']=5
store['active_learning_steps'][54]['evaluation_metrics']={'accuracy': 0.9489, 'crossentropy': 0.41748154296875}
store['active_learning_steps'][54]['acquisition']={'indices': [3030, 6130, 36126, 54652, 27540], 'labels': [9, 7, 5, -1, -1], 'scores': [0.9984039068222046, 0.961870551109314, 0.9602509140968323, 0.9564919471740723, 0.9466660618782043]}
store['active_learning_steps'].append({})
store['active_learning_steps'][55]['training']={}
store['active_learning_steps'][55]['training']['epochs']=[]
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.73046875, 'crossentropy': 1.266981840133667})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6466097831726074})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5323485732078552})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.45006173849105835})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.45731866359710693})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5564826130867004})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.47559887170791626})
store['active_learning_steps'][55]['training']['best_epoch']=4
store['active_learning_steps'][55]['evaluation_metrics']={'accuracy': 0.9445, 'crossentropy': 0.419742333984375}
store['active_learning_steps'][55]['acquisition']={'indices': [20169, 25873, 58379, 31429, 49192], 'labels': [4, 8, -1, -1, 2], 'scores': [0.913706362247467, 0.8879550099372864, 0.8869599103927612, 0.8758273720741272, 0.8704975843429565]}
store['active_learning_steps'].append({})
store['active_learning_steps'][56]['training']={}
store['active_learning_steps'][56]['training']['epochs']=[]
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.7841796875, 'crossentropy': 1.1717877388000488})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6599019765853882})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5059300661087036})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.47463658452033997})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.48319074511528015})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.47640037536621094})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.4571612477302551})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.5079158544540405})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.5059866905212402})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.481334924697876})
store['active_learning_steps'][56]['training']['best_epoch']=7
store['active_learning_steps'][56]['evaluation_metrics']={'accuracy': 0.9453, 'crossentropy': 0.414865087890625}
store['active_learning_steps'][56]['acquisition']={'indices': [52808, 53990, 47949, 50960, 52889], 'labels': [8, -1, 5, -1, -1], 'scores': [0.9963863492012024, 0.9884401559829712, 0.9879904389381409, 0.967851996421814, 0.9617348909378052]}
store['active_learning_steps'].append({})
store['active_learning_steps'][57]['training']={}
store['active_learning_steps'][57]['training']['epochs']=[]
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.7509765625, 'crossentropy': 1.3178844451904297})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 0.8498729467391968})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.612701416015625})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.511854887008667})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6427919864654541})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.5088674426078796})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.5480128526687622})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.5230898857116699})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.5329195857048035})
store['active_learning_steps'][57]['training']['best_epoch']=6
store['active_learning_steps'][57]['evaluation_metrics']={'accuracy': 0.9441, 'crossentropy': 0.45761142578125}
store['active_learning_steps'][57]['acquisition']={'indices': [21601, 52095, 51464, 52889, 6818], 'labels': [1, 0, 0, -1, -1], 'scores': [1.0367323756217957, 0.9939254522323608, 0.9628705382347107, 0.9578590393066406, 0.9415252208709717]}
store['active_learning_steps'].append({})
store['active_learning_steps'][58]['training']={}
store['active_learning_steps'][58]['training']['epochs']=[]
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.740234375, 'crossentropy': 1.2974648475646973})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6466168165206909})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.48906409740448})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.52036452293396})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.44370603561401367})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.4392450153827667})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.4394616186618805})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.4467064142227173})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.47550684213638306})
store['active_learning_steps'][58]['training']['best_epoch']=6
store['active_learning_steps'][58]['evaluation_metrics']={'accuracy': 0.9462, 'crossentropy': 0.41175859375}
store['active_learning_steps'][58]['acquisition']={'indices': [47479, 13554, 31293, 27740, 41426], 'labels': [0, 8, 8, 8, 4], 'scores': [0.9915758967399597, 0.9765591621398926, 0.9314525723457336, 0.923180341720581, 0.921114981174469]}
store['active_learning_steps'].append({})
store['active_learning_steps'][59]['training']={}
store['active_learning_steps'][59]['training']['epochs']=[]
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 1.3791565895080566})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.6857032775878906})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.6285684108734131})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.5127217173576355})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.4886725842952728})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.5115588307380676})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.4893755614757538})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.5190340876579285})
store['active_learning_steps'][59]['training']['best_epoch']=5
store['active_learning_steps'][59]['evaluation_metrics']={'accuracy': 0.9427, 'crossentropy': 0.46872109375}
store['active_learning_steps'][59]['acquisition']={'indices': [49505, 59574, 33073, 22364, 7782], 'labels': [6, 5, 6, 0, 2], 'scores': [0.9468291401863098, 0.9016280174255371, 0.8834168910980225, 0.8803271651268005, 0.8766182065010071]}
store['active_learning_steps'].append({})
store['active_learning_steps'][60]['training']={}
store['active_learning_steps'][60]['training']['epochs']=[]
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 1.3878490924835205})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.6354025602340698})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.48495161533355713})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.5169029235839844})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.4603731632232666})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.49691295623779297})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4839664399623871})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.480040967464447})
store['active_learning_steps'][60]['training']['best_epoch']=5
store['active_learning_steps'][60]['evaluation_metrics']={'accuracy': 0.9435, 'crossentropy': 0.422764013671875}
store['active_learning_steps'][60]['acquisition']={'indices': [13524, 37829, 53872, 33429, 7924], 'labels': [3, 6, 8, 6, 8], 'scores': [0.9298233985900879, 0.9066092669963837, 0.8960253000259399, 0.8848797082901001, 0.8838944435119629]}
store['active_learning_steps'].append({})
store['active_learning_steps'][61]['training']={}
store['active_learning_steps'][61]['training']['epochs']=[]
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.7578125, 'crossentropy': 1.125603199005127})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.6056532859802246})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.49838006496429443})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.43325695395469666})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3883725106716156})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.4096641540527344})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.4212503135204315})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3986169695854187})
store['active_learning_steps'][61]['training']['best_epoch']=5
store['active_learning_steps'][61]['evaluation_metrics']={'accuracy': 0.9562, 'crossentropy': 0.3489997802734375}
store['active_learning_steps'][61]['acquisition']={'indices': [56427, 3676, 39627, 39411, 262], 'labels': [2, 2, 2, 2, 2], 'scores': [0.9762789607048035, 0.9740710258483887, 0.9583098888397217, 0.9371560215950012, 0.930351734161377]}
store['active_learning_steps'].append({})
store['active_learning_steps'][62]['training']={}
store['active_learning_steps'][62]['training']['epochs']=[]
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 1.2556369304656982})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.6615397930145264})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.48164576292037964})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.396612286567688})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.47795721888542175})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.4819639027118683})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.38844192028045654})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.4360651969909668})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.4163147211074829})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.39605188369750977})
store['active_learning_steps'][62]['training']['best_epoch']=7
store['active_learning_steps'][62]['evaluation_metrics']={'accuracy': 0.952, 'crossentropy': 0.375042041015625}
store['active_learning_steps'][62]['acquisition']={'indices': [7949, 50421, 35864, 56006, 57665], 'labels': [-1, 8, 5, 3, 8], 'scores': [0.9956831336021423, 0.9507365226745605, 0.9483562111854553, 0.9421929121017456, 0.9383971095085144]}
store['active_learning_steps'].append({})
store['active_learning_steps'][63]['training']={}
store['active_learning_steps'][63]['training']['epochs']=[]
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 1.4012176990509033})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.7134573459625244})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.524286687374115})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.45367735624313354})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.4193422794342041})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.45856863260269165})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.4378122091293335})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.4734550416469574})
store['active_learning_steps'][63]['training']['best_epoch']=5
store['active_learning_steps'][63]['evaluation_metrics']={'accuracy': 0.9448, 'crossentropy': 0.4180154296875}
store['active_learning_steps'][63]['acquisition']={'indices': [42415, 55244, 28632, 29759, 28319], 'labels': [7, 7, 7, 5, 9], 'scores': [0.9703038930892944, 0.9315861463546753, 0.9079238772392273, 0.8958117365837097, 0.8887676000595093]}
store['active_learning_steps'].append({})
store['active_learning_steps'][64]['training']={}
store['active_learning_steps'][64]['training']['epochs']=[]
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 1.2044546604156494})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6815962195396423})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.45048654079437256})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.42532220482826233})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.4311296343803406})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.4359121322631836})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.4168747663497925})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3778795003890991})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.4068964719772339})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.43985435366630554})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.4127269685268402})
store['active_learning_steps'][64]['training']['best_epoch']=8
store['active_learning_steps'][64]['evaluation_metrics']={'accuracy': 0.9558, 'crossentropy': 0.3578193359375}
store['active_learning_steps'][64]['acquisition']={'indices': [49910, 788, 54954, 48681, 36744], 'labels': [6, 9, 8, 2, 1], 'scores': [0.9874034523963928, 0.9816873669624329, 0.9370867609977722, 0.9327896237373352, 0.9323641657829285]}
store['active_learning_steps'].append({})
store['active_learning_steps'][65]['training']={}
store['active_learning_steps'][65]['training']['epochs']=[]
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.7880859375, 'crossentropy': 1.2310672998428345})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6895684599876404})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.46322357654571533})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.45421749353408813})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.42406389117240906})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.49633854627609253})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.4106042981147766})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.39494216442108154})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.39717990159988403})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.44248679280281067})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.47400587797164917})
store['active_learning_steps'][65]['training']['best_epoch']=8
store['active_learning_steps'][65]['evaluation_metrics']={'accuracy': 0.9607, 'crossentropy': 0.3606874267578125}
store['active_learning_steps'][65]['acquisition']={'indices': [32387, 29320, 46021, 22561, 42787], 'labels': [4, 1, 9, 6, 4], 'scores': [1.1000482439994812, 1.026605486869812, 1.0170960426330566, 1.0064522624015808, 0.9597046971321106]}
store['active_learning_steps'].append({})
store['active_learning_steps'][66]['training']={}
store['active_learning_steps'][66]['training']['epochs']=[]
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 1.342237949371338})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6493642926216125})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.47334372997283936})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.4173172116279602})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.4472540020942688})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.39042603969573975})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.42779800295829773})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.38474196195602417})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3963988423347473})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.443867951631546})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.4341496229171753})
store['active_learning_steps'][66]['training']['best_epoch']=8
store['active_learning_steps'][66]['evaluation_metrics']={'accuracy': 0.9622, 'crossentropy': 0.35041025390625}
store['active_learning_steps'][66]['acquisition']={'indices': [14210, 27420, 30883, 1254, 7949], 'labels': [-1, -1, 3, -1, -1], 'scores': [1.0785471200942993, 1.0244635343551636, 1.0212536454200745, 1.0210109949111938, 1.020812749862671]}
store['active_learning_steps'].append({})
store['active_learning_steps'][67]['training']={}
store['active_learning_steps'][67]['training']['epochs']=[]
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.748046875, 'crossentropy': 1.2486937046051025})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6434377431869507})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5674161911010742})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5781903266906738})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.44781482219696045})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.41811254620552063})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.4578242301940918})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.45218443870544434})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.3972201645374298})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.4613420069217682})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.4508180320262909})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.4587029218673706})
store['active_learning_steps'][67]['training']['best_epoch']=9
store['active_learning_steps'][67]['evaluation_metrics']={'accuracy': 0.9543, 'crossentropy': 0.384932666015625}
store['active_learning_steps'][67]['acquisition']={'indices': [48360, 24164, 1376, 26358, 25701], 'labels': [3, 9, 7, 3, -1], 'scores': [1.025238573551178, 0.9981845617294312, 0.9862961769104004, 0.9806300401687622, 0.9719029664993286]}
store['active_learning_steps'].append({})
store['active_learning_steps'][68]['training']={}
store['active_learning_steps'][68]['training']['epochs']=[]
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.8046875, 'crossentropy': 1.2865533828735352})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.6631479263305664})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.5249767303466797})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.4755856990814209})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.4659324288368225})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.4402482509613037})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.4516277313232422})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.441558837890625})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.46531423926353455})
store['active_learning_steps'][68]['training']['best_epoch']=6
store['active_learning_steps'][68]['evaluation_metrics']={'accuracy': 0.9504, 'crossentropy': 0.4092460693359375}
store['active_learning_steps'][68]['acquisition']={'indices': [41933, 43897, 7949, 52889, 27877], 'labels': [5, 1, -1, -1, 5], 'scores': [0.9556019306182861, 0.9350645542144775, 0.9168790578842163, 0.8991449475288391, 0.8938288688659668]}
store['active_learning_steps'].append({})
store['active_learning_steps'][69]['training']={}
store['active_learning_steps'][69]['training']['epochs']=[]
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.712890625, 'crossentropy': 1.3375358581542969})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6530293226242065})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.47899848222732544})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.39077329635620117})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.480330228805542})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.4204883575439453})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.46461260318756104})
store['active_learning_steps'][69]['training']['best_epoch']=4
store['active_learning_steps'][69]['evaluation_metrics']={'accuracy': 0.9541, 'crossentropy': 0.3903024658203125}
store['active_learning_steps'][69]['acquisition']={'indices': [27296, 53844, 50403, 9390, 23404], 'labels': [-1, 5, -1, -1, -1], 'scores': [0.8457155227661133, 0.8401300311088562, 0.8344098925590515, 0.8271753787994385, 0.8240681290626526]}
store['active_learning_steps'].append({})
store['active_learning_steps'][70]['training']={}
store['active_learning_steps'][70]['training']['epochs']=[]
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.75, 'crossentropy': 1.2353605031967163})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6992958188056946})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.4949479401111603})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.47663262486457825})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.4300186038017273})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.41539710760116577})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.4424102306365967})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.4448873996734619})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.4473298192024231})
store['active_learning_steps'][70]['training']['best_epoch']=6
store['active_learning_steps'][70]['evaluation_metrics']={'accuracy': 0.9552, 'crossentropy': 0.3792806396484375}
store['active_learning_steps'][70]['acquisition']={'indices': [34328, 39561, 14790, 43648, 47036], 'labels': [8, 2, 9, 5, 2], 'scores': [0.9056374430656433, 0.9023748934268951, 0.8873529434204102, 0.8860073089599609, 0.8699401021003723]}
store['active_learning_steps'].append({})
store['active_learning_steps'][71]['training']={}
store['active_learning_steps'][71]['training']['epochs']=[]
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 1.2460473775863647})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6752355098724365})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.5215872526168823})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.4786994457244873})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.461317777633667})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.44178393483161926})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.4513302445411682})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.38541364669799805})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.4847728908061981})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.39975810050964355})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3923633098602295})
store['active_learning_steps'][71]['training']['best_epoch']=8
store['active_learning_steps'][71]['evaluation_metrics']={'accuracy': 0.958, 'crossentropy': 0.3829880126953125}
store['active_learning_steps'][71]['acquisition']={'indices': [34946, 8606, 37122, 14210, 37578], 'labels': [8, -1, -1, -1, -1], 'scores': [0.9577367305755615, 0.9503027200698853, 0.9428512454032898, 0.9427598118782043, 0.9345623254776001]}
store['active_learning_steps'].append({})
store['active_learning_steps'][72]['training']={}
store['active_learning_steps'][72]['training']['epochs']=[]
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 1.5247726440429688})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.8172780275344849})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.5132298469543457})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.4744040071964264})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.42329856753349304})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.4197767376899719})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.48448166251182556})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.4293563961982727})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.4208924174308777})
store['active_learning_steps'][72]['training']['best_epoch']=6
store['active_learning_steps'][72]['evaluation_metrics']={'accuracy': 0.9572, 'crossentropy': 0.401190087890625}
store['active_learning_steps'][72]['acquisition']={'indices': [9677, 45422, 30932, 4153, 6832], 'labels': [0, 0, 0, 2, 0], 'scores': [0.9976401925086975, 0.98371422290802, 0.9474984407424927, 0.938927412033081, 0.9259886145591736]}
store['active_learning_steps'].append({})
store['active_learning_steps'][73]['training']={}
store['active_learning_steps'][73]['training']['epochs']=[]
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.7236328125, 'crossentropy': 1.4360194206237793})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.7149596214294434})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.5352845191955566})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.5016254186630249})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.4598905146121979})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.44262179732322693})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.41620123386383057})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.41241273283958435})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3599928617477417})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.4295850396156311})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.4172469973564148})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.44402366876602173})
store['active_learning_steps'][73]['training']['best_epoch']=9
store['active_learning_steps'][73]['evaluation_metrics']={'accuracy': 0.9607, 'crossentropy': 0.363886474609375}
store['active_learning_steps'][73]['acquisition']={'indices': [53324, 7949, 32016, 2682, 14735], 'labels': [9, -1, 9, 8, 9], 'scores': [0.9987190961837769, 0.9944959282875061, 0.9590456485748291, 0.9552211761474609, 0.9551492929458618]}
store['active_learning_steps'].append({})
store['active_learning_steps'][74]['training']={}
store['active_learning_steps'][74]['training']['epochs']=[]
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.7236328125, 'crossentropy': 1.2875597476959229})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.7354514002799988})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.5183277726173401})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.4035196304321289})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3895898461341858})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3858926296234131})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.36462295055389404})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3739505112171173})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.40146559476852417})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.36440950632095337})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.41112616658210754})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.38565877079963684})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.38045358657836914})
store['active_learning_steps'][74]['training']['best_epoch']=10
store['active_learning_steps'][74]['evaluation_metrics']={'accuracy': 0.9609, 'crossentropy': 0.375430615234375}
store['active_learning_steps'][74]['acquisition']={'indices': [37078, 42438, 12748, 57154, 20746], 'labels': [8, 9, 0, 0, 1], 'scores': [1.0773529410362244, 1.0167747139930725, 1.0162448287010193, 1.005816638469696, 1.0012252926826477]}
store['active_learning_steps'].append({})
store['active_learning_steps'][75]['training']={}
store['active_learning_steps'][75]['training']['epochs']=[]
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 1.3688478469848633})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.7362363338470459})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.4994378089904785})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.4421267807483673})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.4338111877441406})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.39198940992355347})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.4435216784477234})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.42246368527412415})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.4116054177284241})
store['active_learning_steps'][75]['training']['best_epoch']=6
store['active_learning_steps'][75]['evaluation_metrics']={'accuracy': 0.9588, 'crossentropy': 0.3797227294921875}
store['active_learning_steps'][75]['acquisition']={'indices': [31738, 28536, 59286, 47626, 59294], 'labels': [8, 3, 8, -1, 8], 'scores': [0.9559967517852783, 0.9426347017288208, 0.9257563948631287, 0.9228373765945435, 0.9106189012527466]}
store['active_learning_steps'].append({})
store['active_learning_steps'][76]['training']={}
store['active_learning_steps'][76]['training']['epochs']=[]
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 1.28410005569458})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.6355128884315491})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.5236170291900635})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.41585731506347656})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.38541579246520996})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.37778139114379883})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3558659255504608})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3612060248851776})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3898288607597351})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.4036206901073456})
store['active_learning_steps'][76]['training']['best_epoch']=7
store['active_learning_steps'][76]['evaluation_metrics']={'accuracy': 0.9625, 'crossentropy': 0.33467158203125}
store['active_learning_steps'][76]['acquisition']={'indices': [18962, 23094, 12940, 33035, 17178], 'labels': [7, 7, 5, -1, 8], 'scores': [1.0139572024345398, 0.9672205448150635, 0.9212420582771301, 0.9204548001289368, 0.9083710312843323]}
store['active_learning_steps'].append({})
store['active_learning_steps'][77]['training']={}
store['active_learning_steps'][77]['training']['epochs']=[]
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.7626953125, 'crossentropy': 1.1863594055175781})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6755635738372803})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.484205961227417})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.4380685091018677})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3787766396999359})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.4006204903125763})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.40485355257987976})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.4321991801261902})
store['active_learning_steps'][77]['training']['best_epoch']=5
store['active_learning_steps'][77]['evaluation_metrics']={'accuracy': 0.9558, 'crossentropy': 0.36584599609375}
store['active_learning_steps'][77]['acquisition']={'indices': [54858, 45024, 5303, 6474, 32747], 'labels': [3, 5, -1, 6, 8], 'scores': [0.8858262300491333, 0.8766451478004456, 0.8546938896179199, 0.8500467538833618, 0.8358923196792603]}
store['active_learning_steps'].append({})
store['active_learning_steps'][78]['training']={}
store['active_learning_steps'][78]['training']['epochs']=[]
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 1.4422717094421387})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.6489425301551819})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.5372927188873291})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.47580376267433167})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.4679354429244995})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.46069416403770447})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.4073725938796997})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.41090935468673706})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.4355764389038086})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.4238013029098511})
store['active_learning_steps'][78]['training']['best_epoch']=7
store['active_learning_steps'][78]['evaluation_metrics']={'accuracy': 0.9563, 'crossentropy': 0.3804553466796875}
store['active_learning_steps'][78]['acquisition']={'indices': [16795, 19089, 12018, 22497, 31650], 'labels': [7, 5, 7, 7, 5], 'scores': [0.9317578077316284, 0.9316399097442627, 0.9310387969017029, 0.9225368499755859, 0.9097951650619507]}
store['active_learning_steps'].append({})
store['active_learning_steps'][79]['training']={}
store['active_learning_steps'][79]['training']['epochs']=[]
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.7607421875, 'crossentropy': 1.3601360321044922})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.7421231269836426})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5444008111953735})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.4970795512199402})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.39541149139404297})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.44567471742630005})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.45469027757644653})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3713570833206177})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.38998740911483765})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.4122923016548157})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.44566482305526733})
store['active_learning_steps'][79]['training']['best_epoch']=8
store['active_learning_steps'][79]['evaluation_metrics']={'accuracy': 0.956, 'crossentropy': 0.3821806396484375}
store['active_learning_steps'][79]['acquisition']={'indices': [11482, 47626, 50459, 7949, 29672], 'labels': [8, -1, 8, -1, 9], 'scores': [1.0788305401802063, 1.0277409553527832, 0.989772617816925, 0.9810957908630371, 0.9725255370140076]}
store['active_learning_steps'].append({})
store['active_learning_steps'][80]['training']={}
store['active_learning_steps'][80]['training']['epochs']=[]
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.728515625, 'crossentropy': 1.3055264949798584})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.6408770680427551})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.47613510489463806})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.41667473316192627})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.4132345914840698})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.4572972357273102})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.41398927569389343})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.325735867023468})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3301717936992645})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3900129497051239})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.4060520827770233})
store['active_learning_steps'][80]['training']['best_epoch']=8
store['active_learning_steps'][80]['evaluation_metrics']={'accuracy': 0.964, 'crossentropy': 0.321461181640625}
store['active_learning_steps'][80]['acquisition']={'indices': [13149, 21896, 34188, 12184, 36363], 'labels': [7, 8, 3, 0, 6], 'scores': [0.9430190920829773, 0.9341792464256287, 0.9231313467025757, 0.913194477558136, 0.9027866125106812]}
store['active_learning_steps'].append({})
store['active_learning_steps'][81]['training']={}
store['active_learning_steps'][81]['training']['epochs']=[]
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.7373046875, 'crossentropy': 1.285421371459961})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.6933275461196899})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.5149484872817993})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.41250985860824585})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.42697441577911377})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.37617355585098267})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3654858469963074})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.38568150997161865})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3119903802871704})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.35479724407196045})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.35219255089759827})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3387184143066406})
store['active_learning_steps'][81]['training']['best_epoch']=9
store['active_learning_steps'][81]['evaluation_metrics']={'accuracy': 0.9675, 'crossentropy': 0.3110543212890625}
store['active_learning_steps'][81]['acquisition']={'indices': [4800, 18324, 38698, 57728, 31014], 'labels': [6, 0, 5, 9, -1], 'scores': [1.0568186044692993, 0.9877375364303589, 0.962372362613678, 0.9438324570655823, 0.9375519752502441]}
store['active_learning_steps'].append({})
store['active_learning_steps'][82]['training']={}
store['active_learning_steps'][82]['training']['epochs']=[]
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 1.4956145286560059})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.7325775623321533})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5174356698989868})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.44891291856765747})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.45884793996810913})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3846242427825928})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3780444860458374})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3999900221824646})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.4135017395019531})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.42374688386917114})
store['active_learning_steps'][82]['training']['best_epoch']=7
store['active_learning_steps'][82]['evaluation_metrics']={'accuracy': 0.9578, 'crossentropy': 0.3657457275390625}
store['active_learning_steps'][82]['acquisition']={'indices': [4036, 29885, 49573, 47626, 53919], 'labels': [-1, -1, 2, -1, -1], 'scores': [0.9559028148651123, 0.9458827376365662, 0.9259027242660522, 0.9232022762298584, 0.9202287793159485]}
store['active_learning_steps'].append({})
store['active_learning_steps'][83]['training']={}
store['active_learning_steps'][83]['training']['epochs']=[]
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 1.4296249151229858})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.7727992534637451})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5684860944747925})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.4421291947364807})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.39191192388534546})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3617918789386749})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3825950026512146})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.4165753126144409})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.39427775144577026})
store['active_learning_steps'][83]['training']['best_epoch']=6
store['active_learning_steps'][83]['evaluation_metrics']={'accuracy': 0.9628, 'crossentropy': 0.3484930908203125}
store['active_learning_steps'][83]['acquisition']={'indices': [38974, 50403, 7949, 18307, 10886], 'labels': [1, -1, -1, -1, 1], 'scores': [0.8576503992080688, 0.8524689674377441, 0.8511942625045776, 0.8478292226791382, 0.8360435962677002]}
store['active_learning_steps'].append({})
store['active_learning_steps'][84]['training']={}
store['active_learning_steps'][84]['training']['epochs']=[]
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 1.3345671892166138})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.6826664209365845})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.689629316329956})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.4569927453994751})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.4044928550720215})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.4085690379142761})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3903270959854126})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3877168893814087})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.38110053539276123})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.44368067383766174})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.36908650398254395})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.37773481011390686})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.38399559259414673})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.40573692321777344})
store['active_learning_steps'][84]['training']['best_epoch']=11
store['active_learning_steps'][84]['evaluation_metrics']={'accuracy': 0.962, 'crossentropy': 0.3506897216796875}
store['active_learning_steps'][84]['acquisition']={'indices': [29018, 623, 13195, 50090, 35326], 'labels': [-1, 6, -1, 4, 5], 'scores': [1.0726451873779297, 1.034850537776947, 1.0030831098556519, 0.9932090640068054, 0.9845525026321411]}
store['active_learning_steps'].append({})
store['active_learning_steps'][85]['training']={}
store['active_learning_steps'][85]['training']['epochs']=[]
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 1.4246453046798706})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.7503753900527954})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.566720724105835})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.4610533118247986})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.43236255645751953})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3926316499710083})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.36409124732017517})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3878474831581116})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3992697596549988})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.41963812708854675})
store['active_learning_steps'][85]['training']['best_epoch']=7
store['active_learning_steps'][85]['evaluation_metrics']={'accuracy': 0.9586, 'crossentropy': 0.3603038330078125}
store['active_learning_steps'][85]['acquisition']={'indices': [52889, 15771, 50736, 40766, 20002], 'labels': [-1, 5, -1, 4, -1], 'scores': [1.0489009022712708, 1.018154799938202, 0.9848797917366028, 0.9593286514282227, 0.9465149641036987]}
store['active_learning_steps'].append({})
store['active_learning_steps'][86]['training']={}
store['active_learning_steps'][86]['training']['epochs']=[]
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.7587890625, 'crossentropy': 1.2521710395812988})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.7222236394882202})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.4800458550453186})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.4102991819381714})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.37884944677352905})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.34472012519836426})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3594399094581604})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.354674756526947})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.34202808141708374})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.35073965787887573})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.3201144337654114})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3530258536338806})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.37169429659843445})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3955470025539398})
store['active_learning_steps'][86]['training']['best_epoch']=11
store['active_learning_steps'][86]['evaluation_metrics']={'accuracy': 0.9662, 'crossentropy': 0.3201455810546875}
store['active_learning_steps'][86]['acquisition']={'indices': [3798, 45901, 20720, 52456, 16876], 'labels': [7, 7, 7, 2, -1], 'scores': [1.0913195610046387, 1.063922256231308, 1.0538554787635803, 1.049962043762207, 1.0264429450035095]}
store['active_learning_steps'].append({})
store['active_learning_steps'][87]['training']={}
store['active_learning_steps'][87]['training']['epochs']=[]
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.73046875, 'crossentropy': 1.4507355690002441})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.7605958580970764})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5488345623016357})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.4795990586280823})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.4088764190673828})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.4300399422645569})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.4012702703475952})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.39931920170783997})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3684036433696747})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3440938889980316})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3600877523422241})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.37974637746810913})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3928937315940857})
store['active_learning_steps'][87]['training']['best_epoch']=10
store['active_learning_steps'][87]['evaluation_metrics']={'accuracy': 0.9641, 'crossentropy': 0.333568701171875}
store['active_learning_steps'][87]['acquisition']={'indices': [38090, 7949, 6309, 11295, 50736], 'labels': [5, -1, 3, 0, -1], 'scores': [1.0253103375434875, 0.9960296750068665, 0.9593570232391357, 0.9522872567176819, 0.948722243309021]}
store['active_learning_steps'].append({})
store['active_learning_steps'][88]['training']={}
store['active_learning_steps'][88]['training']['epochs']=[]
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 1.481288194656372})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.7080634832382202})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.609804630279541})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.5111346244812012})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.403266578912735})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.38376808166503906})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.42018502950668335})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.4189709424972534})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3956691026687622})
store['active_learning_steps'][88]['training']['best_epoch']=6
store['active_learning_steps'][88]['evaluation_metrics']={'accuracy': 0.9654, 'crossentropy': 0.3386046875}
store['active_learning_steps'][88]['acquisition']={'indices': [47626, 29501, 49064, 42673, 26150], 'labels': [-1, -1, 8, -1, 5], 'scores': [0.9151113033294678, 0.9103143215179443, 0.901735782623291, 0.887592613697052, 0.8776865601539612]}
store['active_learning_steps'].append({})
store['active_learning_steps'][89]['training']={}
store['active_learning_steps'][89]['training']['epochs']=[]
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.75390625, 'crossentropy': 1.3619000911712646})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.7499616742134094})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5243232250213623})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.42728936672210693})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.37847521901130676})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.39516115188598633})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.41687583923339844})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.35808175802230835})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3617284893989563})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3680952489376068})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3927333354949951})
store['active_learning_steps'][89]['training']['best_epoch']=8
store['active_learning_steps'][89]['evaluation_metrics']={'accuracy': 0.9663, 'crossentropy': 0.3094263916015625}
store['active_learning_steps'][89]['acquisition']={'indices': [30900, 52590, 14305, 3273, 34406], 'labels': [5, -1, 8, 8, 4], 'scores': [0.9462937116622925, 0.938259482383728, 0.915367603302002, 0.9120938777923584, 0.8988569378852844]}
store['active_learning_steps'].append({})
store['active_learning_steps'][90]['training']={}
store['active_learning_steps'][90]['training']['epochs']=[]
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 1.4141709804534912})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.7346799373626709})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5627803802490234})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.44052571058273315})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.40980181097984314})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.37779808044433594})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.4032692015171051})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.40432292222976685})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3593926429748535})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3819442391395569})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.36771658062934875})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3498469889163971})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3784008026123047})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.4112222194671631})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.39548248052597046})
store['active_learning_steps'][90]['training']['best_epoch']=12
store['active_learning_steps'][90]['evaluation_metrics']={'accuracy': 0.9625, 'crossentropy': 0.329611279296875}
store['active_learning_steps'][90]['acquisition']={'indices': [47626, 52086, 59427, 25176, 57416], 'labels': [-1, 5, 1, 4, -1], 'scores': [1.1420000791549683, 1.0883941650390625, 1.0149946808815002, 1.0134297013282776, 1.012814462184906]}
store['active_learning_steps'].append({})
store['active_learning_steps'][91]['training']={}
store['active_learning_steps'][91]['training']['epochs']=[]
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.74609375, 'crossentropy': 1.3646948337554932})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.7107561826705933})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.5107560753822327})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.4518393278121948})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.38114774227142334})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.37431520223617554})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3420299291610718})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3552258014678955})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3758614659309387})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.36964285373687744})
store['active_learning_steps'][91]['training']['best_epoch']=7
store['active_learning_steps'][91]['evaluation_metrics']={'accuracy': 0.9641, 'crossentropy': 0.333424609375}
store['active_learning_steps'][91]['acquisition']={'indices': [41608, 57416, 7768, 52889, 42703], 'labels': [-1, -1, 8, -1, 0], 'scores': [1.0171118378639221, 0.9839043617248535, 0.9751083254814148, 0.9664236307144165, 0.965616762638092]}
store['active_learning_steps'].append({})
store['active_learning_steps'][92]['training']={}
store['active_learning_steps'][92]['training']['epochs']=[]
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 1.4422107934951782})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.769127607345581})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.5319636464118958})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.4209784269332886})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3878890872001648})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.35099220275878906})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3719017505645752})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3773167133331299})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3452160954475403})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.34731218218803406})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3707723021507263})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3352188467979431})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.4024093747138977})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3431530296802521})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3461712598800659})
store['active_learning_steps'][92]['training']['best_epoch']=12
store['active_learning_steps'][92]['evaluation_metrics']={'accuracy': 0.9634, 'crossentropy': 0.32962646484375}
store['active_learning_steps'][92]['acquisition']={'indices': [42199, 55906, 7949, 18003, 49890], 'labels': [3, 2, -1, 2, 5], 'scores': [1.0537886023521423, 1.0009625554084778, 0.9994509220123291, 0.9898668527603149, 0.9651270508766174]}
store['active_learning_steps'].append({})
store['active_learning_steps'][93]['training']={}
store['active_learning_steps'][93]['training']['epochs']=[]
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.806640625, 'crossentropy': 1.331291675567627})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.7177892923355103})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.5011618137359619})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.42075204849243164})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3663177192211151})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.4034733772277832})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.34129980206489563})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.37289565801620483})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.35639917850494385})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.35138559341430664})
store['active_learning_steps'][93]['training']['best_epoch']=7
store['active_learning_steps'][93]['evaluation_metrics']={'accuracy': 0.9644, 'crossentropy': 0.33017451171875}
store['active_learning_steps'][93]['acquisition']={'indices': [13969, 54401, 3980, 7325, 47626], 'labels': [3, -1, 2, 0, -1], 'scores': [0.9469828009605408, 0.9309694170951843, 0.9269568920135498, 0.9234633445739746, 0.9146316051483154]}
store['active_learning_steps'].append({})
store['active_learning_steps'][94]['training']={}
store['active_learning_steps'][94]['training']['epochs']=[]
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.728515625, 'crossentropy': 1.4925813674926758})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.7831426858901978})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.522017240524292})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.4551685154438019})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3484833240509033})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.36723554134368896})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3271295428276062})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.391158789396286})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3622360825538635})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.4024297297000885})
store['active_learning_steps'][94]['training']['best_epoch']=7
store['active_learning_steps'][94]['evaluation_metrics']={'accuracy': 0.965, 'crossentropy': 0.3312275634765625}
store['active_learning_steps'][94]['acquisition']={'indices': [20820, 47626, 52757, 53673, 52422], 'labels': [9, -1, 2, 4, 2], 'scores': [0.9094058573246002, 0.8729760646820068, 0.8691200017929077, 0.8653815388679504, 0.8557779788970947]}
store['active_learning_steps'].append({})
store['active_learning_steps'][95]['training']={}
store['active_learning_steps'][95]['training']['epochs']=[]
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 1.4422190189361572})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.7341328263282776})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.5215176343917847})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.42987731099128723})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.40959784388542175})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.388885498046875})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3979278802871704})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.35627734661102295})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3525378108024597})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.36350196599960327})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3899613618850708})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.38394129276275635})
store['active_learning_steps'][95]['training']['best_epoch']=9
store['active_learning_steps'][95]['evaluation_metrics']={'accuracy': 0.9639, 'crossentropy': 0.3251942626953125}
store['active_learning_steps'][95]['acquisition']={'indices': [25551, 15725, 1518, 53570, 40654], 'labels': [-1, 9, 9, 3, 5], 'scores': [0.9312864542007446, 0.9251298308372498, 0.9215767979621887, 0.9179125428199768, 0.9125240445137024]}
store['active_learning_steps'].append({})
store['active_learning_steps'][96]['training']={}
store['active_learning_steps'][96]['training']['epochs']=[]
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 1.3192863464355469})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.7228946685791016})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5347158908843994})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.44326865673065186})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.36704081296920776})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3609696626663208})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.32782047986984253})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.36179760098457336})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3318943977355957})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.33706894516944885})
store['active_learning_steps'][96]['training']['best_epoch']=7
store['active_learning_steps'][96]['evaluation_metrics']={'accuracy': 0.9598, 'crossentropy': 0.3499284912109375}
store['active_learning_steps'][96]['acquisition']={'indices': [47626, 41608, 40530, 20206, 34942], 'labels': [-1, -1, 2, 7, 9], 'scores': [1.0000970363616943, 0.9339908957481384, 0.9059391021728516, 0.8955276012420654, 0.8797516226768494]}
store['active_learning_steps'].append({})
store['active_learning_steps'][97]['training']={}
store['active_learning_steps'][97]['training']['epochs']=[]
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.5576171875, 'crossentropy': 1.4150590896606445})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.7541350722312927})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.5047270655632019})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3918722867965698})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3477577567100525})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3635382354259491})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.30635106563568115})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3488618731498718})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3636637330055237})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.3200506567955017})
store['active_learning_steps'][97]['training']['best_epoch']=7
store['active_learning_steps'][97]['evaluation_metrics']={'accuracy': 0.9649, 'crossentropy': 0.305502490234375}
store['active_learning_steps'][97]['acquisition']={'indices': [7949, 17958, 45911, 17010, 51180], 'labels': [-1, 9, 3, 3, 7], 'scores': [0.9925925731658936, 0.9625107049942017, 0.9460239410400391, 0.9384889602661133, 0.9380663931369781]}
store['active_learning_steps'].append({})
store['active_learning_steps'][98]['training']={}
store['active_learning_steps'][98]['training']['epochs']=[]
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.734375, 'crossentropy': 1.396594762802124})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.6721680164337158})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.4626912474632263})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.38420820236206055})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.36737769842147827})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3504451811313629})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3911922574043274})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3263712525367737})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.298145592212677})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.32345202565193176})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3281005322933197})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3087172210216522})
store['active_learning_steps'][98]['training']['best_epoch']=9
store['active_learning_steps'][98]['evaluation_metrics']={'accuracy': 0.971, 'crossentropy': 0.2923737060546875}
store['active_learning_steps'][98]['acquisition']={'indices': [47626, 18501, 47297, 41060, 22188], 'labels': [-1, 4, 8, 6, -1], 'scores': [0.937599241733551, 0.924610435962677, 0.9087042808532715, 0.8997393250465393, 0.8953742980957031]}
store['active_learning_steps'].append({})
store['active_learning_steps'][99]['training']={}
store['active_learning_steps'][99]['training']['epochs']=[]
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.7646484375, 'crossentropy': 1.3777329921722412})
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.6955417990684509})
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.49402639269828796})
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.44068092107772827})
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3526490330696106})
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3724699914455414})
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.36194705963134766})
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3733506202697754})
store['active_learning_steps'][99]['training']['best_epoch']=5
store['active_learning_steps'][99]['evaluation_metrics']={'accuracy': 0.9625, 'crossentropy': 0.3500147216796875}
store['active_learning_steps'][99]['acquisition']={'indices': [47626, 16488, 228, 36990, 35482], 'labels': [-1, 9, 3, -1, 4], 'scores': [0.8433204889297485, 0.8241779208183289, 0.7658846974372864, 0.7645419836044312, 0.7643042802810669]}
store['active_learning_steps'].append({})
store['active_learning_steps'][100]['training']={}
store['active_learning_steps'][100]['training']['epochs']=[]
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 1.4276435375213623})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.785947322845459})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.5151557326316833})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.39874517917633057})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.35462963581085205})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.38033413887023926})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.331171452999115})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3467393219470978})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.30934497714042664})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.34417450428009033})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.32752448320388794})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.34706375002861023})
store['active_learning_steps'][100]['training']['best_epoch']=9
store['active_learning_steps'][100]['evaluation_metrics']={'accuracy': 0.9676, 'crossentropy': 0.3062128173828125}
store['active_learning_steps'][100]['acquisition']={'indices': [28844, 15663, 56514, 8867, 7949], 'labels': [2, 0, 2, 8, -1], 'scores': [1.0098846554756165, 1.007330596446991, 0.9689878821372986, 0.9686439633369446, 0.9683429598808289]}
store['active_learning_steps'].append({})
store['active_learning_steps'][101]['training']={}
store['active_learning_steps'][101]['training']['epochs']=[]
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.798828125, 'crossentropy': 1.2435734272003174})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.6901057958602905})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.47752439975738525})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3984493613243103})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.39865177869796753})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3636959493160248})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3622625172138214})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3337807059288025})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.34867721796035767})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.363289475440979})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.33352136611938477})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3430684804916382})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.4068349003791809})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.37076836824417114})
store['active_learning_steps'][101]['training']['best_epoch']=11
store['active_learning_steps'][101]['evaluation_metrics']={'accuracy': 0.9682, 'crossentropy': 0.2976332763671875}
store['active_learning_steps'][101]['acquisition']={'indices': [27576, 32276, 24630, 8883, 13242], 'labels': [5, 3, 5, 2, 3], 'scores': [1.0169570446014404, 0.985798180103302, 0.9722967743873596, 0.9395323395729065, 0.9378965497016907]}
store['active_learning_steps'].append({})
store['active_learning_steps'][102]['training']={}
store['active_learning_steps'][102]['training']['epochs']=[]
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 1.458815097808838})
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.8133237361907959})
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5640284419059753})
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.4466741681098938})
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.412742018699646})
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3362951874732971})
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.33519071340560913})
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.33549466729164124})
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3609556257724762})
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.34611213207244873})
store['active_learning_steps'][102]['training']['best_epoch']=7
store['active_learning_steps'][102]['evaluation_metrics']={'accuracy': 0.9685, 'crossentropy': 0.31308583984375}
store['active_learning_steps'][102]['acquisition']={'indices': [21900, 32638, 29018, 32823, 56196], 'labels': [6, -1, -1, -1, -1], 'scores': [1.021787166595459, 0.9432416558265686, 0.931435227394104, 0.923775315284729, 0.9065467715263367]}
store['active_learning_steps'].append({})
store['active_learning_steps'][103]['training']={}
store['active_learning_steps'][103]['training']['epochs']=[]
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 1.4331790208816528})
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.7066620588302612})
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.4864751100540161})
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.3732501268386841})
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.40292033553123474})
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.35975706577301025})
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.32803720235824585})
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.3025400638580322})
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.32517382502555847})
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.33441105484962463})
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.33957409858703613})
store['active_learning_steps'][103]['training']['best_epoch']=8
store['active_learning_steps'][103]['evaluation_metrics']={'accuracy': 0.9686, 'crossentropy': 0.284099951171875}
store['active_learning_steps'][103]['acquisition']={'indices': [15434, 1522, 52092, 19362, 31742], 'labels': [2, 9, 7, 8, 7], 'scores': [0.8941864967346191, 0.8817402720451355, 0.8799052834510803, 0.8785278797149658, 0.8768797814846039]}
store['active_learning_steps'].append({})
store['active_learning_steps'][104]['training']={}
store['active_learning_steps'][104]['training']['epochs']=[]
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.78515625, 'crossentropy': 1.4485875368118286})
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.7157601118087769})
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.5150848627090454})
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.388619065284729})
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3425767421722412})
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3127090632915497})
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3213498294353485})
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3483154773712158})
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.29106536507606506})
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2992175221443176})
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3309650123119354})
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3156370520591736})
store['active_learning_steps'][104]['training']['best_epoch']=9
store['active_learning_steps'][104]['evaluation_metrics']={'accuracy': 0.9716, 'crossentropy': 0.2859525390625}
store['active_learning_steps'][104]['acquisition']={'indices': [8297, 52113, 22139, 22607, 29018], 'labels': [7, 7, 2, 4, -1], 'scores': [0.9978088736534119, 0.959989607334137, 0.9522183537483215, 0.9488608837127686, 0.9396476745605469]}
store['active_learning_steps'].append({})
store['active_learning_steps'][105]['training']={}
store['active_learning_steps'][105]['training']['epochs']=[]
store['active_learning_steps'][105]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 1.5489985942840576})
store['active_learning_steps'][105]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.809280276298523})
store['active_learning_steps'][105]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.5626608729362488})
store['active_learning_steps'][105]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.4361456632614136})
store['active_learning_steps'][105]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.32902228832244873})
store['active_learning_steps'][105]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.35546571016311646})
store['active_learning_steps'][105]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.298744261264801})
store['active_learning_steps'][105]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.3114106059074402})
store['active_learning_steps'][105]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3035687208175659})
store['active_learning_steps'][105]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.28951627016067505})
store['active_learning_steps'][105]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.3353205919265747})
store['active_learning_steps'][105]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2898469567298889})
store['active_learning_steps'][105]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.30721718072891235})
store['active_learning_steps'][105]['training']['best_epoch']=10
store['active_learning_steps'][105]['evaluation_metrics']={'accuracy': 0.9709, 'crossentropy': 0.28807021484375}
