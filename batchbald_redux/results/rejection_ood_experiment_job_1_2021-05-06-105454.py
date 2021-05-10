store = {}
store['timestamp']=1620294894
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/rejection_ood_experiment.py', '--id=1']
store['commit']='2edd2424ec449a84ea20a7324261784a7627b78d'
store['github_url']='2edd2424ec449a84ea20a7324261784a7627b78d'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/rejection_ood_experiment.py'
store['job_id']=1
store['worker_id']=1
store['num_workers']=40
store['config']={'seed': 1, 'acquisition_size': 10, 'max_training_set': 450, 'num_pool_samples': 100, 'num_eval_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'validation_set_size': 1024, 'validation_split_random_state': 0, 'initial_training_set_size': 20, 'samples_per_epoch': 5056, 'mnist_repetitions': 1, 'add_dataset_noise': False, 'acquisition_function': 'batchbald_redux.acquisition_functions.BALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationPoolModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 0.0}
store['log']={}
store['dataset_info']={'training': "(FastMNIST (train; 58976 samples)) + ('OoD Dataset (60000 samples)' | constant_target{'target': tensor(-1, device='cuda:0'), 'num_classes': 10})", 'test': "'FastMNIST (test, 10000 samples)'"}
store['initial_training_set_indices']=[30392, 53434, 12640, 8533, 22304, 37915, 58226, 44119, 3091, 14640, 58125, 39579, 43812, 53689, 52296, 46037, 22015, 40334, 57520, 43803]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 2.2121522426605225})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 2.5924594402313232})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 2.5327870845794678})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 3.0106239318847656})
store['active_learning_steps'][0]['training']['best_epoch']=1
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.6488, 'crossentropy': 2.0698453125}
store['active_learning_steps'][0]['acquisition']={'indices': [8586, 39494, 42053, 13464, 48210, 30790, 47452, 39623, 29706, 39179], 'labels': [9, 0, 0, 0, 0, 0, 0, 0, 0, 9], 'scores': [1.2043094038963318, 1.1812102496623993, 1.1677685976028442, 1.1667768359184265, 1.1625686883926392, 1.1541523337364197, 1.1531119346618652, 1.15297532081604, 1.1510692834854126, 1.1488277316093445]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 2.252762794494629})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 2.6107988357543945})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 3.031553268432617})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 3.024153232574463})
store['active_learning_steps'][1]['training']['best_epoch']=1
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.6703, 'crossentropy': 2.0501962890625}
store['active_learning_steps'][1]['acquisition']={'indices': [19298, 4727, 24589, 10227, 23347, 24223, 10515, 51137, 28432, 8067], 'labels': [6, 8, 8, 5, 8, 8, 8, 5, 8, 8], 'scores': [1.1755862832069397, 1.1451637744903564, 1.1439638137817383, 1.1267607808113098, 1.123361587524414, 1.1230679750442505, 1.1175719499588013, 1.1090205311775208, 1.1065183877944946, 1.103754699230194]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 2.2695536613464355})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 2.746058225631714})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 3.2443084716796875})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 3.4775800704956055})
store['active_learning_steps'][2]['training']['best_epoch']=1
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.6473, 'crossentropy': 2.034992578125}
store['active_learning_steps'][2]['acquisition']={'indices': [24716, 36826, 18971, 49992, 47014, 40085, 26434, 19213, 45256, 57456], 'labels': [5, 6, 6, 5, 6, 6, 2, 2, 5, 6], 'scores': [1.0030938982963562, 0.9910394549369812, 0.9812344312667847, 0.9773728251457214, 0.9683257341384888, 0.963438868522644, 0.9608607888221741, 0.959381639957428, 0.9573959708213806, 0.9557622075080872]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 1.9180097579956055})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 2.2339465618133545})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 2.471327066421509})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 2.91290545463562})
store['active_learning_steps'][3]['training']['best_epoch']=1
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.6977, 'crossentropy': 1.7093892578125}
store['active_learning_steps'][3]['acquisition']={'indices': [20025, 10210, 5728, 18740, 27644, 49138, 54162, 39110, 28192, 5216], 'labels': [8, 3, 3, 8, 3, 4, 8, 4, 9, 2], 'scores': [1.0045056343078613, 0.9842697381973267, 0.9730130434036255, 0.9691183567047119, 0.960141658782959, 0.9591125249862671, 0.9581168293952942, 0.9559171199798584, 0.9548673033714294, 0.9495676159858704]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 1.8512506484985352})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.716796875, 'crossentropy': 1.812027931213379})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 2.1411221027374268})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.712890625, 'crossentropy': 2.1902976036071777})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 2.3399641513824463})
store['active_learning_steps'][4]['training']['best_epoch']=2
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.7481, 'crossentropy': 1.593640625}
store['active_learning_steps'][4]['acquisition']={'indices': [37435, 21219, 24608, 57904, 39918, 37580, 42639, 44382, 44740, 19575], 'labels': [2, 2, 5, 2, 2, 2, 7, 6, 2, 3], 'scores': [1.1187744140625, 1.1059364080429077, 1.073351800441742, 1.066549837589264, 1.0662611722946167, 1.048354685306549, 1.0474143624305725, 1.0461595058441162, 1.0377598404884338, 1.0373343229293823]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7451171875, 'crossentropy': 1.3540911674499512})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.779296875, 'crossentropy': 1.4947476387023926})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.73828125, 'crossentropy': 1.66326904296875})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7548828125, 'crossentropy': 1.9845333099365234})
store['active_learning_steps'][5]['training']['best_epoch']=1
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.7754, 'crossentropy': 1.16657529296875}
store['active_learning_steps'][5]['acquisition']={'indices': [18356, 45085, 32427, 25234, 37743, 14121, 27225, 54065, 12903, 25960], 'labels': [2, 2, 0, 4, 2, 2, 7, 7, 9, 4], 'scores': [0.9709051847457886, 0.9689170718193054, 0.9604719281196594, 0.9490630626678467, 0.925301730632782, 0.9236418604850769, 0.9144182205200195, 0.9135379195213318, 0.9117810130119324, 0.9096556305885315]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7509765625, 'crossentropy': 1.1914432048797607})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.765625, 'crossentropy': 1.6517207622528076})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.765625, 'crossentropy': 1.7118510007858276})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7626953125, 'crossentropy': 1.8164026737213135})
store['active_learning_steps'][6]['training']['best_epoch']=1
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.7723, 'crossentropy': 1.0834681640625}
store['active_learning_steps'][6]['acquisition']={'indices': [33812, 37089, 667, 46727, 42891, 20869, 49111, 40457, 31253, 15695], 'labels': [6, 5, 0, 2, 2, 3, 0, 0, 5, 0], 'scores': [0.9009250998497009, 0.8621160984039307, 0.8620225191116333, 0.8601855039596558, 0.8412589430809021, 0.8384357690811157, 0.836821436882019, 0.8345786929130554, 0.8328436613082886, 0.8244727849960327]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7666015625, 'crossentropy': 1.0886214971542358})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7646484375, 'crossentropy': 1.4916982650756836})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7587890625, 'crossentropy': 1.5198254585266113})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7705078125, 'crossentropy': 1.5130786895751953})
store['active_learning_steps'][7]['training']['best_epoch']=1
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.7775, 'crossentropy': 1.08923583984375}
store['active_learning_steps'][7]['acquisition']={'indices': [19089, 49991, 10800, 9725, 32409, 57987, 14705, 21550, 58560, 47651], 'labels': [5, 5, 8, 2, 3, 5, 0, 5, 0, 3], 'scores': [0.7898718118667603, 0.7783215045928955, 0.7771059274673462, 0.7768348455429077, 0.775007426738739, 0.7735195755958557, 0.7697927951812744, 0.767671525478363, 0.7662169933319092, 0.7610833048820496]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.744140625, 'crossentropy': 1.1655535697937012})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.751953125, 'crossentropy': 1.417870044708252})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.76171875, 'crossentropy': 1.485708475112915})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.759765625, 'crossentropy': 1.6219619512557983})
store['active_learning_steps'][8]['training']['best_epoch']=1
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.7473, 'crossentropy': 1.1500125}
store['active_learning_steps'][8]['acquisition']={'indices': [51986, 8417, 55513, 42368, 8978, 12413, 13333, 942, 9810, 18405], 'labels': [2, 6, 5, 7, 2, 7, 7, 7, 9, 9], 'scores': [0.7555849552154541, 0.7451963424682617, 0.7253512740135193, 0.7221888899803162, 0.7217983603477478, 0.7189961671829224, 0.7166473865509033, 0.7157453298568726, 0.7088638544082642, 0.7051532864570618]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7294921875, 'crossentropy': 1.1081249713897705})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7919921875, 'crossentropy': 1.0863621234893799})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7626953125, 'crossentropy': 1.3895409107208252})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.77734375, 'crossentropy': 1.4111461639404297})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 1.4590420722961426})
store['active_learning_steps'][9]['training']['best_epoch']=2
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.8131, 'crossentropy': 0.981582421875}
store['active_learning_steps'][9]['acquisition']={'indices': [1812, 5474, 26444, 15250, 3644, 50688, 12416, 4066, 53170, 17756], 'labels': [4, 8, 1, 3, 1, 3, 3, 1, 8, 8], 'scores': [1.0016024708747864, 0.9422061443328857, 0.9385218024253845, 0.9172753095626831, 0.9077378511428833, 0.9027760624885559, 0.8982706665992737, 0.8942011594772339, 0.8934594392776489, 0.8915116786956787]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7685546875, 'crossentropy': 1.015019178390503})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 0.9539483785629272})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7978515625, 'crossentropy': 1.15372896194458})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 1.207193374633789})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 1.2373989820480347})
store['active_learning_steps'][10]['training']['best_epoch']=2
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.8337, 'crossentropy': 0.89289443359375}
store['active_learning_steps'][10]['acquisition']={'indices': [30441, 41591, 11229, 16971, 3268, 33383, 37843, 51195, 12647, 17005], 'labels': [1, 1, 1, 1, 6, 1, 1, 1, 1, 1], 'scores': [1.0290527939796448, 0.9924963712692261, 0.9867254495620728, 0.9860463738441467, 0.9767888188362122, 0.9763020873069763, 0.9699808955192566, 0.9687705039978027, 0.9628416895866394, 0.9607369303703308]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.7841796875, 'crossentropy': 0.9637044668197632})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 0.9547357559204102})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 1.005540132522583})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 1.0743169784545898})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 1.0777513980865479})
store['active_learning_steps'][11]['training']['best_epoch']=2
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.8517, 'crossentropy': 0.82510009765625}
store['active_learning_steps'][11]['acquisition']={'indices': [50517, 19637, 43173, 16929, 24295, 21448, 14411, 4549, 33740, 15949], 'labels': [4, 4, 4, 4, 4, 4, 4, 4, 4, 5], 'scores': [1.0514326691627502, 1.0238561034202576, 1.0082582831382751, 0.9924657344818115, 0.9911891222000122, 0.9790988564491272, 0.97068190574646, 0.959043562412262, 0.9458414912223816, 0.9444531798362732]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.7939453125, 'crossentropy': 0.9185553789138794})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 0.8562625050544739})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.8189975023269653})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.8429904580116272})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.9388980269432068})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 1.1008881330490112})
store['active_learning_steps'][12]['training']['best_epoch']=3
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.8865, 'crossentropy': 0.70700732421875}
store['active_learning_steps'][12]['acquisition']={'indices': [49088, 48096, 48098, 12934, 12117, 4061, 42671, 6152, 31664, 54885], 'labels': [8, 7, 7, 8, 3, 7, 2, 8, 3, 6], 'scores': [1.0094546675682068, 0.9916918873786926, 0.9653198719024658, 0.9636710286140442, 0.9570828676223755, 0.9552646279335022, 0.953481912612915, 0.9513043165206909, 0.9455084800720215, 0.9454894661903381]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.8633749485015869})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.7646464705467224})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.7970191240310669})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.7321069836616516})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.8528423309326172})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.8151853084564209})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.8481455445289612})
store['active_learning_steps'][13]['training']['best_epoch']=4
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.9016, 'crossentropy': 0.65709892578125}
store['active_learning_steps'][13]['acquisition']={'indices': [16210, 23059, 42323, 22481, 15803, 45502, 16692, 49395, 15899, 58470], 'labels': [5, 1, 2, 7, 1, 1, 5, 1, 9, 9], 'scores': [1.0939382314682007, 1.0731951594352722, 1.0685124397277832, 1.0654206275939941, 1.052557110786438, 1.0514504313468933, 1.050248622894287, 1.0498250722885132, 1.0390708446502686, 1.0353035926818848]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 0.8938325643539429})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.6906057000160217})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.7431834936141968})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.7355366945266724})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6932349801063538})
store['active_learning_steps'][14]['training']['best_epoch']=2
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.8983, 'crossentropy': 0.60418359375}
store['active_learning_steps'][14]['acquisition']={'indices': [46794, 32323, 33364, 37696, 39611, 22561, 25332, 58024, 50618, 59747], 'labels': [8, 5, 2, 2, 8, 6, 2, 8, 6, 5], 'scores': [0.8760099411010742, 0.8628912568092346, 0.853233277797699, 0.8388847708702087, 0.8384644985198975, 0.832892119884491, 0.8319365382194519, 0.8311620950698853, 0.8280729651451111, 0.8248732089996338]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 0.9397203922271729})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.6468567848205566})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.6589887142181396})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6629244089126587})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.7578427195549011})
store['active_learning_steps'][15]['training']['best_epoch']=2
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.9011, 'crossentropy': 0.60985185546875}
store['active_learning_steps'][15]['acquisition']={'indices': [55743, 57334, 29764, 8443, 33057, 2856, 42504, 16756, 13149, 41608], 'labels': [3, 7, 4, 2, 7, 4, 8, 7, 7, -1], 'scores': [0.8556972146034241, 0.8178654909133911, 0.8121174573898315, 0.7981507182121277, 0.7905545234680176, 0.7834882736206055, 0.7833880186080933, 0.7824324369430542, 0.7814395427703857, 0.7785087823867798]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 0.9142423868179321})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.670916736125946})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5948553085327148})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5933980941772461})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6977521181106567})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6753984689712524})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6812130808830261})
store['active_learning_steps'][16]['training']['best_epoch']=4
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.9221, 'crossentropy': 0.5112900390625}
store['active_learning_steps'][16]['acquisition']={'indices': [32065, 11534, 37469, 16488, 23140, 9948, 2548, 26733, 19942, 2352], 'labels': [2, 7, 2, 9, 7, 8, 4, 2, 5, 0], 'scores': [1.0073153376579285, 1.0013797283172607, 0.9957747459411621, 0.9914574325084686, 0.9884425401687622, 0.9853622317314148, 0.9699037075042725, 0.9539868831634521, 0.9468109011650085, 0.938647449016571]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.8587538003921509})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5101724863052368})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.5736855268478394})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.54166179895401})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6539676189422607})
store['active_learning_steps'][17]['training']['best_epoch']=2
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.9215, 'crossentropy': 0.503323193359375}
store['active_learning_steps'][17]['acquisition']={'indices': [57972, 50459, 41933, 11711, 9472, 59468, 5316, 28412, 4153, 36080], 'labels': [4, 8, 5, 2, 2, 7, 9, 0, 2, 9], 'scores': [0.889121413230896, 0.8795361518859863, 0.8672208189964294, 0.8522332906723022, 0.8346003293991089, 0.8222895264625549, 0.8037393093109131, 0.7988951206207275, 0.7945821285247803, 0.7901226282119751]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 0.9678435325622559})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6177893877029419})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5833195447921753})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5632190704345703})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5651533603668213})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5879220962524414})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.6619315147399902})
store['active_learning_steps'][18]['training']['best_epoch']=4
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.9194, 'crossentropy': 0.5346958984375}
store['active_learning_steps'][18]['acquisition']={'indices': [17079, 20641, 48006, 37339, 47949, 49525, 45048, 42784, 6236, 52688], 'labels': [6, 9, 6, 4, 5, 8, 4, 7, 6, 6], 'scores': [1.0281116962432861, 1.0041984915733337, 0.9918924570083618, 0.9894640445709229, 0.9732736349105835, 0.9697350263595581, 0.9659131169319153, 0.9630950689315796, 0.9509865641593933, 0.9406678080558777]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.78515625, 'crossentropy': 0.947253406047821})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5605801939964294})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.5687879323959351})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.580477774143219})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6291993260383606})
store['active_learning_steps'][19]['training']['best_epoch']=2
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.9164, 'crossentropy': 0.53413857421875}
store['active_learning_steps'][19]['acquisition']={'indices': [37044, 43042, 42703, 40312, 55628, 38567, 34520, 20363, 18501, 43065], 'labels': [6, 8, 0, 0, 3, 4, 6, 8, 4, 3], 'scores': [0.766154408454895, 0.7661280035972595, 0.7604394555091858, 0.7550605535507202, 0.7526923418045044, 0.7390016317367554, 0.7374626398086548, 0.7363971471786499, 0.7349272966384888, 0.7345757484436035]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 0.9807548522949219})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5546165704727173})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.47319236397743225})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.4725581109523773})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.4801497459411621})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5188328623771667})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.506960928440094})
store['active_learning_steps'][20]['training']['best_epoch']=4
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.9328, 'crossentropy': 0.448704345703125}
store['active_learning_steps'][20]['acquisition']={'indices': [53872, 22824, 34328, 12650, 39355, 51426, 54971, 49039, 54239, 28536], 'labels': [8, 9, 8, 5, 8, -1, -1, -1, -1, 3], 'scores': [0.9794691801071167, 0.9473055601119995, 0.9403836131095886, 0.938088595867157, 0.9341717958450317, 0.928241491317749, 0.921386182308197, 0.9195757508277893, 0.9159762859344482, 0.9129143953323364]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 0.9831149578094482})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6416916847229004})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5681429505348206})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5464550256729126})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.529773473739624})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5415596961975098})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5660134553909302})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.6218298077583313})
store['active_learning_steps'][21]['training']['best_epoch']=5
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.9304, 'crossentropy': 0.46432138671875}
